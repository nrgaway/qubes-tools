Installation
============

To install or upgrade to the latest version::

    pip install -U say

To ``easy_install`` under a specific Python version (3.3 in this example)::

    python3.3 -m easy_install --upgrade say

(You may need to prefix these with ``sudo`` to authorize
installation. In environments without super-user privileges, you may want to
use ``pip``'s ``--user`` option, to install only for a single user, rather
than system-wide.)

Testing
-------

If you wish to run the module tests locally, you'll need to install
``pytest`` and ``tox``.  For full testing, you will also need ``pytest-cov``
and ``coverage``. Then run one of these commands::

    tox                # normal run - speed optimized
    tox -e py27        # run for a specific version only (e.g. py27, py34)
    tox -c toxcov.ini  # run full coverage tests

The provided ``tox.ini`` and ``toxcov.ini`` config files do not define
a preferred package index / repository. If you want to use them with 
a specific (presumably local) index, the ``-i`` option will come in
very handy::

    tox -i INDEX_URL
