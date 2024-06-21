from sys import argv
from simple_term_menu import TerminalMenu
from gitparser import Repo

def checkout():
    repo = Repo()
    branches = repo.branches()
    terminal_menu = TerminalMenu(branches)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {branches[menu_entry_index]}!")
    repo.checkout(branches[menu_entry_index])
    

def main():
    commands = {
        "checkout": checkout,
    }

    command = argv[1]
    func = commands.get(command)
    if not func:
        print(f"Unknown command: {command}")
        return
    
    func()


if __name__ == "__main__":
    main()