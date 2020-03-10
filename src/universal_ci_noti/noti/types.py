from dataclasses import dataclass
from typing import Optional

from dataclasses_json import DataClassJsonMixin


class JobStatus:
    UNDEFINED = "undefined"
    SUCCESS = "success"
    FAILED = "failed"


@dataclass
class SCMInfo(DataClassJsonMixin):
    name: str
    url: str
    branch: str
    committer: str


@dataclass
class JobResult(DataClassJsonMixin):
    status: JobStatus = JobStatus.UNDEFINED
    scm: Optional[SCMInfo] = None
    url: Optional[str] = None
