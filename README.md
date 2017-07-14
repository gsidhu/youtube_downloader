YouTube Playlist Downloader
======

**Features:** 
* Works for standard YouTube playlists
* [DONE] Works for YouTube Mix playlists
* [DONE] Checks if video is unavailable or if file already exists in the downloads directory
* [TODO] ???

**Requirements:** Python 3.x/2.x, pafy, bs4, youtube-dl, lxml

```
pip install pafy bs4 youtube-dl lxml
```

Instructions for Windows
------
1. Extract the `yt_downloader for Windows` folder by downloading the ZIP using the green-coloured 'Clone or download' button on the top right.
2. Run the `yt_downloader_2_x.exe` file.
3. Type in the playlist ID and press Enter.
4. All the tracks will be downloaded to the "Downloaded Music" folder.
5. Enjoy your piracy.

Instructions for Python (all OS)
------
1. Edit the `yt_downloader.py` file with the playlist URL and folder location of your desire.
2. Run the file.
3. Rejoice in your piracy.

The file format is .m4a which should work seamlessly with iTunes. Currently there is a limit of 100 tracks, I will push a fix for it soon/whenever I get the time.

I recommend using [EasyTAG](https://wiki.gnome.org/Apps/EasyTAG) to add ID3 tags to your files.

**Note:** Use the `yt_downloader_2_x.py` file if you are running Python 2.x. For Python 3.x, use `yt_downloader.py`.
