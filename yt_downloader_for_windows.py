# -*- coding: utf-8 -*-
'''
YouTube Playlist Downloader
Gurjot Sidhu, 2017
MIT License

Requirements: Python 2.7+/3.x, pafy, bs4, youtube-dl

Provide the URL for a YouTube playlist and the script will download all the
songs in the playlist (up to 100; will add a fix soon) to your local drive.

The file format is .m4a which should work with iTunes.

I recommend using EasyTAG to add ID3 tags to your files.
'''

from __future__ import print_function
from __future__ import unicode_literals
import os
import pafy
import re
import subprocess
import youtube_dl
from string import punctuation

#==============================================================================
# ENTER THE URL FOR THE PLAYLIST HERE
#==============================================================================
print("Pro Tip: To paste press Alt + Space, then select Paste from the Edit menu.\n")
PLAYLIST_URL = str(raw_input("Enter the playlist URL: "))

#==============================================================================
# If you want an MP3 file change the 0 below to 1 (default format is .m4a)
#==============================================================================
print("\nThe default file format is .m4a/.aac (the iTunes one). But there is also an option to download MP3 files.\n")
FORMAT_CHOICE = raw_input("Do you want to download MP3 files? (y/n) ")
if str(FORMAT_CHOICE).lower() == 'y':
    FORMAT_MP3 = True
    print("Cool. Downloading MP3 files then.\n")
else:
    FORMAT_MP3 = False
    print("Cool. Downloading m4a/AAC files then.\n")
    
#==============================================================================
# ENTER THE LOCATION FOR WHERE YOU WANT THE DOWNLOADED FILES TO BE PLACED
#==============================================================================
print("All downloaded files will be placed in the Downloaded Music folder in this directory.\n")
FOLDER_LOCATION = "./Downloaded Music/"

#==============================================================================
# IGNORE EVERYTHING FOLLOWING THIS
#==============================================================================
playlist_json = pafy.get_playlist(PLAYLIST_URL)
titles = []
ids = []

for item in range(len(playlist_json['items'])):
    titles.append(playlist_json['items'][item]['playlist_meta']['title'].encode('ascii','ignore'))
    ids.append(playlist_json['items'][item]['playlist_meta']['encrypted_id'].encode('ascii','ignore'))

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        pass
        
def get_filename(input_title):
    # Sanitize string literal
    if isinstance(input_title,unicode):
        replacement_title = input_title.encode('ascii','ignore')
    elif isinstance(input_title,str):
        replacement_title = input_title
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
    return str(replacement_title)

def check_existence(title):
    all_files = os.listdir(FOLDER_LOCATION)
    if str(title+".m4a") in all_files or str(title+'.mp3') in all_files:
        return True
    else:
        return False

def get_m4a(title, video_id):
    video_url = str("https://www.youtube.com/watch?v="+video_id)
    # Check if video is available
    try:
        video = pafy.new(video_url)
#    except IOError:
#        print("Nope. Looks like this video is unavailable. Skipping it.\n")
#        return False
    except:
        print("There seems to be a problem with this video. Trying to download mp3 version instead.\n")
        try:
            get_mp3(title, video_id)
            return True
        except:
            print("Nope. Looks like this video is unavailable. Skipping it.\n")
            return False
    # Fetch audio
    audio = video.getbestaudio(preftype="m4a")
    FILE_LOCATION = str(FOLDER_LOCATION + title + ".m4a")
    audio.download(FILE_LOCATION)

def get_mp3(title, video_id):
    video_url = str("https://www.youtube.com/watch?v="+video_id)
    ydl_opts = {
        'format': 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'ignoreerrors': True,
        'logger': MyLogger(),
        'outtmpl': str(FOLDER_LOCATION + title + '.%(ext)s')
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
    except:
        subprocess.call(str('''youtube-dl -i --quiet --extract-audio --audio-format mp3 -o "''' + FOLDER_LOCATION + title + '.%(ext)s" ' + video_url), shell=True)

#==============================================================================
# Download the shit
#==============================================================================
for i in range(len(ids)):
    replacement_title = get_filename(titles[i])
    print(str("Now downloading: "+replacement_title))

    # Check if file already exists
    if check_existence(replacement_title):
        print("This file already exists in the downloads folder. Skipping it.\n")
        continue

    if FORMAT_MP3:
        get_mp3(replacement_title, ids[i])
    else:
        get_m4a(replacement_title, ids[i])

print("\nBoom. Done. Rejoice in your piracy now.")
