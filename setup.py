import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": [], "excludes": []}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

target = Executable(
    script="theacrine.py",
    base="Win32GUI",
    icon="icons/default_16.ico"
    )

setup(
    name="theacrine_1.2",
    version="1.2",
    description="GUI for Theacrine app!",
    options={"build_exe": build_exe_options},
    executables=[target]
)