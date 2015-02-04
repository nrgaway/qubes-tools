#!/usr/bin/python2 -O
# -*- coding: utf-8 -*-

'''
Qubes OS

:copyright: © 2014 Jason Mehring <nrgaway@gmail.com>
'''

__author__ = 'Jason Mehring'
__license__ = 'GPLv2 or later'
__version__ = '0.1'

import os
import shutil
import sys
import re
import argparse

DEBUG = False
DEPENDS_RE = re.compile(r"^Build-Depends:(.*?)^[A-Z].*?:", re.MULTILINE|re.DOTALL)
PACKAGE_RE = re.compile(r"([a-zA-Z]{1}.+?)[,\s\$]", re.MULTILINE|re.DOTALL)

def main(argv):
    default = 'debian/control'

    parser = argparse.ArgumentParser()
    parser.add_argument('control_file',
                        action="store",
                        nargs='?',
                        const=default,
                        default=default,
                        help="Path to Debian control file")
    args = parser.parse_args()

    if os.path.exists(args.control_file):
        parseControlFile(args.control_file)
    else:
        print "You must run parsedepends.py in a source package containing debian/control"
        sys.exit(1)

def parseControlFile(path):
    result = []
    with open(path) as file_:
        if DEBUG:
            print file_.read()
            file_.seek(0)
        depends = DEPENDS_RE.search(file_.read())
        if depends:
            if DEBUG:
                print depends.groups()
            packages = PACKAGE_RE.findall(depends.group(1))
            if packages:
                if DEBUG:
                    print packages
                for pkg in packages:
                    if DEBUG:
                        print pkg.rsplit(' ')[0].strip()
                    result.append(pkg.rsplit(' ')[0].strip())
    print ' '.join(result)

if __name__ == "__main__":
    main(sys.argv[1:])
