Encodings
=========

Character encodings remain a fractious and often exasperating part of IT.
``say()`` and ``fmt()`` try to avoid this by working with Unicode strings. In
Python 3, all strings are Unicode strings, and output is by default UTF-8
encoded. Yay!

In Python 2, we try to maintain the same environment. If a template or input
string is *not* of type ``unicode``, please include only ASCII characters, not
encoded bytes from UTF-8 or whatever. If you don't do this, any trouble results
be on your head. If ``say`` opens a file for you (e.g. with ``setfiles()``), it
uses ``io.open()`` to inherit its default encoding to UTF-8. If you have ``say``
write to a file that you've opened, you should similarly use ``io.open()`` or
another mechanism that transparently writes to a proper encoding.

