# @Author: George Onoufriou <GeorgeRaven>
# @Date:   2018-05-16
# @Project: RavenNucleon
# @Filename: helpers.py
# @Last modified by:   GeorgeRaven
# @Last modified time: 2018-05-16
# @License: Please see LICENSE file in project root



import argparse
import os, sys
home = os.path.expanduser("~")
name = os.path.basename(sys.argv[0])
prePend = "[ " + name + " ] "

def argz(argv=None, description=None):

    if(description == None):
        description = "RavenNucleon"

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("-d", "--device",       default="", required=True,
        help="device name to install archlinux on e.g: \'/dev/sdd\'")
    parser.add_argument("-v", "--verbose",      default=0, type=int,
        help="sets verbosity level; how much information is displayed")
    parser.add_argument("--noconfirm", default=False, action="store_true",
        help="for those that live life on the... ledge")

    return vars(parser.parse_args(argv))
