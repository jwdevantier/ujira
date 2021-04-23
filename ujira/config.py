from pydantic_yaml import YamlModel
import typing as t


class JiraConfigQuery(YamlModel):
    label: str
    jql: str


class UjiraConfig(YamlModel):
    queries: t.Dict[str, JiraConfigQuery]


def get_config() -> UjiraConfig:
    cfg = getattr(get_config, "_config", None)
    if cfg:
        return cfg
    cfg = UjiraConfig.parse_file("config.yml", content_type="yml")
    setattr(get_config, "_config", cfg)
    return cfg
