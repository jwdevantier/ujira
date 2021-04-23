from dominate.tags import *
from ujira.auth import get_auth


def btn(text, href="#", **kwargs):
    base_cls = "py-1 px-2 bg-gray-400 rounded uppercase text-xs font-bold text-white hover:bg-teal-300"
    if "cls" in kwargs:
        kwargs["cls"] = base_cls + " " + kwargs["cls"]
    else:
        kwargs["cls"] = base_cls
    return a(text, href=href, **kwargs)


@table
def issue(issue):
    issue = {"key": "FOO-234", "summary": "Lay plans for world domination", "description": None, "type": "task", "priorty": "highest", "components": ["EvilCorp"], "assignee": "the intern", "reporter": "foot soldier", "status": "to do"}
    issue_key = issue["key"]
    with div(cls="my-4 bg-white border-2 border-gray-300 p-6 rounded-md shadow-lg"):
        h1(issue["summary"], cls="mt-2 text-2xl font-bold text-gray-900")
        with div(cls="mt-2"):
            btn("Open in Jira", href=f"{get_auth().jira_endpoint}/browse/{issue_key}", target="_blank")
        p("nothing yet")
