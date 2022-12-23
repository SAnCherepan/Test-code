import requests
from .repository import Repository


class RepoReader:

    github_base_url = "https://api.github.com"

    github_org_repos_url = "/orgs/{}/repos"

    def __init__(self, auth_token):
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {auth_token}",
                                     "Accept": "application/vnd.github+json"})

    def read_repos(self, org_name: str):
        url = self.github_base_url + self.github_org_repos_url.format(org_name)
        
        response = self.session.get(url)
        response.raise_for_status()

        repos = [Repository(self.session, repo_data) for repo_data in response.json()]

        return repos
