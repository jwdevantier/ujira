import dominate as dom
from dominate.tags import *
from pydantic import BaseModel
from fastapi.responses import HTMLResponse


class PageEntry(BaseModel):
    label: str
    href: str = "#"


@li(cls="px-5")
def page_menu_hdr(label):
    with li(cls="px-5"):
        with div(cls="flex flex-row items-center h-8"):
            div(label, cls="flex font-semibold text-sm text-gray-300 my-4 font-sans")


@li
def page_entry(label, href="#"):
    with a(href=href, cls="relative flex flex-row items-center h-11 focus:outline-none hover:bg-gray-700 text-gray-500 hover:text-gray-200 border-l-4 border-transparent hover:border-blue-500 pr-6"):
        span(label, cls="ml-4 font-semibold text-sm tracking-wide truncate font-sans")


@div(cls="overflow-y-auto overflow-x-hidden flex-grow")
def page_menu(menu_items):
    with ul(cls="flex flex-col py-6 space-y-1"):
        for section in menu_items:
            hdr, entries = section
            page_menu_hdr(hdr)
            for entry in entries:
                page_entry(entry.label, href=entry.href)


def page(body, title=None, menu_items=None):
    doc = dom.document(title=f"ujira | {title}" if title else "ujira")
    with doc.head:
        link(rel="stylesheet", href="https://www.unpkg.com/tailwindcss@2.1.1/dist/tailwind.min.css")
    with div(cls="min-h-screen flex flex-col flex-auto flex-shrink-0 antialiased bg-gray-50 text-gray-800") as container:
        doc += container
        with div(cls="fixed flex flex-col top-0 left-0 w-64 bg-gray-900 h-full shadow-lg"):
            # Menu Header
            with div(cls="flex items-center pl-6 h-20 border-b border-gray-800"):
                with div(cls="my-3"):
                    p("ujira", cls="text-md font-medium tracking-wide text-gray-100 font-sans uppercase")

            # Menu items
            page_menu(menu_items or [])
        div(body, cls="ml-72 flex")

    return HTMLResponse(str(doc))