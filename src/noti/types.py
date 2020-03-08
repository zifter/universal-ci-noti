from typing import Optional


class JobStatus:
    UNDEFINED = 'undefined'
    SUCCESS = 'success'
    FAILED = 'failed'


class SCMInfo:
    def __init__(self, name, url, branch, committer):
        self.repo_name: str = name
        self.repo_url: str = url
        self.branch: str = branch
        self.last_committer: str = committer

    @classmethod
    def from_json(cls, data: dict):
        return cls(data.get('name'), data.get('url'), data.get('branch'), data.get('committer'))


class JobResult:
    def __init__(self):
        self.status: JobStatus = JobStatus.UNDEFINED

        self.scm: SCMInfo = None
        self.job_url: Optional[str] = None

    @classmethod
    def from_json(cls, data):
        result = cls()
        result.status = data['status']
        result.scm = SCMInfo.from_json(data['scm'])
        result.job_url = data['url']

        return result
