from functools import cache
from text import *
import subprocess

silent = subprocess.DEVNULL
save = subprocess.PIPE

@cache
class Repo:
    def __init__(self, repo_path: str = "."):
        result = subprocess.run(
            ["git", "config", "user.email"],
            stdout=save,
            text=True,
            check=True
        )
        self.email = result.stdout.strip()


    def current_branch(self):
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            stdout=save,
            text=True,
            check=True
        )
        return result.stdout.strip()
        

    def fetch(self):
        print("Fetching all remotes...")
        subprocess.run(
            ["git", "fetch", "--all"], 
            stdout=silent, 
            check=True
        )
        

    def checkout(self, branch: str):
        subprocess.run(
            ["git", "checkout", branch],
            check=True
        )
        subprocess.Popen(
            ["git", "pull"],
            stdout=silent,
            stderr=silent
        )
        

    def branches(self):
        result = subprocess.run(
            ['git', 'for-each-ref', '--sort=-committerdate', '--format=%(committerdate:iso8601) mail:%(authoremail) %(refname:short)', 'refs/remotes/', 'refs/heads'],
            stdout=save, 
            text=True, 
            check=True
        )
        output = result.stdout
        branches = output.split("\n")
        branches = [b for b in branches if b]

        my_branches = [b for b in branches if self.email in b.split("mail:")[1].split(" ")[0]]
        names = [b.split(" ")[-1] for b in my_branches]
        names = [n for n in names if n != "master"]
        names = [get_suffix(n, "origin/") or n for n in names]
        names = remove_duplicates(names)

        current = self.current_branch()
        if current in names:
            names.remove(current)
            names.insert(0, current)

        return names
    
    def entries(self):
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            stdout=save,
            text=True,
            check=True
        )
        
        output = result.stdout
        entries = output.split("\n")
        
        result = {}
        result["added"] = {
            "new": [get_suffix(e, "A") for e in entries if get_suffix(e, "A")],
            "modified": [get_suffix(e, "M") for e in entries if get_suffix(e, "M")],
            "deleted": [get_suffix(e, "D") for e in entries if get_suffix(e, "D")]
        }
        result["not_added"] = {
            "new": [get_suffix(e, "??") for e in entries if get_suffix(e, "??")],
            "modified": [get_suffix(e, " M") for e in entries if get_suffix(e, " M")],
            "deleted": [get_suffix(e, " D") for e in entries if get_suffix(e, " D")]
        }
        return result