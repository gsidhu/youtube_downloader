# -*- coding: utf-8 -*-
'''
YouTube Playlist Downloader
Gurjot Sidhu, July 2017
MIT License

Requirements: Python 3.x, pafy, youtube-dl, bs4, lxml

Provide the URL for a YouTube playlist and the script will download all the
songs in the playlist (up to 100; will add a fix soon) to your local drive.

The file format is .m4a which should work with iTunes.

I recommend using EasyTAG to add ID3 tags to your files.
'''

import os
import pafy
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

#==============================================================================
# ENTER THE URL FOR THE PLAYLIST HERE
#==============================================================================
#PLAYLIST_URL = "https://www.youtube.com/playlist?list=PL2140A0411C65DD13"
PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLxKHVMqMZqUQknyKcYbQaRfXvZXPR5VJ2"
#PLAYLIST_URL = "https://www.youtube.com/watch?v=JGwWNGJdvx8&list=RDQMgEzdN5RuCXE"

#==============================================================================
# ENTER THE LOCATION FOR WHERE YOU WANT THE DOWNLOADED FILES TO BE PLACED
#==============================================================================
#FOLDER_LOCATION = "/home/gurjot/Music/Songs_of_A_Mad_Man/"
FOLDER_LOCATION = "/home/gurjot/Music/"

#==============================================================================
# IGNORE EVERYTHING FOLLOWING THIS
#==============================================================================
playlist = urlopen(PLAYLIST_URL)
content = playlist.read()
soup = bs(content,"lxml")
titles = []
ids = []

#For standard playlists
if "?list" in PLAYLIST_URL:
	sources = soup.find_all('tr',{"data-video-id":True})
	for source in sources:
		titles.append(source['data-title'])
		ids.append(source['data-video-id'])
#For YouTube Mix playlists
elif "&list" in PLAYLIST_URL:
	sources = soup.find_all('li',{"data-video-id":True})
	for source in sources:
		titles.append(source['data-video-title'])
		ids.append(source['data-video-id'])

for i in range(len(ids)):
    print("Now downloading: ", titles[i])
    # Check if file already exists
    all_files = os.listdir(FOLDER_LOCATION)
    if str(titles[i]+".m4a") in all_files:
        print("This file already exists in the downloads folder. Skipping it.\n")
        continue
    
    video_url = str("https://www.youtube.com/watch?v="+ids[i])
    
    # Check if video is available
    try:
        video = pafy.new(video_url)
    except IOError:
        print("This video is not available. Skipping it.\n")
        continue
    
    # Fetch audio
    audio = video.getbestaudio(preftype="m4a")
    audio.download(FOLDER_LOCATION)
