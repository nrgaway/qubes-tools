Indentation and Wrapping
========================

Indentation is a common way to display data hierarchically. ``say`` will
help you manage it. For example::

    say('ITEMS')
    for item in items:
        say(item, indent=1)

will indent the items by one indentation level (by default, each indent
level is four spaces, but
you can change that with the ``indent_str`` option).

If you want to change the default indentation level::

    say.set(indent=1)      # to an absolute level
    say.set(indent='+1')   # strings => set relative to current level

    ...

    say.set(indent=0)      # to get back to the default, no indent

Or you can use a ``with`` construct::

    with say.settings(indent='+1'):
        say(...)

        # anything say() emits here will be auto-indented +1 levels

    # anything say() emits here, after the with, will not be indented +1

.. note:: If using a string to indicate relative indent levels offends your sense of
    dimensionality or strict typing, there is a class ``Relative`` that does the same
    thing in a more formal way. ``indent='+2'`` and ``indent=Relative(+2)`` are identical.

If you have a lot of data or text to print, and it would normally create
super-long, difficult-to-read lines, you can easily wrap it::

    say("This is a really long...blah blah blah", wrap=40)

Will automatically wrap the text to the given width
using Python's standard ``textwrap`` module.
Feel free to use indentation and wrapping together.

