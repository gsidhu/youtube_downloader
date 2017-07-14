import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["bs4","urllib2","pafy","lxml","os","string","re"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
##if sys.platform == "win32":
##    base = "Win32GUI"

setup(  name = "YouTube Playlist Downloader",
        version = "0.1.1",
        description = "Download audio tracks from YouTube playlists",
        options = {"build_exe": build_exe_options},
executables = [Executable("yt_downloader_for_windows.py", base=base)])
