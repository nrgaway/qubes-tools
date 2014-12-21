#####
Notes
#####

.. topic:: Restructured Text (reST) and Sphinx CheatSheet

  |  `<http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`_
  |  `<http://www.math.uiuc.edu/~gfrancis/illimath/windows/aszgard_mini/movpy-2.0.0-py2.4.4/manuals/docutils/ref/rst/directives.html>`_
  |  `<http://sphinx-doc.org/rest.html>`_

::

  # vim formatting and command to reformat to 80 chars / line
  # vim: set textwidth=80 ts=4 sw=4 sts=4 et :
  # gqG - reformat to 80 chars per column


================================================================================
December 5-7, 2014
================================================================================

.. topic:: Tasks

  - Created a dedicated development environment for Qubes work
  - Created dedicated Qubes OS signing key
  - Created repo on Github
  - Created a WIP branch of ``qubes-builder`` (nrgaway) to pull proper branches /
    repos
  - Created a script to install develop dependencies for python and track missing
    spec depends
  - Able to get doc to compile and read though them

  ..

  - Should I create copy of all repos on Github
  - ``[Resolved]`` How to sign (tag) -- manually or via Makefile?
  - How to add a git remote (your branch to my branch)
  - ``[Resolved: 80]`` Line length 80 or 132?
  - ``pep8``; ``pylint``; ``travis-ci``

I have reviewed the docs and test, noticing only init and vm tests are currently
implemented so far.  Most of the code still seems foreign to me at this point so
I guess I should just dive in and start something to become more familiar on how
it all works together.

Do you just want me to start proof reading the code correcting spelling
mistakes, remove unused imports, etc?

================================================================================
December 8, 2014
================================================================================

.. topic:: Tasks

  - Manually compiled git to newest version to allow auto-sign of commits
  - Moved NOTES from ``qubes-builder`` here
  - Configured Thunderbird better for displaying reply emails
  - Moved ``depends.sh`` from core-admin to here
  - Added global ignore for all my debuggers, etc
  - Added code to ``examples/nrgaway.conf`` in my personal ``qubes-builder`` (nrgaway
    branch)repo to add my keyring using my qubes-os signing key located in
    ``qubes-builder`` (``nrgaway-qubes-signing-key.asc``)

   ..

    | Make nrgaway-keyring
    | Fingerprint=E0E3 2283 FDCA C1A5 1007  8F27 1BB9 B1FB 5A4C 6DAD

  - Signed and tagged all repos I am currently working with and removed NOCHECK

  - From builder.conf:
     ``qubes-builder, core-admin, qubes-tools``

.. PARSED-LITERAL::

.. topic:: Git Installation from Source Notes

  |  **git-key:**
  |    `<http://pgp.mit.edu:11371/pks/lookup?search=0x96AFE6CB&op=index&fingerprint=on>`_
  |    `<http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x20D04E5A713660A7>`_
  |    Fingerprint=96E0 7AF2 5771 9559 80DA  D100 20D0 4E5A 7136 60A7

  .. CODE::

    # git install steps:
    git clone https://github.com/git/git.git
    cd git git fetch
    
    git checkout v2.2.0
    git verify-tag v2.2.0
    #yum erase git  # No point in removing existing git if you want kdevelop* + perl-Git
    make configure
    
    ./configure --prefix=/usr
    make all doc sudo
    make install install-doc install-html; # as root

    # Re-install packages that were removed when removing git
    sudo yum install kdevelop kdevelop-libs perl-Git

  Opps, kdevelop kdevelop-libs perl-Git require git as depend, so I guess
  re-install old git package again, and re-run ``make install...`` again to
  over-write git

  .. NOTE::
     Will need to ``make-install`` again on any git repo update though


================================================================================
December 9, 2014
================================================================================

.. topic:: Tasks

  - reviewing ``core-admin/qubes modules``
  - we could consider adding doc string to beginning of each module to give a
    complete overview of what each module does and include some example code as
    well
  - maybe ``qubes.__init__`` should be refactored; really big
  ..
  - CamelCase for class names?
  - camelCase for method names
  - snake_case for attrs
  - min 3 chars for vars/attrs?  except in cases of i, x


================================================================================
December 12, 2014
================================================================================

.. CODE::

    pylint --rcfile=/path/to/salt/.pylintrc salt/dir/to/lint autopep8
       --ignore E309 --aggressive --aggressive --experimental autopep8

       --ignore E309 --max-line-length 79 --experimental pep8 -a -a

**--experimental**:  Better handling of line formatting E301 - Put a blank line
between a class docstring and its first method declaration.  E309 - Put a blank
line between a class declaration and its first method declaration.

Add ``# noqa`` inline to ignore a specific pep8 rule (such as E690 changing '=='
to 'is')

``pip install autopep8`` (don't install package; rpm version too old)

.. admonition:: TODO

.. topic:: Pep8 config file:

  ``~/.config/pep8 [pep8] ignore = E226,E302,E41 max-line-length = 160``

  At the project level, a ``tox.ini`` file or a ``setup.cfg`` file is read if present
  (.pep8 file is also supported, but it is deprecated). If none of these files
  have a [pep8] section, no project specific configuration is loaded.

.. topic:: Pep8 Links:

  | **pypi:**
  |  `<https://pypi.python.org/pypi/pep8>`_
  ..
  | **docs:**
  |  `<http://pep8.readthedocs.org/en/latest/>`_
  |  `<http://pep8.readthedocs.org/en/latest/intro.html#error-codes>`_
  ..
  | **Autopep8:**
  |  pypi: `<https://pypi.python.org/pypi/autopep8>`_
  |  github: `<https://github.com/hhatto/autopep8>`_

  | **Related Tools:**
  |   `<https://github.com/jcrocholl/pep8/wiki/RelatedTools>`_


================================================================================
December 13, 2014
================================================================================

.. topic:: Links

  | **sphinxcontrib:**
  |  `<https://bitbucket.org/birkenfeld/sphinx-contrib>`_

In reviewing docs, and after applying creating pylint and pep8 rules I noticed
docs needed some love.  I had a really difficult time following the docs mostly
due to the formatting.

I checked out the Sphinx included default themes that, but they were also quite
ugly and hard to read so I decided on creating a Qubes specific theme.

In my theme research I at first considered using bootstrap and even installed
some bootstrap theme but it would be too difficult to modify since the bootstrap
css is not so friendly.  I have experience with semantic-ui and went ahead and
used that as a base and found it would work nicely


================================================================================
December 14-16, 2014
================================================================================

Implemented the new Qubes Sphinx/Semantic theme taking into consideration future
corporate branding as will be required.

I am thinking someone (maybe me) should take a look at branding everything
nicely so its all very modern and visually pleasing and of course make sure
everything has same look and feel.  This will be important to attract corporate
users.

Things I feel that need to happen will be an overhaul of main web site with a
modern theme.  Before that happens, confirm Trac is the system that we want to
stick with, but provide a few options to consider that would allow an easy
enough migration path.

Sphinx Theme Features:
  - About 85-90% complete.  Search may not work; need to test
  - Added Qubes corporate logo
  - Mobile friendly (almost)
  - Will be easy to re-theme (different colours / fonts / layout) now using the
    semantic-ui framework
  - Added coloured callouts for section and inner section which are toggleable
    on/off and saved locally on the browser
  - Created a nice flow for reading

TODO (at  some later date):
  - Footer and search page still using old format
  - Final font colours and style still needs to be picked
  - Complete search template
  - Reformat menu list

ISSUES:
  - I had a few issues that took more time than I would have liked to to figure
    out. 
  - [Solved] First issue was trying to get toggle's popup to change text based
    on state
  - [Solved] Was trying to use cookies to save toggle state, but cookies did
    not seem to work on localhost.  Found an html5 command to allow local
    storage (``localStorage.setItem``) that was even easier than using cookies
  - [Solved] Getting side column to flow nicely and dis-appear if screen res
    got lower (tablet, mobile).  Applied proper css styling to fix


================================================================================
December 16-17, 2014
================================================================================

After reviewing code and creating initial tools and configurations for code
syntax I again started into proof reading the code and docs as requested.  I was
soon overwhelmed wondering how to keep this up on an on-going basis so looked
into ways to handle this.

I found a spelling extension for Sphinx and implemented it.  It did a nice job
of finding spelling mistakes, but lacked in the ability for reviewing the
mistakes and adding words to the master dictionary easily that were considered
good words.

I created a small sphinx extension that also works stand alone that takes the
spelling output and removes duplicates and formats it nicely for review.  I
decided to also in include the suggested word replacements so one could easily
compare if the word was actually a mistake.  I chose a simple YAML format for
the only reason that the word and suggestions will be styled different colours
when reviewing so it made it even easier to read.  I am just using regex to
parse it (not YAML parser).

I then used the tool to fix all spelling errors it could find :)

To run the spelling extension, just type ``make spelling`` in the docs directory.
If there are no typos, then it will complete without an error, otherwise it will
show an error and there will be two files written in the ``_build/spelling``
directory named output.txt and output-missing.txt.  The latter sorts and removes
duplicate entries and displays for easy review.  If there are words that we want
added to the dictionary, keep them in that file and delete all those words that
are spelling mistakes, then run ``_ext/spelltool _build/spelling/output-missing
spelling_wordlist.txt`` and that will add the words left in output-missing.yaml
to the dictionary.  Then run 'make spelling' again and use that list to fix
spelling mistakes.

Cleaned up theme, spelling. code profiling code and committed it.  Not sure if I
am signing it correctly yet though


================================================================================
December 18, 2014
================================================================================

Will be starting on adding logging into the Qubes modules today.

Was also thinking I could start on some ``CI`` system like ``Jenkins`` to tie everything
together, especially with multiple developers working on code

