# @Author: George Onoufriou <GeorgeRaven>
# @Date:   2018-05-16
# @Project: RavenNucleon
# @Filename: nucleon.py
# @Last modified by:   GeorgeRaven
# @Last modified time: 2018-05-16
# @License: Please see LICENSE file in project root



import os, sys, json
from src import helpers

# this file serves as the RavenNucleon entry point

args = helpers.argz(sys.argv[1:])
print(json.loads(json.dumps(args)))
