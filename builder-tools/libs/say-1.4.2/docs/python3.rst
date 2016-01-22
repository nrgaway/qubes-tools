Python 3
========

Say works virtually the same way in Python 2 and Python 3. This can simplify
software that should work across the versions, without the hassle
of ``from __future__ import print_function``.

``say`` attempts to mask some of the quirky complexities of the 2-to-3 divide,
such as string encodings and codec use. In general, things work best if
you use Unicode strings any time you need to use non-ASCII characters.
In Python 3, this is automatic.

