# @Author: George Onoufriou <GeorgeRaven>
# @Date:   2018-05-16
# @Project: RavenNucleon
# @Filename: log.py
# @Last modified by:   GeorgeRaven
# @Last modified time: 2018-05-17
# @License: Please see LICENSE file in project root

class Log(object):

    import os, sys
    from colorama import Fore, Back, Style, init

    className = "Log"
    prePend = "[ " + os.path.basename(sys.argv[0]) + " -> " + className + "] "
    prePend_parent = "[ " + os.path.basename(sys.argv[0]) + " ]"
    init(autoreset=True) # forces colorama to auto reset colors

    def __init__(self, logLevel=-1):
        self.logLevel = logLevel

    def print(self, text, minLogLevel=3):
        if(minLogLevel==-1):
            print(text) # this allows for universal formating as no prePending
        elif(minLogLevel==0) and (self.logLevel >= minLogLevel):
            print(self.Fore.GREEN + self.prePend_parent + " [ info ] " + text)
        elif(minLogLevel==1) and (self.logLevel >= minLogLevel):
            print(self.Fore.YELLOW + self.prePend_parent + " [ warn ] " + text)
        elif(minLogLevel==2) and (self.logLevel >= minLogLevel):
            print(self.Fore.RED + self.prePend_parent + " [ error ] " + text)
        elif(minLogLevel==3) and (self.logLevel >= minLogLevel):
            print(self.Fore.MAGENTA +self.prePend_parent + " [ debug ] " + text)
        #TODO implement level specific formating

if __name__ == "__main__":
    log = Log()
