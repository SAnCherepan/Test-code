# Repo reader

This is a simple python package that can be used to get basic list of repositories in a GitHub repository group (a.k.a. organisation).

# Installation

Python package:
```commandline
python -m pip install --index-url https://test.pypi.org/simple/ repo_reader_sancherepan
```

Docker image:
```commandline
docker pull sancherepan/repo-reader
docker run -it --rm sancherepan/repo-reader read-repos --help
```

# Usage

In your code:
```python
from repo_reader_sancherepan.repo_reader import RepoReader

reader = RepoReader("<your_github_auth_token>")
repos = reader.read_repos("<github_repo_group_name>")
```

In command line:
```commandline
read-repos your_github_auth_token github_repo_group_name
```

In docker:
```commandline
docker run -it --rm sancherepan/repo-reader read-repos your_github_auth_token github_repo_group_name
```