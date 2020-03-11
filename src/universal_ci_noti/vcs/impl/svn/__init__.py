from universal_ci_noti.vcs.repo import Repository


class SvnRepository(Repository):
    @staticmethod
    def is_svn_repo(url: str):
        # TODO
        return url.startswith("svn")

    @staticmethod
    def create(url: str):
        return SvnRepository(url)

    def __init__(self, url: str):
        super().__init__("svn")

        self.url = url

        raise NotImplementedError()

    # TODO
    def name(self):
        return ""

    def get_committer(self, commit):
        # TODO
        return None
