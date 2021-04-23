from dominate.tags import *


def issue_href(issue_key):
    return f"/issues/{issue_key}"


@tr(cls="border-b border-gray-200 hover:bg-gray-100")
def issue_row(i):
    td(a(i["key"], href=issue_href(i["key"])),
         cls="py-3 px-6 text-left text-blue-500")
    td(i["summary"], cls="py-3 px-6 text-left")
    td([component_label(c) for c in i["components"]], cls="py-3 px-6 text-center")
    td(status_label(i["status"]), cls="py-3 px-6 text-center")
    td(i["assignee"], cls="py-3 px-6 text-center")


def status_label(status):
    color = {"to do": "blue",
     "done": "green",
     "in progress": "yellow",
     "in review": "purple"}[status.lower()]
    return span(status, cls=f"bg-{color}-200 text-{color}-600 py-1 px-3 rounded-full text-xs uppercase font-bold")


def component_label(component):
    return span(component, cls="py-1 px-2 bg-gray-400 rounded uppercase text-xs font-bold text-white hover:bg-teal-300")


@table(cls="mb-4 mt-8")
def issues_table(issues):
    issue_rows = [
        issue_row(i) for i in issues
    ]
    for e in issue_rows[::2]:
        e["class"] = e["class"] + " bg-gray-50"

    thead(tr(th("key", cls="py-3 px-6 text-left"),
                 th("summary", cls="py-3 px-6 text-left"),
                 th("Components", cls="py-3 px-6 text-left"),
                 th("status", cls="py-3 px-6 text-center"),
                 th("assignee", cls="py-3 px-6 text-center"),
                 cls="bg-gray-200 text-gray-600 uppercase text-sm leading-normal"))
    tbody(issue_rows, cls="text-gray-600 text-sm font-light")
