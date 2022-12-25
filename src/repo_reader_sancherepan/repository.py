import requests
from .branch import Branch


class Repository(object):
    """
    A GitHub repository with some basic properties
    """
    session: requests.Session

    def __init__(self, session, data: dict):
        self.session = session

        if "name" in data:
            self.name = data["name"]
        else:
            raise ValueError('bad repository data: expected attribute "name"')

        if "size" in data:
            self.size = data["size"]
        else:
            raise ValueError('bad repository data: expected attribute "size"')

        if "has_issues" in data and data["has_issues"] is True:
            if "open_issues_count" in data:
                self.open_issues_count = data["open_issues_count"]
            else:
                raise ValueError('bad repository data: expected attribute "open_issues_count"')
        else:
            self.open_issues_count = "Issues are not enabled in this repo"

        if "url" in data:
            self.count_branches(data["url"])
        else:
            self.branches = None

    def count_branches(self, repo_url):
        url = f"{repo_url}/branches"
        response = self.session.get(url)
        response.raise_for_status()

        self.branches = [Branch(branch_data) for branch_data in response.json()]
