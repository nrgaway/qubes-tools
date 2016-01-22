Titles, Rules, and Spacing
==========================

``say`` defines a few convenience formatting functions::

    say.title('Errors', sep='-')
    for i,e in enumerate(errors, start=1):
        say("{i:3}: {e['name'].upper()}")

might yield::


    --------------- Errors ---------------

      1: I/O ERROR
      2: COMPUTE ERROR

A similar method ``hr`` produces just a horizontal line ("rule"), like
the HTML ``<hr>`` element. For either, one can optionally
specify the width (``width``), character repeated to make the line (``sep``),
and vertical separation/whitespace above and below the item (``vsep``).
Good options for the separator might be be '-', '=', or parts of the `Unicode
box drawing character set <http://en.wikipedia.org/wiki/Box-drawing_character>`_.

A final method, ``sep``, creates a short left-aligned bar with optional
following text. It's useful for creating logical subsections.::

    say.sep("coffee")
    say("I prefer coffee")
    say.sep("tea", sep="=", width=4)
    say("I prefer tea")

Yields::

    -- coffee
    I prefer coffee

    ==== tea
    I prefer tea

You can even define reusable styles for separators (and other say calls)::

    tilde_sep = dict(sep="~", width=4)
    say.sep("pass one", **tilde_sep)

Yields::

    ~~~~ pass one

Vertical Spacing
----------------

You don't need to add explicit
newline characters here and there to achieve good
vertical spacing.  ``say.blank_lines(n)`` emits n blank lines. And just
about every ``say`` call also supports a ``vsep`` (vertical separation)
parameter.::

    say('TITLE', vsep=(2,0)        # add 2 newlines before (none after)
    say('=====', vsep=(0,2))       # add 2 newlines after (none before)
    say('something else', vsep=1)  # add 1 newline before, 1 after

This Just In
------------

A new capability is to differentially set the formatting parameters on
a method by method basis. For example, if you want to see titles
in green::

    say.title.set(style='green')

You could long set such options on a call-by-call basis, but being
able to set the defaults just for specific methods allows you to
get more formatting in with fewer characters typed.  This capability
is available on a limited basis: primarily for format-specific calls
(``blank_lines``, ``hr``, ``sep``, and ``title``) for now.

.. note:: ``title`` and ``sep`` now print out more vertical whitespace
    than in previous versions.
    This is a direct usage of this method-by-method
    configurability. Basically, ``say.title.set(vsep=1)`` and
    ``say.sep.set(vsep=(1,0))`` now come baked-in.
