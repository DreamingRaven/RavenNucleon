#!/usr/bin/env python3

# @Author: George Onoufriou <georgeraven>
# @Date:   2019-01-06
# @Filename: piFlash.py
# @Last modified by:   archer
# @Last modified time: 2019-01-10
# @License: Please see LICENSE in project root.
# @Copyright: George Onoufriou


import argparse
import os
import subprocess
import sys


def main(args):

    parentPath = "./tempPiFlash"
    rootPath = parentPath + "/root"
    bootPath = parentPath + "/boot"

    wget thing peeps want
    subprocess.call([
        "wget", "http://os.archlinuxarm.org/os/ArchLinuxARM-rpi-latest.tar.gz",
        #"-P", "/dev/shm/piFlash/",
        "-O", args["tempFile"]
    ])

    # flash thing peeps want
    if(args["parted"] != None):
        subprocess.call(
            ["sudo", "parted", "--script", args["device"]] + args["parted"]
        )

    # make neccessary directories
    subprocess.call([
        "mkdir", "-p", rootPath, bootPath
    ])

    # mk vfat
    subprocess.call([
        "sudo", "mkfs.vfat", str(args["device"] + "1")
    ])

    # mk ext4
    subprocess.call([
        "sudo", "mkfs.ext4", str(args["device"] + "2")
    ])

    # mount root
    subprocess.call([
        "sudo", "mount", str(args["device"] + "2"), rootPath
    ])

    # mount boot
    subprocess.call([
        "sudo", "mount", str(args["device"] + "1"), bootPath
    ])

    # unpack tar.gz pi file into root
    subprocess.call([
        "sudo", "bsdtar", "-xpf", args["tempFile"], "-C", rootPath
    ])

    # move boot stuff to boot from root
    subprocess.call([
        "mv", str(rootPath + "/boot/*"), bootPath
    ])

    # make sure everything is where it should be pre-unmounting
    subprocess.call([
        "sync"
    ])

    # unmount everything just mounted
    subprocess.call([
        "sudo", "umount", rootPath, bootPath
    ])

    # delete the old things peeps probably dont want to free memory
    subprocess.call([
        "sudo", "rm", "-r", args["tempFile"], parentPath
    ])


def argz(argv, description=None):
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("-t", "--tempFile",
                        default=str("/dev/shm/piFlash.iso"),
                        help="set the path to the wget outfile location (default: /dev/shm/piFlash.iso)")
    parser.add_argument("-p", "--parted", nargs='+',
                        default=[
                            "mklabel", "msdos",
                            "mkpart", "primary", "1MiB", "101MiB",
                            "mkpart", "primary", "106MiB", "100%",
                        ],
                        help="path to each file desired to be converted")
    parser.add_argument("-d", "--device", required=True,
                        default="",
                        help="device path which is the target of flashing e.g /dev/sda")
    parser.add_argument("-D", "--devRoot",
                        default="",
                        help="device path which is the target of dd'ing the ISO")
    parser.add_argument("-i", "--iso",
                        default="http://os.archlinuxarm.org/os/ArchLinuxARM-rpi-latest.tar.gz",
                        help="wget path to iso to be flashed")

    # parse the initial args which have only been slightly sanitised
    args = vars(parser.parse_args(argv))

    # list args which are paths to be made cross platform
    pathArgNames = ["tempFile"]

    # return normalised args with cross platform paths
    return normArgs(args=args, pathArgs=pathArgNames)


def normArgs(args, pathArgs):
    for argName in pathArgs:
        if(type(args[argName]) != list):
            args[argName] = str(os.path.abspath(args[argName]))
        else:
            tempList = list()
            for listItem in args[argName]:
                tempList.append(str(os.path.abspath(listItem)))
            args[argName] = tempList
    return args


if(__name__ == "__main__"):
    description = "piFlash, python wget flasher for repeatable installation of raspberry pi archlinux arm"
    args = argz(sys.argv[1:], description=description)
    main(args)
