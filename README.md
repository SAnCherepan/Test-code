# Repo reader

This is a simple example package that can be used to get basic info on GitHub repository groups (a.k.a. orgs).

# Installation

Install the python package:
```
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps repo_reader_sancherepan
```


# Usage

In your code:
```python
from repo_reader_sancherepan.repo_reader import RepoReader

reader = RepoReader("<your_github_auth_token>")
repos = reader.read_repos("<github_repo_group_name>")
```

See also an [example using CLI](cli/print-repos-info.py)
