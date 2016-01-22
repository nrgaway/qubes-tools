Colors and Styles
=================

``say`` has built-in support for style-driven formatting. By default,
ANSI terminal colors and styles are automagically supported.

::

    answer = 42

    say("The answer is {answer:style=bold+red}")

This uses the `ansicolors <https://pypi.python.org/pypi/ansicolors>`_
module, though with a slightly more permissive syntax. Available colors are
'black', 'blue', 'cyan', 'green', 'magenta', 'red', 'white', and 'yellow'.
Available styles are 'bold', 'italic', 'underline', 'blink', 'blink2',
'faint', 'negative', 'concealed', and 'crossed'. These styles can be
combined with a ``+`` or ``|`` character. Note, however, that not all styles
are available on every terminal.

.. note:: When naming a style within the template braces (``{}``) of format strings, you can quote the style name or not. ``fmt("{x:style=red+bold}")`` is equivalent to ``fmt("{x:style='red+bold'}")``.

You can define your own styles::

    say.style(warning=lambda x: color(x, fg='red'))

Because styles are defined through executables (lambdas, usually), they can
include decisions or text transformations of arbitrary complexity.
For example::


    say.style(redwarn=lambda n: color(n, fg='red', style='bold') if int(n) < 0 else n)
    ...
    say("Result: {n:style=redwarn}")

That will display the number ``n`` in bold red characters, but only if it's value is
negative. For positive numbers, ``n`` is displayed normally.

Or define a style where a message is surrounded by red stars::

    say.style(stars=lambda x: fmt('*** ', style='red') + \
                              fmt(x,      style='black') + \
                              fmt(' ***', style='red'))
    say.style(redacted=lambda x: 'x' * len(x))

    message = 'hey'
    say(message, style='stars')
    say(message, style='redacted')

Yields::

    *** hey ***
    xxx

(with red stars)

.. note:: Style defining lambdas (or functions) take string arguments. If the string is logically a number, it must be then cast into an ``int``, ``float``, or whatever. The code must ultimate return a string.

You can also apply a style to the entire contents of a ``say`` or ``fmt`` invocation::

    say("There is green everywhere!", style='green|underline')

While the goal of ``say`` is to have correct behavior under absolutely all
combinations of text styling, coloring, indentation, numbering, and so on, be
aware that the coloring/styling is relatively new, has limited tests and
documentation to date, and is still evolving. One known bug attends ``say``'s
use of Python's ``textwrap`` module, which is not savvy to ANSI-terminal control
codes; text that includes control codes and is wrapped is currently likely to
wrap in the wrong place. Enclosing one bit of colored text inside another bit of
colored text is not as easy as it could be. Finally, style definitions are
idiosyncratically shared across instances. That said, some fairly complex
invocations already work quite nicely. Try, e.g.::

    say.set(prefix=numberer(template=color('{n:>3}: ', fg='blue')), \
            wrap=40)
    say('a long paragraph...with gobs of text', style='red')

This correctly puts the line numbers in blue, wraps the lines to 40 characters,
and puts the text in red. (The ``textwrap`` collision with control characters
is avoided here because the wrapped text is pure, and the control codes for
red styling are added after wrapping.)

Styled formatting is an extremely powerful approach, giving the
same kind of flexibility and abstraction seen for styles in word processors and
CSS-based Web design. It will be further developed.
Plans already include replacing ``textwrap`` with an ANSI-savvy text wrapping
module, providing simpler ways to state complex formatting, and mechanisms
to auto-map styles into HTML output.

