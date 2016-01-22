Non-Functional Invocation
=========================

For those who don't want to always and forever surround "print statements" with
the Python 3-style function parentheses, the ``>`` operator is
provided as an experimental, non-functional way to print. The following
are identical::

    say> "{user.id}: {user.username}"
    say("{user.id}: {user.username}")

You can name as many values as you like in the format string, but there can
only be one format string, and no options. If you need to ``say`` multiple values,
or say them with statement-specific options, you must use the functional syntax.

