# UJIRA

**NOTE**: This application is not finished. It may not ever be either. Feel free to fork.

## The motivation
This project is spawned from the frustrations of working with JIRA with a less-than-optimal connection.
JIRA is bloated. To load an issue page, some ~30+ requests are made in my case, 17+ of which are not cached, 16 of which can only be even initiated sometime after the initial request for a `batch.js` blob has completed.
In anything less than the very best connection scenario, the experience degrades fast.

## What this does
This project is a quick hack which none the less works well for tracking issues.

This project allows you to specify JQL queries in a config file, which will then display in the WEB UI's menu. When clicked, the relevant query is run and the results are displayed in a table view. This is a singular query and is reasonably fast, even under sub-optimal conditions.
To further speed up the process, both JQL query results and individual issues are cached in time-based TTL caches, speeding up navigation as repeat access of results are served from these caches.

## How would I continue?
* Complete the (single) issue view and ensure issues from the issue list lead to it.
* Extend use of the [Jira](https://jira.readthedocs.io/en/master/) & [aiojira](https://pypi.org/project/aiojira/). In particular extend use to modifying tickets (status, summary, description etc) and allow creation of tickets.


## Getting Started

To get started you will need to

1. provide your JIRA credentials and endpoint
2. (optionally) provide additional JQL queries you want to use
3. Install the various back- and front-end dependencies.

### Pointing ujira to your jira installation
`ujira` expects to read an `env` file during startup which defines some environment variables, this is namely
used to configure which JIRA installation to talk to and which credentials to present.

Create an `env` file with the following information, remember to change the values:

```
JIRA_ENDPOINT="https://myjira.mycompany.com"
JIRA_USERNAME="my-username"
JIRA_PASSWORD="my-password"
```

## Backend

1. Install [poetry](https://python-poetry.org) and ensure it is in your $PATH
2. Install dependencies (`poetry install`)