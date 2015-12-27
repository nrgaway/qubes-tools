The Value Proposition
=====================

While it's easy enough to add a few spaces to the format string of any ``print``
statement or function in order to achieve a little indentation, it's easy to
mistakenly type too many or too few spaces, or to forget to type them in some
format strings. If you're indenting strings that themselves may contain
multiple lines, the simple ``print`` approach breaks because it won't take
multi-line strings into account. Nor will it be integrated with line wrapping
or numbering or other formatting you also want.

``say``, however, simply and correctly handles these combined formatting
operations. Harder cases like multi-line strings are just as nicely and well
indented as simple ones--something not otherwise easily accomplished without
adding gunky, complexifying string manipulation code to every place in your
program that prints anything.

This starts to illustrate ``say``'s "do the right thing" philosophy. So many
languages' printing and formatting functions "output values" at a low level.
They may format basic data types, but they don't provide straightforward ways to
do neat text transformations that rapidly yield correct, attractively-formatted
output. ``say`` does. Over time, ``say`` will provide even more high-level
formatting options. For now: indentation, wrapping, and line numbering.

.. note:: If you do find any errors in the way ``say`` handles formatting operations,
    `there's an app for that <https://bitbucket.org/jeunice/say/issues>`_. Let's fix
    them once, in a common place, in reusable code--not spread around many different programs.

