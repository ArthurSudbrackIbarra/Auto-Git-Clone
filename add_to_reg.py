from os import getcwd
from sys import executable as python_exe
from winreg import CreateKey, HKEY_CLASSES_ROOT, REG_EXPAND_SZ, SetValue, REG_SZ

# Getting the path of current working directory.
cwd = getcwd()

# Setting the path of the context menu (right-click menu).
key_path = r'Directory\\Background\\shell\\AutoGitClone\\'

# Creating outer key.
outer_key = CreateKey(HKEY_CLASSES_ROOT, key_path)
SetValue(outer_key, '', REG_SZ, '&-> Git Clone Here <-')

# Creating inner key.
inner_key = CreateKey(outer_key, r"command")
SetValue(inner_key, '', REG_SZ, f'{python_exe} "{cwd}\\cloner.py"')

print("\n-> Command successfully added to Windows context menu!")
