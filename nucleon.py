#!/usr/bin/env python3
# @Author: George Onoufriou <GeorgeRaven>
# @Date:   2018-05-16
# @Project: RavenNucleon
# @Filename: nucleon.py
# @Last modified by:   georgeraven
# @Last modified time: 2018-05-29
# @License: Please see LICENSE file in project root



import os, sys, json, inspect
from src.helpers import argz, logger, installer, updater
from src.log import Log

def main():
    None

# declaring usefull global variables
home = os.path.expanduser("~")
name = os.path.basename(sys.argv[0])

fileAndPath = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(fileAndPath))

prePend = "[ " + name + " ] "
description = name + "; " + "Python script entry point for RavenNucleon\
 so that archlinux may reign supreme on whatever you choose for Nucleon\
to install it on."

# capture arguments in dict then put into json for bash
args = argz(sys.argv[1:], description=description)
args_json = json.loads(json.dumps(args))

# setting up fallback logger
log = Log(logLevel=args["loglevel"])
print = log.print

# installing, updating, upgrading
installer(path=path)
updater(path=path)

# if level3 (debug) prepare for some verbose shnitzel
if(args["loglevel"] >= 3):
    main()
else:
    try:
        main()
        # raise ValueError('A very specific bad thing happened.')

    except:
        print(str(sys.exc_info()[0]) + " " + str(sys.exc_info()[1]), 2)
