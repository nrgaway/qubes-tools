Change Log
==========

**1.4.0**  (September 8, 2015)

    Added ability to set styles for some methods such as ``title``,
    ``hr``, and ``sep`` as an overlay to class, object, and per-call
    settings. This is a first delivery on what will become a general
    feature over the next few releases. Added vertical spacing to
    ``title`` and ``sep`` methods for nicer layouts.

    Increased testing line coverage to 96%, improving several
    routines' robustness in the process.


**1.3.12**  (September 1, 2015)

    Tweaks and testing for new version 1.4 of underlying ``options``
    module.

    New ``options`` version returns support for Python 2.6.


**1.3.9**  (August 26, 2015)

    Reorganized documentation structure. Updated some setup
    dependencies.


**1.3.5**  (August 17, 2015)

    Instituted integrated, multi-version coverage testing with tox,
    pytest, pytest-cov, and coverage. Initial score: 86%.


**1.3.4**  (August 16, 2015)

    Updated ``SayReturn`` logic, which was broken, in order to support
    an upgrade of ``show``


**1.3.3**  (August 16, 2015)

    Added ``sep`` method for separators.

    Some code cleanups and a few additional tests.å

    Officially switched to YAML-format Change Log (``CHANGES.yml``)


**1.3.2**  (August 12, 2015)

    Code cleanups.


**1.3.1**  (August 11, 2015)

    Doc, config, and testing updates. Removed ``joiner`` module and
    tests. May import that funcationality from ``quoter`` module in
    future.

    Python 2.6 currently unsupported due to issues with underlying
    ``stuf`` module. Support may return, depending on compatibility
    upgrades for future ``stuf`` releases.


**1.3**  (July 22, 2015)

    Added ``Template`` class. A deferred-rendering version of ``Text``


**1.2.6**  (July 22, 2015)

    Configuration, testing matrix, and doc tweaks.


**1.2.5**  (December 29, 2014)

    Fixed problem that was occuring with use of Unicode characters
    when rendered inside the Komodo IDE, which set the ``sys.stdout``
    encoding to ``US-ASCII`` not ``UTF-8``. In those cases, now
    inserts a codec-based writer object to do the encoding.


**1.2.4**  (June 4, 2014)

    Now testing for Python 3.3 and 3.4. One slight problem with them
    when encoding to base64 or similar bytes-oriented output that did
    not appear in earlier Python 3 builds. Examining.

    Added gittip link as an experiment.


**1.2.1**  (October 16, 2013)

    Fixed bug with quoting of style names/definitions.

    Tweaked documentation of style definitions.


**1.2.0**  (September 30, 2013)

    Added style definitions and convenient access to ANSI colors.


**1.1.0**  (September 24, 2013)

    Line numbering now an optional way to format output.

    Line wrapping is now much more precise. The ``wrap`` parameter now
    specifies the line length desired, including however many
    characters are consumed by prefix, suffix, and indentation.

    Vertical spacing is regularized and much better tested. The
    ``vsep`` option, previously available only on a few methods, is
    now available everywhere. ``vsep=N`` gives N blank lines before
    and after the given output statement. ``vsep=(M,N)`` gives M blank
    lines before, and N blank lines after. A new ``Vertical`` class
    describes vertical spacing behind the scenes.

    ``Say`` no longer attempts to handle file encoding itself, but
    passes this responsibility off to file objects, such as those
    returned by ``io.open``. This is cleaner, though it does remove
    the whimsical possibility of automagical base64 and rot13
    encodings. The ``encoding`` option is withdrawn as a result.

    You can now set the files you'd like to output to in the same way
    you'd set any other option (e.g. ``say.set(files=[...])`` or
    ``say.clone(files=[...])``). "Magic" parameter handling is enabled
    so that if any of the items listed are strings, then a file of
    that name is opened for writing. Beware, however, that if you
    manage the files option explicitly (e.g.
    ``say.options.files.append(...)``), you had better provide proper
    open files. No magical interpretation is done then. The
    previously-necessary ``say.setfiles()`` API remains, but is now
    deprecated.

    ``fmt()`` is now handled by ``Fmt``, a proper subclass of ``Say``,
    rather than just through instance settings.

    ``say()`` no longer returns the value it outputs. ``retvalue`` and
    ``encoded`` options have therefore been withdrawn.


**1.0.4**  (September 16, 2013)

    Had to back out part of the common ``__version__`` grabbing. Not
    compatible with Sphinx / readthedocs build process.


**1.0.3**  (September 16, 2013)

    Added ``FmtException`` class

    Tightened imports for namespace cleanliness.

    Doc tweaks.

    Added ``__version__`` metadata common to module, ``setup.py``, and
    docs.


**1.0.2**  (September 14, 2013)

    Added ``prefix`` and ``suffix`` options to ``say`` and ``fmt``,
    along with docs and tests.


**1.0.1**  (September 13, 2013)

    Moved main documentation to Sphinx format in ``./docs``, and
    hosted the long-form documentation on readthedocs.org.
    ``README.rst`` now an abridged version/teaser for the module.


**1.0**  (September 8, 2013)

    Cleaned up source for better PEP8 conformance

    Bumped version number to 1.0 as part of move to `semantic
    versioning <http://semver.org>`_, or at least enough of it so as
    to not screw up Python installation procedures (which don't seem
    to understand 0.401 is a lesser version that 0.5, because 401 >
    5).



