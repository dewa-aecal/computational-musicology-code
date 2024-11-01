# -*- coding: utf-8 -*-
"""
@author: Dewa Ardiana
This code is used to get metadata of MP3 files inside a specific folder.
"""

from tinytag import TinyTag
import os


def load_mp3(path):
    #list all file in the folder
    files=os.listdir(path)
    #filter file that end with mp3
    mp3_files=[file for file in files if file.endswith('.mp3')]
    
    for mp3_file in mp3_files:
        #create full path that combining folder path and filename
        file_path=os.path.join(path, mp3_file)
        #extract metadata from file
        tag=TinyTag.get(file_path)
        #convert duration to minutes. By default tag.duration give seconds
        duration_minutes=tag.duration/60
        #print title, artist, and duration
        print(f"Title: {tag.title}, Artist: {tag.artist}, Duration: {duration_minutes:.2f} minutes")

#set path folder that contain mp3 files
path='music'

load_mp3(path)
    