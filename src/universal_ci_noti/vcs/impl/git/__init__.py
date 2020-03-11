from universal_ci_noti.vcs.repo import Repository


class GitRepository(Repository):
    @staticmethod
    def is_git_repo(url: str):
        return url.endswith(".git")

    @staticmethod
    def create(url: str):
        return GitRepository(url)

    def __init__(self, url: str):
        super().__init__("git")

        self.url = url

    def name(self):
        return self.url[self.url.rfind("/") + 1 : self.url.rfind(".")]

    def get_committer(self, commit):
        # TODO
        return None
