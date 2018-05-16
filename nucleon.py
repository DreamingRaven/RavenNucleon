# @Author: George Onoufriou <GeorgeRaven>
# @Date:   2018-05-16
# @Project: RavenNucleon
# @Filename: nucleon.py
# @Last modified by:   GeorgeRaven
# @Last modified time: 2018-05-16
# @License: Please see LICENSE file in project root



import os, sys, json
from src.helpers import argz
from src.log import Log

# declaring usefull global variables
home = os.path.expanduser("~")
name = os.path.basename(sys.argv[0])
prePend = "[ " + name + " ] "
description = name + "; " + "Python script entry point for RavenNucleon\
 so that archlinux may reign supreme on whatever you choose for Nucleon\
to install it on."
# log = helpers.log()

# capture arguments in dict
args = argz(sys.argv[1:], description=description)
# create json version of dict to pass to bash
args_json = json.loads(json.dumps(args))

# helpers.log(args_json, status=0)
