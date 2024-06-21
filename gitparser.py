from singleton import singleton
import subprocess

silent = subprocess.DEVNULL
save = subprocess.PIPE

@singleton
class Repo:
    def __init__(self, repo_path: str = "."):
        result = subprocess.run(
            ["git", "config", "user.email"],
            stdout=save,
            text=True,
            check=True
        )
        self.email = result.stdout.strip()


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
        

    def branches(self):
        result = subprocess.run(
            ['git', 'for-each-ref', '--sort=-committerdate', '--format=%(committerdate:iso8601) mail:%(authoremail) %(refname:short)', 'refs/heads/'],
            stdout=save, 
            text=True, 
            check=True
        )
        output = result.stdout
        branches = output.split("\n")
        branches = [b for b in branches if b]
        my_branches = [b for b in branches if self.email in b.split("mail:")[1].split(" ")[0]]
        my_branches = sorted(my_branches)
        
        names = [b.split(" ")[-1] for b in my_branches]
        # print(names)
        return names