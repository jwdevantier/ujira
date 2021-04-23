from pydantic import BaseSettings


class AuthEnv(BaseSettings):
    jira_username: str
    jira_password: str
    jira_endpoint: str

    class Config:
        env_file = "auth.env"


def get_auth() -> AuthEnv:
    inst = getattr(get_auth, "__inst", None)
    if inst:
        return inst
    inst = AuthEnv()
    setattr(get_auth, "__inst", inst)
    return inst