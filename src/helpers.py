import argparse
import os, sys
home = os.path.expanduser("~")
name = os.path.basename(sys.argv[0])
prePend = "[ " + name + " ] "

def argz(argv=None, description=None):

    if(description == None):
        description = "Nucleon"

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("-C", "--coll",     default="testColl",
        help="")
    parser.add_argument("--intuitivePlots", default=0, type=int,
        help="")

    return vars(parser.parse_args(argv))
