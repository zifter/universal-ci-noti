from universal_ci_noti.noti.types import SCMInfo


def test_scm_from_json():
    info = SCMInfo.from_json(
        {
            "name": "Backend",
            "url": "https://api.slack.com/ref/",
            "branch": "master",
            "committer": "zifter",
        }
    )

    assert info.repo_name == "Backend"
    assert info.repo_url == "https://api.slack.com/ref/"
    assert info.branch == "master"
    assert info.last_committer == "zifter"
