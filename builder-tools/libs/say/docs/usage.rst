Usage
=====

::

    from say import *

    x = 12
    nums = list(range(4))
    name = 'Fred'

    say("There are {x} things.")
    say("Nums has {len(nums)} items: {nums}")
    say("Name: {name!r}")

yields::

    There are 12 things.
    Nums has 4 items: [0, 1, 2, 3]
    Name: 'Fred'

Or if you want the resulting string, rather than to print the string::

    >>> fmt("{name} has {x} things and {len(nums)} numbers.")
    'Fred has 12 things and 4 numbers.'

At this level, ``say`` is basically a simpler, nicer recasting of::

    from __future__ import print_function

    print("There are {0} things.".format(x))
    print("Nums has {0} items: {1}".format(len(nums), nums))
    print("Name: {0!r}".format(name))
    s = "{0} has {1} things and {2} numbers.".format(name, x, len(nums))

(The ``import`` and
numerical sequencing of ``{}`` format specs is required to make pure-Python
code work correctly from Python 2.6 forward from
a single code base.)

But ``say`` and ``fmt`` read so much nicer! They are clear, simplem
and direct, and don't separate the place where the value
should appear from the value.

Full expressions are are supported within the format braces (``{}``). Whatever
variable names or expressions are found therein will be evaluated in the context
of the caller.

The more items that are being printed, and the complicated the ``format``
invocation, the more valuable this simple inline specification becomes.

But ``say`` isn't just replacing positional templates with inline templates.
It also works in a variety of ways to up-level the output-generation task.
For example::

    say.title('Discovered')
    say("Name: {name:style=blue}", indent='+1')
    say("Age:  {age:style=blue}", indent='+1')

.. image:: http://content.screencast.com/users/jonathaneunice/folders/Jing/media/81bf4738-c875-4998-82ac-a91d211d000b/00000745.png
    :align: left

Prints a nicely formatted text block, with a proper title and indentation,
and just the variable information in blue.


