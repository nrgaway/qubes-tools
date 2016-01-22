Text and Templates
==================

Often the job of output is not about individual text lines, but about creating
multi-line files such as scripts and reports. This often leads away from standard
output mechanisms toward template packages, but ``say`` has you covered here as
well.

::

    from say import Text

    # assume `hostname` and `filepath` already defined

    script = Text()
    script += """
        !#/bin/bash

        # Output the results of a ping command to the given file

        ping {hostname!r} >{filepath!r}
    """

    script.write_to("script.sh")

Then ``script.sh`` will contain::

    !#/bin/bash

    # Output the results of a ping command to the given file

    ping 'server1234.example.com' >'ping-results.txt'

``Text`` objects are basically a list of text lines. In most cases, when you add
text (either as multi-line strings or lists of strings), ``Text`` will
automatically interpolate variables the same way ``say`` does. One can
simply ``print`` or
``say`` ``Text`` objects, as their ``str()`` value is the full text you would
assume. ``Text`` objects have both ``text`` and ``lines`` properties which
can be either accessed or assigned to.

``+=`` incremental assignment
automatically removes blank starting and ending lines, and any whitespace prefix
that is common to all of the lines (i.e. it will *dedent* any given text).
This ensures you don't need to give up
nice Python program formatting just to include a template.

While ``+=`` is a handy way of incrementally building text, it
isn't strictly necessary in the simple example above; the
``Text(...)`` constructor itself accepts a string or set of lines.

Other in-place operators are: ``|=`` for adding text while preserving leading white
space (no dedent) and ``&=`` adds text verbatim--without dedent or string
interpolation.

One can ``read_from()`` a file (appending the contents of the file to the given
text object, with optional interpolation and dedenting). One can also
``write_to()`` a file. Use the ``append`` flag if you wish to add to rather than
overwrite the file of a given name, and you can set an output encoding if you
like (``encoding='utf-8'`` is the default).

So far we've discussed ``Text`` objects almost like strings, but they also act
as lists of individual lines (strings). They are, for example,
indexable via ``[]``, and they are iterable.
Their ``len()`` is the number of lines they contain. One can
``append()`` or ``extend()`` them with one or multiple strings, respectively.
``append()`` takes a keyword parameter ``interpolate`` that controls whether
``{}`` expressions in the string are interpolated. ``extend()`` additionally takes
a ``dedent`` flag that, if true, will
automatically remove blank starting and ending lines, and any whitespace prefix
that is common to all of the lines.

If ``t`` is a ``Text`` instance, ``str(t)`` will be the full string representing it.
If you wish to move from multiple lines to a single-line, joined string, ``' '.join(t)``
does the trick.

``Text`` objects, unlike strings, are mutable. The ``replace(x, y)`` method will
replace all instances of ``x`` with ``y`` *in situ*. If given just one argument,
a ``dict``, all the keys will be replaced with their corresponding values.

``Text`` doesn't have the full set of text-onboarding options seen in `textdata
<http://pypi.python.org/pypi/textdata>`_, but it should suit many circumstances.
If you need more, ``textdata`` can be used alongside ``Text``.

Finally, it's possible to use a ``Text`` object like a file and write to it.
So::

    t = Text()
    say.set(files=[sys.stdout, t])

    say('something')

will now append each thing said to both ``sys.stdout`` and ``t``.

There is a related class ``Template`` that does not interpolate its
format variables when constructed, but rather when explicitly rendered. This
suits certain form-filling operations::

    t = Template("Dear {name},\n\nWelcome to our club!\n")
    for name in 'Joe Jane Jeremey'.split():
        print t.render()


