#!/usr/bin/env bash

err ()
{
    >&2 echo "ERR> $*"
}

fatal ()
{
    err $*
    exit 1
}

source env || fatal "No env file found, see README"
poetry run jirashell -s ${JIRA_ENDPOINT} -u ${JIRA_USERNAME} -p ${JIRA_PASSWORD}