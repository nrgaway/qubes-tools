#!/bin/bash
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 sts=4 et :

if ! [ $# -eq 1 ]; then
    echo "usage $0 <file_name>"
    exit
fi

# =============================================================================
# PEP8:
#     https://github.com/hhatto/autopep8
#
#     pip install --upgrade autopep8
#     pip install --upgrade pep8
# =============================================================================

path="$(readlink -m $0)"
dir="${path%/*}"

filename="${1}"
autopep8="${dir}/autopep8/autopep8.py"
docformatter="${dir}/docformatter/docformatter.py"

echo "${dir}/autopep8/autopep8.py"


# Two stages seems the best way to prevent splitting to many lines
# ----------------------------------------------------------------
$autopep8 --ignore E309,E128,E303,E112 --max-line-length 79 "${filename}" > "${filename}.pep8"
$autopep8 --ignore E309,E128,E303,E112 --max-line-length 79 -a "${filename}.pep8" > "${filename}.pep8e"
# Really be careful with this one; needs to manually be checked
$autopep8 --select E711,E7112 --max-line-length 79 "${filename}.pep8e" > "${filename}.pep8s"

cp "${filename}" "${filename}.doc"
cp "${filename}.pep8s" "${filename}.docs"
$docformatter --in-place "${filename}.doc"
$docformatter --in-place "${filename}.docs"

# Test
meld "${filename}" "${filename}.pep8s"
#meld "${filename}.pep8s" "${filename}.doc"
#meld "${filename}" "${filename}.pep8"
#meld "${filename}.pep8" "${filename}.pep8e"
#meld "${filename}.pep8e" "${filename}.pep8s"

# Ignore
# --------
# E112 - Fix under-indented comments.
# E128 - Fix a badly indented line. (Allows under-indented line)
# E309 - Add missing blank line. (Removes blank line after class def; before comment
# E303 - Remove extra blank lines. (Allows 2 blank lines between function defs) -- need to hack to make 2 lines; not more or less
