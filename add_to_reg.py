from os import getcwd
from sys import executable as python_exe
from winreg import CreateKey, SetValue, SetValueEx, HKEY_CLASSES_ROOT, REG_SZ

# Getting the path of current working directory.
cwd = getcwd()

# Setting the path of the context menu (right-click menu).
key_path = 'Directory\\Background\\shell\\AutoGitClone\\'

# Creating outer key.
outer_key = CreateKey(HKEY_CLASSES_ROOT, key_path)
SetValue(outer_key, '', REG_SZ, '&Git Clone Here')

# Creating icon value.
icon_path = f'{cwd}\\git.ico'
SetValueEx(outer_key, 'Icon', 0, REG_SZ, icon_path)

# Creating inner key.
inner_key = CreateKey(outer_key, 'command')
SetValue(inner_key, '', REG_SZ, f'{python_exe} "{cwd}\\cloner.py"')

print('\n-> Command successfully added to Windows context menu!')
