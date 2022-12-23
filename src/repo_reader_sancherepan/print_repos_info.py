import sys
import argparse
from .repo_reader import RepoReader


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('auth_token', help='<your_github_auth_token>')
    parser.add_argument('org_name', help="<github_repo_group_name>")

    if args is None:
        args = sys.argv[1:]

    args = parser.parse_args(args)
    auth_token = args.auth_token
    org_name = args.org_name

    reader = RepoReader(auth_token)
    repos = reader.read_repos(org_name)

    for repo in repos:
        print(f"repo: {repo.name}, "
              f"size: {repo.size}, "
              f"open_issues: {repo.open_issues_count}, "
              f"branches: {len(repo.branches)}\n")


if __name__ == '__main__':
    sys.exit(main(sys.argv))
