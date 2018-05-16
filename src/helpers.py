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

    # creating argument groups
    optional = parser._action_groups.pop() # popping -h off
    required = parser.add_argument_group('required arguments')


    # creating arguments in required group
    required.add_argument("-d", "--device",       default="", required=True,
        help="device name to install archlinux on e.g: \'/dev/sdd\' or \
         '/dev/sdd1' for a specific partition")

    # creating arguments in optional group
    optional.add_argument("-v", "--verbose",      default=0, type=int,
        help="sets verbosity level; how much information is displayed")
    optional.add_argument("--noconfirm", default=False, action="store_true",
        help="for those that live life on the... ledge")

    parser._action_groups.append(optional) # pushing -h back on with extras
    return vars(parser.parse_args(argv))

def log(message, status=0):
    if(status==-1):
        None # only for the cool dudes
    elif(status==0):
        print(prePend, " [ info ]", message)
    elif(status==1):
        print(prePend, " [ warn ]", message)
    elif(status==2):
        print(prePend, " [ error ]", message)
    elif(status==3):
        print(prePend, " [ debug ]", message)
