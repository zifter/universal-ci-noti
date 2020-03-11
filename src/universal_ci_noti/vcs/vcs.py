from typing import List

from universal_ci_noti.vcs.impl import SvnRepository
from universal_ci_noti.vcs.impl.git import GitRepository
from universal_ci_noti.vcs.repo import Repository


class VCS:
    class RepoCreator:
        def __init__(self, detector, creator):
            self.detect = detector
            self.create = creator

    @staticmethod
    def create():
        return VCS(
            [
                VCS.RepoCreator(GitRepository.is_git_repo, GitRepository.create),
                VCS.RepoCreator(SvnRepository.is_svn_repo, SvnRepository.create),
            ]
        )

    def __init__(self, creators: List[RepoCreator]):
        self._creators = creators

    def repo(self, url) -> Repository:
        for c in self._creators:
            if c.detect(url):
                return c.create(url)

        raise RuntimeError(f"Cant create repo for {url}")
