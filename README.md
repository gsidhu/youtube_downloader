##YouTube Playlist Downloader

**Requirements:** Python 3.x/2.x, pafy, bs4, youtube-dl

```
pip install pafy bs4 youtube-dl
```

Provide the URL for a YouTube playlist and the script will download all the songs in the playlist (up to 100 files only; will add a fix soon) to your local drive (into a folder you specify).

The file format is .m4a which should work with iTunes.

I recommend using [EasyTAG](https://wiki.gnome.org/Apps/EasyTAG) to add ID3 tags to your files.

*Note: Use the yt_downloader_2_x.py file if you are running Python 2.x. For Python 3.x, use yt_downloader.py.*
