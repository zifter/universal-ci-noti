import abc


class Repository:
    def __init__(self, vcs_type: str):
        self.vcs_type: str = vcs_type

    @abc.abstractmethod
    def name(self):
        """
        Get repository name

        :return:
        """

    @abc.abstractmethod
    def get_committer(self, commit):
        pass
