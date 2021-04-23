import aiojira
from cachetools import TTLCache
from asyncache import cached
from cachetools import keys
import typing as t
from ujira.auth import AuthEnv


issue_cache = TTLCache(maxsize=1024, ttl=120)
jira: t.Optional[aiojira.JIRA] = None


async def get_jira() -> aiojira.JIRA:
    inst = getattr(get_jira, "__inst", None)
    if inst:
        return inst
    print("proxy.get_jira - acquiring JIRA handle")
    auth = AuthEnv()
    inst = await aiojira.JIRA.create(server=auth.jira_endpoint,
                                     basic_auth=(auth.jira_username, auth.jira_password))
    setattr(get_jira, "__inst", inst)
    return inst


@cached(cache=issue_cache)
async def get_issue(issue_id):
    print("CACHE MISS")
    j = await get_jira()
    return await j.issue(issue_id)


@cached(cache=TTLCache(maxsize=1024, ttl=60))
async def search_issues(jql: str):
    j = await get_jira()
    issues = await j.search_issues(jql)
    for i in issues:
        print(f"caching {i.key}")
        issue_cache[keys.hashkey(i.key)] = i
    return issues
