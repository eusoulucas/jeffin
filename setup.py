import sys
from cx_Freeze import setup, Executable
from tkinter import *
import os

os.environ["TCL_LIBRARY"] = "C:\\Users\\lucad\\AppData\\Local\\Programs\\Python\\Python38-32\\tcl\\tcl8.6"
os.environ["Tk_LIBRARY"] = "C:\\Users\\lucad\\AppData\\Local\\Programs\\Python\\Python38-32\\tcl\\tk8.6"

base = None

if sys.platform == "win32":
    base = "Win32GUI"

executable = [Executable("main.py", base = base)]
packages = ["tkinter", "selenium","selenium.webdriver.common.keys","itertools","explicit",
            "bot","time", "random", "datetime", "random", "idna", "six", "ordered_set", "html.parser",
            "packaging.version", "packaging","pkg_resources.py2_warn", "pkg_resources.extern", "setuptools.msvc"]

options = {
    "build_exe":
    {
        "packages": packages,
        "include_files":
        [
            os.path.join("C:\\Users\\lucad\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs\\tcl86t.dll"),
            os.path.join("C:\\Users\\lucad\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs\\tk86t.dll"),
        ]
    },
}

setup(  name = "Jeffin",
        options = options,
        version = "2.0",
        description = "Bot de comentarios do instagram",
        executables = executable
        )
