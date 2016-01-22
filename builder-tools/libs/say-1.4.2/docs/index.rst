say
===

It's been *forty five years* since ``C`` introduced ``printf()`` and the basic
formatted printing of positional parameters. Isn't it time for an upgrade?
**You betcha!**

``say`` evolves Python's ``print``
statement/function, ``format`` function/method, and ``%`` string
interpolation operator with simpler, higher-level facilities. For example,
it provides direct template formatting:

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



.. toctree::
   :titlesonly:

   Usage <usage>
   Indentation and Wrapping <indentwrap>
   Prefixes and Suffixes <prefixsuffix>
   The Value Proposition <valueprop>
   Titles, Rules, and Spacing <titles>
   Colors and Styles <styles>
   Where and When You Like <wherewhen>
   Encodings <encodings>
   Non-Functional Invocation <nonfunctional>
   Text and Templates <text>
   Iterpolators and Exceptions <iterpolators>
   Python 3 <python3>
   Alternatives <alternatives>
   Notes and To-Dos <notes>
   API Reference <api>
   Installation <installation>
   CHANGES
