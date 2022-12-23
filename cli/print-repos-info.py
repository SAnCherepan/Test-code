from src.repo_reader_sancherepan.repo_reader import RepoReader
import sys


def main(auth_token, org_name):
    reader = RepoReader(auth_token)
    repos = reader.read_repos(org_name)

    for repo in repos:
        print(f"repo: {repo.name}, "
              f"size: {repo.size}, "
              f"open_issues: {repo.open_issues_count}, "
              f"branches: {len(repo.branches)}\n")

    print()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: print-repos-info.py <github_auth_token> <github_org_name>")
    else:
        main(auth_token=sys.argv[1],
             org_name=sys.argv[2])
