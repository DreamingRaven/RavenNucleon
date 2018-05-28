# @Author: George Onoufriou <GeorgeRaven>
# @Date:   2018-05-16
# @Project: RavenNucleon
# @Filename: helpers.py
# @Last modified by:   georgeraven
# @Last modified time: 2018-05-28
# @License: Please see LICENSE file in project root



import argparse
import os, sys
home = os.path.expanduser("~")
name = os.path.basename(sys.argv[0])
prePend = "[ " + name + " ] "

# project specific arguments
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
    optional.add_argument("-l", "--loglevel",      default=0, type=int,
        help="sets verbosity level; how much information is displayed")
    optional.add_argument("--noconfirm", default=False, action="store_true",
        help="for those that live life on the... ledge")

    parser._action_groups.append(optional) # pushing -h back on with extras
    return vars(parser.parse_args(argv))



# conditional overide of print to custom logger, if availiable
def logger():
    None
    # in try except try to import module and return it as print function
    # else return standard print



# barebones installer to be used as fallback if full
# featured version is not availiable
def installer(path="./",
              urls=["https://github.com/DreamingRaven/RavenPythonLib"]):
    # neat trick to always ensure path ends in seperator '/' by appending empty
    path = os.path.join(path, "") # e.g "/usr/bin" vs "/usr/bin/"

    for url in urls:
        if (os.path.exists(path + os.path.basename(url)) == False):
            print(prePend, "find=false installing:",
                path + os.path.basename(url))
            try:
                os.system("cd " + path + "; git clone " + url)
            except:
                print(prePend,
                    "Could not install:", url , "to",
                    path + os.path.basename(url) )



# barebones updater to be used as fallback if full
# featured version is not availiable
def updater(path="./",
            urls=["https://github.com/DreamingRaven/RavenPythonLib"]):
    # neat trick to force filenames to always end in seperator "/"
    path = os.path.join(path, "") # e.g "/usr/bin" vs "/usr/bin/"

    # attempt self update if permission availiable
    try:
        print(prePend, "Updating self:")
        os.system("cd " + path + "; git pull")
    except:
        print(prePend + "Could not update self")

    for url in urls:
        # update any dependancies
        print(prePend, "Updating", os.path.basename(url) + ":" )
        try:
            os.system("cd " + path + os.path.basename(url) + "; git pull")
        except:
            None
