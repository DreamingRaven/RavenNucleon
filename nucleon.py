# @Author: George Onoufriou <GeorgeRaven>
# @Date:   2018-05-16
# @Project: RavenNucleon
# @Filename: nucleon.py
# @Last modified by:   georgeraven
# @Last modified time: 2018-05-28
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

# capture arguments in dict
args = argz(sys.argv[1:], description=description)
# create json version of dict to pass to bash
args_json = json.loads(json.dumps(args))

# setting up fallback logger
log = Log(logLevel=args["loglevel"])
print = log.print # overiding default print with fallback logger

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
        log.print(str(sys.exc_info()[0]) + " " + str(sys.exc_info()[1]), 2)
