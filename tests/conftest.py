import pytest
import json

github_base_url = "https://api.github.com"


# ToDo: recursively lookup resources directory and generate mocks wherever response.json is present
@pytest.fixture(autouse=True)
def request_register_get_urls(requests_mock):
    # list of repositories
    with open('tests/resources/orgs/docker/repos/response.json', 'r') as fp:
        requests_mock.get(
            f'{github_base_url}/orgs/docker/repos',
            json=json.loads(fp.read())
        )

    # branches for individual repositories
    repos = ['docker-py', 'compose', 'docs']
    for repo in repos:
        with open(f'tests/resources/repos/docker/{repo}/branches/response.json', 'r') as fp:
            requests_mock.get(
                f'{github_base_url}/repos/docker/{repo}/branches',
                json=json.loads(fp.read())
            )

    return requests_mock
