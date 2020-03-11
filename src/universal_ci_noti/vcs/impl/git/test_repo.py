import pytest
from universal_ci_noti.vcs.impl import GitRepository


@pytest.mark.parametrize(
    "url,result",
    [
        ("https://github.com/evgeny-goldin/asgard.git", True),
        ("https://github.com/evgeny-goldin/asgard.svn", False),
    ],
)
def test_is_git_repo(url, result):
    assert GitRepository.is_git_repo(url) == result
