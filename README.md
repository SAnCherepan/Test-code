# Repo reader

This is a simple example package that can be used to get basic info on GitHub repository groups (a.k.a. organisations).

# Installation

Install the python package:
```
python -m pip install --index-url https://test.pypi.org/simple/ repo_reader_sancherepan
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
