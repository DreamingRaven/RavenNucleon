#!/usr/bin/env python3
# @Author: George Onoufriou <GeorgeRaven>
# @Date:   2018-05-16
# @Project: RavenNucleon
# @Filename: nucleon.py
# @Last modified by:   georgeraven
# @Last modified time: 2018-05-31
# @License: Please see LICENSE file in project root



import os, sys, json, inspect
from src.helpers import argz, logger, installer, updater, isBlockDevice
from src.log import Log



def main():

    print("Init success, hello world!", 3)

    print(prePend + " checking if: " + args["device"] + " exists", -1)
    isBlock = isBlockDevice(args["device"])
    if(isBlock):
        if(args["image"] != "") and (args[""]):
            None
    else:
        print("'" + args["device"] + "' is not a valid device, check if it exists", 2)
        print("could not find: " + args["device"], -1)

# declaring usefull global variables
home = os.path.expanduser("~")
name = os.path.basename(sys.argv[0])

fileAndPath = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(fileAndPath))

prePend = "[ " + name + " ] "
description = name + "; " + "Python script entry point for RavenNucleon\
 so that archlinux may reign supreme on whatever you choose for Nucleon\
to install it on."

dependancies = ["https://github.com/DreamingRaven/RavenPythonLib"]

# capture arguments in dict then put into json for bash
args = argz(sys.argv[1:], description=description)
args_json = json.loads(json.dumps(args))

# setting fallback logger here pre-update
log = Log(logLevel=args["loglevel"])
print = log.print

# attempting update/ falling back
try: # TODO: devise a method to make erros in nested try, catch
    from RavenPythonLib.updaters.gitUpdate import Gupdater
    nucleon = Gupdater(path=path, urls=dependancies)
    nucleon.install()
    nucleon.update()

except:
    print("Gupdater failed, falling back: " + str(sys.exc_info()[1]), 1)
    installer(path=path, urls=dependancies)
    updater(path=path, urls=dependancies)

# attempting set logger from external lib/ falling back
try:
    from RavenPythonLib.loggers.basicLog import Log
    log = Log(logLevel=args["loglevel"])
    print = log.print # note no '()' as function address desired not itself
except:
    log = Log(logLevel=args["loglevel"])
    print = log.print
    print("Main logger could not be loaded, falling back: " +
        str(sys.exc_info()[1]), 1)

# if level3 (debug) prepare for some verbose shnitzel
if(args["loglevel"] >= 3):
    main()
else:
    try:
        main()
        # raise ValueError('A very specific bad thing happened.')

    except:
        print(str(sys.exc_info()[0]) + " " + str(sys.exc_info()[1]), 2)
