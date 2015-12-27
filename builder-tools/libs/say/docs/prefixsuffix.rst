Prefixes and Suffixes
=====================

Every line can be given a prefix or suffix, if desired. For example::

    with say.settings(prefix='> '):
        say('this')
        say('that')

Will give what text email and Markdown consider a quoted block look::

    > this
    > that

Or if you'd like some text to be quoted with blue quotes::

    say(text, prefix=styled('> ', 'blue'))

And if you like your output numbered::

    say.set(prefix=numberer())
    say('this\nand\nthat')

yields::

      1: this
      2: and
      3: that

You can instantiate different numberers for different files, and if you
like, use the ``start`` keyword argument to start a ``numberer`` on
a designated value.

