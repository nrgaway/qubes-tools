Notes
=====

* The ``say`` name was inspired by Perl's `say <http://perldoc.perl.org/functions/say.html>`_,
  but the similarity stops there.

* Automated multi-version testing managed with the wonderful
  `pytest <http://pypi.python.org/pypi/pytest>`_,
  `pytest-cov <http://pypi.python.org/pypi/pytest-cov>`_,
  `coverage <http://pypi.python.org/pypi/coverage>`_,
  and `tox <http://pypi.python.org/pypi/tox>`_.
  Packaging linting with `pyroma <https://pypi.python.org/pypi/pyroma>`_.

* Successfully packaged for, and tested against, all late-model versions of
  Python: 2.6, 2.7, 3.2, 3.3, 3.4, and 3.5 as well as
  PyPy 2.6.0 (based on 2.7.9) and PyPy3 2.4.0 (based on 3.2.5).

* ``say`` has greater ambitions than just simple template printing. It's
  part of a larger rethinking of how output should be formatted.
  ``say.Text``, `show <http://pypi.python.org/pypi/show>`_, and `quoter
  <http://pypi.python.org/pypi/quoter>`_ are other down-payments on this
  larger vision. Stay tuned.

* In addition to being a practical module in its own right, ``say`` is
  testbed for `options <http://pypi.python.org/pypi/options>`_, a package
  that provides high-flexibility option, configuration, and parameter
  management.

* The author, `Jonathan Eunice <mailto:jonathan.eunice@gmail.com>`_ or
  `@jeunice on Twitter <http://twitter.com/jeunice>`_
  welcomes your comments and suggestions. If you're using ``say`` in your own
  work, drop me a note and tell me how you're using it, how you like it,
  and what you'd like to see!

* If you find ``say`` useful, consider buying me a pint and a nice
  salty pretzel. |funding|

.. |funding| image:: https://img.shields.io/gratipay/jeunice.svg
    :target: https://www.gittip.com/jeunice/

To-Dos
======

* Use a text wrapping module that is fully cognient of ANSI escape codes.
* Further formatting techniques for easily generating HTML output and
  formatting non-scalar values.
* Complete the transition to per-method styling and more refined named
  styles.
* Provide code that allows ``pylint`` to see that variables used inside
  the ``say`` and ``fmt`` format strings are indeed thereby used.
