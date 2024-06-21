#!/usr/bin/env python3

from simple_term_menu import TerminalMenu
from gitparser import Repo
def main():
    repo = Repo()
    # repo.fetch()
    branches = repo.branches()
    terminal_menu = TerminalMenu(branches)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {branches[menu_entry_index]}!")
    repo.checkout(branches[menu_entry_index])

if __name__ == "__main__":
    main()