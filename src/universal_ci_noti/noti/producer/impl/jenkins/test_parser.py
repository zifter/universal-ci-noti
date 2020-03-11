from universal_ci_noti.noti.producer.impl.jenkins.parser import JenkinsResponseParser
from universal_ci_noti.noti.types import Build, BuildStatus, JobResult, SCMInfo
from universal_ci_noti.vcs import VCS


def test_parse_job_result():
    noti = {
        "name": "asgard",
        "url": "job/asgard/",
        "build": {
            "full_url": "http://localhost:8080/job/asgard/18/",
            "number": 18,
            "phase": "COMPLETED",
            "status": "SUCCESS",
            "url": "job/asgard/18/",
            "scm": {
                "url": "https://github.com/evgeny-goldin/asgard.git",
                "branch": "origin/master",
                "commit": "c6d86dc654b12425e706bcf951adfe5a8627a517",
            },
            "artifacts": {
                "asgard.war": {
                    "archive": "http://localhost:8080/job/asgard/18/artifact/asgard.war"
                },
                "asgard-standalone.jar": {
                    "archive": "http://localhost:8080/job/asgard/18/artifact/asgard-standalone.jar",
                    "s3": "https://s3-eu-west-1.amazonaws.com/evgenyg-bakery/asgard/asgard-standalone.jar",
                },
            },
        },
    }

    parser = JenkinsResponseParser(VCS.create())
    result = parser.job_result(noti)

    expected = JobResult()
    expected.url = "http://localhost:8080/job/asgard/18/"

    expected.build = Build()
    expected.build.status = BuildStatus.SUCCESS
    expected.build.number = "18"

    expected.build.scm = SCMInfo()
    expected.build.scm.url = "https://github.com/evgeny-goldin/asgard.git"
    expected.build.scm.branch = "origin/master"
    expected.build.scm.commit = "c6d86dc654b12425e706bcf951adfe5a8627a517"
    expected.build.scm.name = "asgard"
    expected.build.scm.committer = None

    assert result == expected
