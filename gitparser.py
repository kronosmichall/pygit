import git
from singleton import singleton

@singleton
class Repo:
    def __init__(self, repo_path: str = "."):
        self.repo = git.Repo(repo_path)
        if not self.repo:
            raise Exception("Repo not found.")
        
    def fetch(self):
        print("Fetching all remotes...")
        self.repo.git.fetch("--all")
