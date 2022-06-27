from os import system
from pyperclip import paste

# Getting the content of the user clipboard.
repo_clone_url = paste()

if len(repo_clone_url) > 0:
    # Running the git clone command.
    system(f'git clone "{repo_clone_url}"')
