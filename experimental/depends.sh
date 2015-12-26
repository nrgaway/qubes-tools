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

if [ ! $# -eq 1 ]; then
    echo "usage $0 <package>"
    exit
fi

path="$(readlink -m $0)"
dir="${path%/*}"
package="${1}"
package_dir="$(readlink -m "${dir}"/..)/${1}"

if [ ! -d "${package_dir}" ]; then
    echo "${package_dir} does not exist.  Exiting!"
    exit 1
fi

# Spec files to parse
DEFAULT_SPEC="rpm_spec/*.spec"
SPEC=${2-"${DEFAULT_SPEC}"}
FILTER="python"

HR_MAX_LENGTH=128
HR_CHAR='-'

# Colors
reset=$(    tput sgr0   || tput me      )
red=$(      tput setaf 1|| tput AF 1    )
green=$(    tput setaf 2|| tput AF 2    )
blue=$(     tput setaf 4|| tput AF 4    )

function Len() {
    local len="${1}"

    re='^[0-9]+$'
    if ! [[ $len =~ $re ]] ; then
        len=${#len}
    fi    

    echo $len
}

function Hr() {
    local len=${1-80}
    local char="${2-"${HR_CHAR}"}"

    len=$(Len $len)
    while [ ${len} -gt 0 ]; do
        printf "${char}"
        len=$[$len-1]
    done
    echo
}

function Decolorize() {
    local string="${1}"

    echo "$(sed -e "s/\x1b\[[0-9;]\{1,5\}m//g" <<< "$string")"
}

function HrTitle() {
    local title="${1}"
    local title_decolorized="$(Decolorize "${title}")"
    local len="${2-${#title_decolorized}}"
    local char="${3-"${HR_CHAR}"}"
    len=$(Len $len)

    printf "${title} "
    Hr $[$len-${#title_decolorized}-1] "$char"
    printf "${reset}"
}

function Header() {
    local depends="${1}"
    local title="${2-"${blue}DEPENDS - SPEC FILE"}"
    local color="${3-"${blue}"}"

    local char='-'
    local len=80

    HrTitle "${color}${char} ${title}" ${len} "${color}${char}"
    echo ${depends} | fold -w $len -s
    Hr ${len} "${color}${char}"
    echo
}

function InstallYum() {
    local depends="${1}"
    local title="${2-"${blue}DEPENDS - SPEC FILE"}"
    local color="${3-"${blue}"}"

    Header "${depends}" "${title}" "${color}"
     sudo yum -y install ${depends}
}

function InstallPip() {
    local depends="${1}"
    local title="${2-"${blue}DEPENDS - SPEC FILE"}"
    local color="${3-"${blue}"}"

    Header "${depends}" "${title}" "${color}"
     sudo pip install --upgrade --force-reinstall ${depends} || {
         if [ -f '/usr/bin/python3-pip' ]; then
             sudo python3-pip install --upgrade --force-reinstall ${depends};
         fi
     }
}

pushd "${package_dir}" > /dev/null
    echo
    depends="$(rpmspec -q --requires ${SPEC} | uniq | grep "${FILTER}")"
    InstallYum "${depends}"
popd > /dev/null

# Manually added depends
if [ -f "${dir}/depends-${package}.missing" ]; then
    depends="$(sed 's/\#.*//g' < "${dir}/depends-${package}.missing")"
    InstallYum "${depends}" "DEPENDS - MISSING FROM SPEC FILE" "${red}"
fi

# Personal rpm packages
if [ -f "${dir}/depends-personal-rpm" ]; then
    depends="$(sed 's/\#.*//g' < "${dir}/depends-personal-rpm")"
    InstallYum "${depends}" "Personal rpm Packages" "${green}"
fi

# Personal pip packages
if [ -f "${dir}/depends-personal-pip" ]; then
    depends="$(sed 's/\#.*//g' < "${dir}/depends-personal-pip")"
    InstallPip "${depends}" "Personal pip Packages" "${green}"
fi

