# -*- coding: utf-8 -*-
'''
YouTube Playlist Downloader
Gurjot Sidhu, 2017
MIT License

Requirements: Python 2.x, pafy, bs4, youtube-dl

Provide the URL for a YouTube playlist and the script will download all the
songs in the playlist (up to 100; will add a fix soon) to your local drive.

The file format is .m4a which should work with iTunes.

I recommend using EasyTAG to add ID3 tags to your files.
'''

from __future__ import print_function
import pafy
from bs4 import BeautifulSoup as bs
from urllib2 import urlopen

#==============================================================================
# ENTER THE URL FOR THE PLAYLIST HERE
#==============================================================================
PLAYLIST_URL = "https://www.youtube.com/playlist?list=PL2140A0411C65DD13"

#==============================================================================
# ENTER THE LOCATION FOR WHERE YOU WANT THE DOWNLOADED FILES TO BE PLACED
#==============================================================================
FOLDER_LOCATION = "/home/gurjot/Music/Songs_of_A_Mad_Man/"

#==============================================================================
# IGNORE EVERYTHING FOLLOWING THIS
#==============================================================================
playlist_url = urlopen(PLAYLIST_URL)
content = playlist_url.read()
soup = bs(content,"lxml")
titles = []
ids = []

sources = soup.find_all('tr',{"data-title":True})
for source in sources:
	titles.append(source['data-title'])
	ids.append(source['data-video-id'])

for i in range(len(ids)):
    print("Now downloading: ", titles[i])
    video_url = str("https://www.youtube.com/watch?v="+ids[i])
    video = pafy.new(video_url)
    audio = video.getbestaudio(preftype="m4a")
    audio.download(FOLDER_LOCATION)