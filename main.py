from sys import argv
from simple_term_menu import TerminalMenu
from gitparser import Repo

def checkout():
    repo = Repo()
    branches = repo.branches()
    current_branch = repo.current_branch()
    print(f"Current branch: {current_branch}")
    if not branches:
        print("No branches found!")
        return
    terminal_menu = TerminalMenu(branches)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {branches[menu_entry_index]}!")
    repo.checkout(branches[menu_entry_index])
    

def fetch():
    repo = Repo()
    repo.fetch()


def main():
    commands = {
        "checkout": checkout,
        "fetch": fetch,
    }
    
    if len(argv) < 2:
        print("Usage: main.py <command>")
        print("Available commands:")
        print("\n".join(commands.keys()))
        return
    command = argv[1]
    func = commands.get(command)
    if not func:
        print(f"Unknown command: {command}")
        return
    
    func()


if __name__ == "__main__":
    main()