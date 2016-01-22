
| |version| |downloads| |versions| |impls| |wheel| |coverage|

.. |version| image:: http://img.shields.io/pypi/v/say.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/say

.. |downloads| image:: http://img.shields.io/pypi/dm/say.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/say

.. |versions| image:: https://img.shields.io/pypi/pyversions/say.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/say

.. |impls| image:: https://img.shields.io/pypi/implementation/say.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/say

.. |wheel| image:: https://img.shields.io/pypi/wheel/say.svg
    :alt: Wheel packaging support
    :target: https://pypi.python.org/pypi/say

.. |coverage| image:: https://img.shields.io/badge/test_coverage-96%25-blue.svg
    :alt: Test line coverage
    :target: https://pypi.python.org/pypi/say


It's been *forty five years* since ``C`` introduced ``printf()`` and the basic
formatted printing of positional parameters. Isn't it time for an upgrade?
**You betcha!**

``say`` evolves Python's ``print``
statement/function, ``format`` function/method, and ``%`` string
interpolation operator with simpler, higher-level facilities. For example,
it provides direct template formatting::

    from say import *

    x, nums, name = 12, list(range(4)), 'Fred'

    say("There are {x} things.")
    say("Nums has {len(nums)} items: {nums}")
    say("Name: {name!r}")

yields::

    There are 12 things.
    Nums has 4 items: [0, 1, 2, 3]
    Name: 'Fred'

Or instead of printing the string immediately, you want the string itself,
the ``fmt()`` function is our version of ``sprintf()``.::

    >>> fmt("{name} has {x} things and {len(nums)} numbers.")
    'Fred has 12 things and 4 numbers.'

The more items being printed, and the more complicated the ``format``
invocation, the more valuable this simple inline specification becomes.

But as nice as replacing positional templates with inline templates
is, ``say`` does a lot more.
It also works in a variety of ways to up-level the output-generation task.
For example::

    say.title('Discovered')
    say("Name: {name:style=blue}", indent='+1')
    say("Age:  {age:style=blue}", indent='+1')

Prints a nicely formatted text block, with a proper title and indentation,
and just the variable information in blue.

.. image:: http://content.screencast.com/users/jonathaneunice/folders/Jing/media/81bf4738-c875-4998-82ac-a91d211d000b/00000745.png
    :align: left

``say`` provides:

* DRY, Pythonic, inline string templates that piggyback
  Python's well-proven ``format()`` method, syntax, and underlying engine.
* A single output mechanism that works the same way across
  Python 2 or Python 3.
* A companion ``fmt()`` object for string formatting.
* Higher-order line formatting such as line numbering,
  indentation, and line-wrapping built in. You can get substantially
  better output
  formatting with almost no additional code.
* Convenient methods for common formatting items such as titles, horizontal
  separators, and vertical whitespace.
* Easy styled output, including ANSI colors and user-defined styles
  and text transforms.
* Easy output to one or more files, without additional code or complexity.
* Super-duper template/text aggregator objects for easily building,
  reading, and writing multi-line texts.

Take it for a test drive today! See `the full documentation
at Read the Docs <http://say.readthedocs.org/en/latest/>`_.
