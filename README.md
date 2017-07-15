YouTube Playlist Downloader
======

**Features:**
* Works for ALL types of YouTube playlists (standard, Mix, Liked etc.)
* Super quiet, almost no error reporting

**Requirements:** Python 2.x, pafy, youtube-dl, ffmpeg

```
pip install pafy youtube-dl ffmpeg
```

Instructions for Windows
------
1. Extract the `YouTube Downloader for Windows` folder by downloading the ZIP using the green-coloured 'Clone or download' button on the top right.
2. Run the `yt_downloader_for_windows.exe` file.
3. Type in the playlist ID and press Enter.
4. Press Enter if you want '.m4a'/'.aac' (iTunes supported) format. Press any other key for '.mp3' format.
5. All the tracks will be downloaded to the "Downloaded Music" folder.
6. Enjoy your piracy.

Instructions for Python (all OS)
------
1. Edit the `yt_downloader.py` file with the playlist URL and folder location of your desire.
2. Change the `FORMAT_MP3' variable to 1 if you want the files to be in '.mp3' format.
3. Run the script.
4. Rejoice in your piracy.

The default file format is '.m4a' which should work seamlessly with iTunes. In case of trouble, the program tries to download a '.mp3' version instead. You can choose to always download '.mp3' versions if that's your thing.

I recommend using [EasyTAG](https://wiki.gnome.org/Apps/EasyTAG) to add ID3 tags to your files.

**Frequently Asked Questions (FAQ)**  
*I get an `ffmpeg` error. What do I do?*  
Go to [this website](https://www.ffmpeg.org/download.html) and install ffmpeg.

*Does this work with Python 3?*  
Well, yeah it kinda does. There's a small problem with the regex and encoding that I need to fix.

*I have other questions. What do I do?*  
Open an issue.

**Copyright**  
This shit's free, man. Do what you want with it.
