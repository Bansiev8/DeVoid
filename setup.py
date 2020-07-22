import cx_Freeze
#from cx_Freeze import setup, Executable
import sys
import os
base = None


if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\WELCOME\AppData\Local\Programs\Python\Python37\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\WELCOME\AppData\Local\Programs\Python\Python37\tcl\tk8.6"

executables = [cx_Freeze.Executable("devoid.py", base=base, icon="icon.ico")]


cx_Freeze.setup(name = "DeVoid",
      options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icon.ico",'tcl86t.dll','tk86t.dll', 'usingic']}},
      version = "0.01",
      description = "It DeVoids your CODE",
      executables = executables)
