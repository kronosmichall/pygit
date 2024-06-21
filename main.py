import argparse
from gitparser import *

def main(repo_path: str):
    # repo = git.Repo(repo_path)
    # print(repo.remotes.origin.url)
    print("xd")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple CLI for git operations.")
    parser.add_argument("--repo_path", type=str, default='.', help="Path to the git repository.")

    args = parser.parse_args()

    main(args.repo_path)