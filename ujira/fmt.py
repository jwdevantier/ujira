from jira.resources import Issue
from ujira.config import JiraConfigQuery
import typing as t


def issue(i: Issue) -> t.Dict[str, t.Any]:
    return {
        # issue key, e.g. FOO-327
        "key": i.key,
        "summary": i.fields.summary,
        "description": i.fields.description,
        "type": i.fields.issuetype.name.lower(),
        "priority": i.fields.priority.name.lower(),
        "components": [c.name for c in i.fields.components],
        "assignee": i.fields.assignee.displayName,
        "reporter": i.fields.reporter.displayName,
        "status": i.fields.status.name.lower(),
    }


def query(key: str, q: JiraConfigQuery) -> t.Dict[str, t.Any]:
    return {
        "key": key,
        "label": q.label,
        "jql": q.jql
    }