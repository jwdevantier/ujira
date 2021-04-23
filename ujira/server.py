from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import pickle
from ujira.auth import AuthEnv
from ujira.config import get_config
import ujira.proxy as proxy
from ujira.components.issues_table import issues_table
from ujira.components.page import page, PageEntry
from ujira.routers import api as api
import ujira.fmt as fmt
import ujira.components as component

# TODO: move issue cache out as separate obj
#  on search_issues, add each hit to cache (cache[key] = issue).


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api.router)


@app.on_event("startup")
async def startup_event():
    print("starting server...")
    auth = AuthEnv()
    return  # TODO: remove again when ready
    # await proxy.startup_event(auth)


@app.on_event("shutdown")
async def shutdown_event():
    print("stopping server...")


@app.get("/hello")
async def hello():
    return {"message": "hello, world"}


# TODO: issue view
@app.get("/issues/{issue_key}")
async def show_issue(issue_key):
    return page(component.issue(issue_key))


@app.get("/queries/{query_key}")
async def show_issues(query_key):
    issues = [
        fmt.issue(issue)
        for issue
        in await proxy.search_issues(get_config().queries[query_key].jql)
    ]

    mymenu = [
        ("Issues", (PageEntry(label=query.label, href=query_key)
                     for query_key, query in get_config().queries.items()))
    ]

    return page(issues_table(issues), menu_items=mymenu)



app.mount("/static", StaticFiles(directory="web"), name="static")


@app.get("/{page}", include_in_schema=False)
def root(page):
    print(f"page: {page}")
    try:
        with open(f"web/{page}.html") as f:
            return HTMLResponse(f.read())
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="page not found")
