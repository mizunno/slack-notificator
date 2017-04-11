#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mizunno
"""

import os
from slackclient import SlackClient

sc = SlackClient("YOUR_SLACK_TOKEN")

#==============================================================================
# The function 'find_all_files(files)' find all files in a directory and 
# subdirectories recursively. Given a empty dict called 'files' (or whatever) 
# return it matching ctime (in seconds) and the file.
#==============================================================================

def find_all_files(files):
    for element in os.listdir():
        if os.path.isdir(element):
            os.chdir(element)
            find_all_files(files)
            os.chdir("..")
        else:
            files[os.path.getctime(element)]=element

#==============================================================================
# The function 'find_newest_file(files)' return the last element added in root 
# directory (where the script is launched).
#==============================================================================

def find_newest_file(files):
    return files[max(files)]

#==============================================================================
# Send a message given as a parameter to books channel.
#==============================================================================

def send_message(message):
    sc.api_call("chat.postMessage",
                channel="#books",
                username="booksbot",
                text=message)
    
files = dict()
find_all_files(files)
send_message("Añadido *"+find_newest_file(files)+"*")