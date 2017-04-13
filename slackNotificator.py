#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import slackweb

sc = slackweb.Slack("YOUR_SLACK_WEBHOOK_URL")

#==============================================================================
# The function 'find_all_files(files)' finds all the files in a directory and
# subdirectories recursively. Given a empty dict called 'files'.
# The function saves the file in the position of its ctime (in seconds).
# Code by Mizunno
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
# The function 'find_newest_file(files)' returns the last element added in root
# directory (where the script is launched).
# Code by Mizunno
#==============================================================================

def find_newest_file(files):
    return files[max(files)]

#==============================================================================
# Send a message given as a parameter to the webHook. It will then post it to
# its default channel as defined in the Slack integration.
# If it's considered necessary, its possible to add a channel="", username=""
# and icon_emoji="" parameters, but as stated before this info is already
# configured in the slack integration settings.
#==============================================================================

def send_message(message):
    sc.notify(text=message)


files = dict()
find_all_files(files)
send_message("Se ha añadido el archivo *"+find_newest_file(files)+"* a la carpeta compartida")