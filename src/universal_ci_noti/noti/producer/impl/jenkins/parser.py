from universal_ci_noti.noti.types import Build, JobResult, SCMInfo
from universal_ci_noti.vcs import VCS


class JenkinsResponseParser:
    def __init__(self, vcs: VCS):
        self.vcs: VCS = vcs

    def job_result(self, d) -> JobResult:
        repo = self.vcs.repo(d["build"]["scm"]["url"])

        result = JobResult()
        result.url = d["build"]["full_url"]

        result.build = Build()
        result.build.number = str(d["build"]["number"])
        result.build.status = d["build"]["status"].upper()

        result.build.scm = SCMInfo()
        result.build.scm.url = d["build"]["scm"]["url"]
        result.build.scm.branch = d["build"]["scm"]["branch"]
        result.build.scm.commit = d["build"]["scm"]["commit"]
        result.build.scm.committer = repo.get_committer(result.build.scm.commit)
        result.build.scm.name = repo.name()

        return result
