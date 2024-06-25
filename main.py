from sys import argv
from simple_term_menu import TerminalMenu
from gitparser import Repo

def checkout():
    branches = Repo().branches()
    current_branch = Repo().current_branch()
    print(f"Current branch: {current_branch}")
    if not branches:
        print("No branches found!")
        return

    terminal_menu = TerminalMenu(branches, show_search_hint=True)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {branches[menu_entry_index]}!")
    Repo().checkout(branches[menu_entry_index])
    

def fetch():
    Repo().fetch()


def add():
    entries = Repo().entries()
    added = entries["added"]
    not_added = entries["not_added"]
    
    for key in added.keys():
        title = key
        entries2 = added[key] + not_added[key]
        if not entries2: continue

        terminal_menu = TerminalMenu(entries2,
                                 preselected_entries=added[key],
                                 multi_select=True,
                                 show_multi_select_hint=True,
                                 show_search_hint=True,
                                 title=title)
        menu_entry_indeces = terminal_menu.show()
        if not menu_entry_indeces:
            continue
        
        # selected_entries = [entries2[i] for i in menu_entry_indeces]


def main():
    commands = {
        "checkout": checkout,
        "fetch": fetch,
        "add": add,
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