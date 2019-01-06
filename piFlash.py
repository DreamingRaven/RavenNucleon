#!/usr/bin/env python3

# @Author: George Onoufriou <georgeraven>
# @Date:   2019-01-06
# @Filename: piFlash.py
# @Last modified by:   georgeraven
# @Last modified time: 2019-01-06
# @License: Please see LICENSE in project root.
# @Copyright: George Onoufriou


import os
import subprocess
import sys

subprocess.call([
    "sudo", "parted", "--script", "/dev/sdd",
    "mklabel", "msdos",
    "mkpart", "primary", "fat32", "1MiB", "100MiB",
])

# parted - -script / dev / sdd \
#     mklabel gpt \
#     mkpart primary 1MiB 100MiB \
#     mkpart primary 100MiB 200MiB \
