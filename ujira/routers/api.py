from fastapi import APIRouter
import ujira.proxy as proxy
import ujira.fmt as fmt
from ujira.config import get_config
import pickle

router = APIRouter(prefix="/api", tags=["api"])


# issue.fields.comment.comments
@router.get("/issues/{issue_key}")
async def ticket(issue_key):
    issue = await proxy.get_issue(issue_key)
    return fmt.issue(issue)


@router.get("/queries")
async def queries():
    return [
        fmt.query(key, q)
        for key, q in get_config().queries.items()
    ]


@router.get("/queries/{query_key}")
async def query(query_key):
    issues = await proxy.search_issues(get_config().queries[query_key].jql)

    with open(f"query_{query_key}.p", "wb") as f:
        pickle.dump([fmt.issue(i) for i in issues], f)

    return [
        fmt.issue(i)
        for i in issues
    ]
