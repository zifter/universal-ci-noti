from dataclasses import dataclass
from typing import Optional

from dataclasses_json import DataClassJsonMixin


class BuildStatus:
    UNDEFINED = "UNDEFINED"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


@dataclass
class SCMInfo(DataClassJsonMixin):
    url: str = ""
    branch: str = ""
    commit: str = ""

    name: Optional[str] = None
    committer: Optional[str] = None


@dataclass
class Build(DataClassJsonMixin):
    status: BuildStatus = BuildStatus.UNDEFINED
    number: str = ""
    scm: Optional[SCMInfo] = None


@dataclass
class JobResult(DataClassJsonMixin):
    url: str = ""
    build: Optional[Build] = None
