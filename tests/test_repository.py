import pytest
from src.repo_reader_sancherepan.repo_reader import RepoReader


def test_repo_reader():
    reader = RepoReader("github_token_1337")
    repos = reader.read_repos("docker")

    assert (len(repos) == 3)

    assert (repos[0].name == "docker-py")

    assert (repos[1].size == 23513)
    assert (repos[1].branches is not None)
    assert (len(repos[1].branches) == 15)

    assert (repos[2].open_issues_count == 435)
