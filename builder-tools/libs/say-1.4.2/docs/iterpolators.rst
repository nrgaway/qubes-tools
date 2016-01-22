Iterpolators and Exceptions
===========================

You may want to write your own functions that take strings
and interpolate ``{}``
format templates in them. The easy way is::

    from say import caller_fmt

    def ucfmt(s):
        return caller_fmt(s).upper()

If ``ucfmt()`` had used ``fmt()``, it would not have worked. ``fmt()`` would
look for interpolating values within the context of ``ucfmt()`` and, not finding
any, probably raised an exception. But using ``caller_fmt()`` it looks into the
context of the caller of ``ucfmt()``, which is exactly where those values would
reside. *Voila!*

And example of how this can work--and a useful tool in its own right--is ``FmtException``.
If you want to have comprehensible error messages when something goes wrong, you
could use ``fmt()``::

    if bad_thing_has_happened:
        raise ValueError(fmt("Parameters {x!r} or {y!r} invalid."))

But if you define your own exceptions, consider subclassing ``FmtException``::

    class InvalidParameters(FmtException, ValueError):
        pass

    ...

    if bad_thing_has_happened:
        raise InvalidParameters("Parameters {x!r} or {y!r} invalid.")

You'll save a few characters, and the code will be simpler and more comprehensible.

