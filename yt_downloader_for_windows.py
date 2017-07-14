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
import os
import pafy
import re
from string import punctuation
from bs4 import BeautifulSoup as bs
from urllib2 import urlopen

#==============================================================================
# ENTER THE URL FOR THE PLAYLIST HERE
#==============================================================================
print("Pro Tip: To paste press Alt + Space, then select Paste from the Edit menu.\n")
PLAYLIST_URL = str(raw_input("Paste the playlist URL: "))

#==============================================================================
# ENTER THE LOCATION FOR WHERE YOU WANT THE DOWNLOADED FILES TO BE PLACED
#==============================================================================
print("\nAll downloaded files will be placed in the Downloaded Music folder in this directory.")
FOLDER_LOCATION = "./Downloaded Music/"

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
    # Sanitize string literal
    if isinstance(titles[i],unicode):
        replacement_title = titles[i].encode('ascii','ignore')
    elif isinstance(titles[i],str):
        replacement_title = titles[i]
    # Remove brackets and contents
    replacement_title = re.sub(re.compile(r'\([^()]*\)'), '', replacement_title)
    replacement_title = re.sub(re.compile(r'\[^]*\)'), '', replacement_title)
    # Remove trailing and multiple spaces
    replacement_title = re.sub(re.compile(r'\s+$'), '', replacement_title)
    replacement_title = re.sub(re.compile(r'\s\s+'), '', replacement_title)
    # Remove punctuation except dashes
    replacement_title = re.sub(re.compile(r'\p{P}(?<!-)'), '', replacement_title)
    replacement_title = re.sub(re.compile(r'\|'), '', replacement_title)
    replacement_title = replacement_title.strip(punctuation)

    print(str("Now downloading: "+str(replacement_title)))

    # Check if file already exists
    all_files = os.listdir(FOLDER_LOCATION)
    if str(replacement_title+".m4a") in all_files:
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
    FILE_LOCATION = str(FOLDER_LOCATION + replacement_title + ".m4a")
    audio.download(FILE_LOCATION)

