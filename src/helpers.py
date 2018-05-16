import argparse
import os, sys
home = os.path.expanduser("~")
name = os.path.basename(sys.argv[0])
prePend = "[ " + name + " ] "

def argz(argv=None, description=None):

    if(description == None):
        description = "Nucleon"

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("-d", "--device",     default="",
        help="device name to install archlinux on")
    parser.add_argument("--noconfirm", default=False, action="store_true",
        help="for those that live life on the... ledge.")

    return vars(parser.parse_args(argv))
