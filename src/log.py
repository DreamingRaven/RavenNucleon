# @Author: George Onoufriou <GeorgeRaven>
# @Date:   2018-05-16
# @Project: RavenNucleon
# @Filename: log.py
# @Last modified by:   GeorgeRaven
# @Last modified time: 2018-05-16
# @License: Please see LICENSE file in project root

class Log(object):

    import os, sys

    className = "Log"
    prePend = "[ " + os.path.basename(sys.argv[0]) + " -> " + className + "] "
    prePend_parent = "[ " + os.path.basename(sys.argv[0]) + " ]"

    def __init__(self, logLevel=0):
        self.logLevel = logLevel

if __name__ == "__main__":
    log = Log()
