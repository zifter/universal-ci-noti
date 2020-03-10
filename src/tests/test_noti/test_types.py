from universal_ci_noti.noti.types import SCMInfo


def test_scm_from_json():
    info = SCMInfo.from_dict(
        {
            "name": "Backend",
            "url": "https://api.slack.com/ref/",
            "branch": "master",
            "committer": "zifter",
        }
    )

    assert info.name == "Backend"
    assert info.url == "https://api.slack.com/ref/"
    assert info.branch == "master"
    assert info.committer == "zifter"
