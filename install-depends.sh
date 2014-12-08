#!/bin/bash -e
# vim: set ts=4 sw=4 sts=4 et :

##
## Install python depends from .spec file
## (for development purposes)
##

##
## The Qubes OS Project, http://www.qubes-os.org
## Copyright (C) 2014 Jason Mehring <nrgaway@gmail.com>
##  
## License: GNU General Public License
##

packages="core-admin"

path="$(readlink -m $0)"
dir="${path%/*}"

for package in ${packages}; do
    "${dir}/depends.sh" $package
done
