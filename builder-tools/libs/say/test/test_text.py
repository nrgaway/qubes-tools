
import six
import os
import sys
from say import Say, Text, Template
import pytest


def test_text_basic():
    t = Text()

    x, y, s = 1, 2, 'this thing'
    t.append('{x} < {y}')
    assert t.text == '1 < 2'
    t.append('{s} x')
    t.append('and {s!r}')
    assert t.text == "1 < 2\nthis thing x\nand 'this thing'"


def test_scripting_example():

    hostname = 'server1234.example.com'
    filepath = 'ping-results.txt'

    script = Text()
    script += """
        !#/bin/bash

        # Output the results of a ping command to the given file

        ping {hostname!r} >{filepath!r}
    """

    assert str(script) == "!#/bin/bash\n\n# Output the results of a ping command to the given file\n\nping 'server1234.example.com' >'ping-results.txt'"


def test_append_raw():
    t = Text()
    x = 212
    t.append('{x}')
    t.append('{x}', interpolate=False)
    assert t.text == '212\n{x}'


def test_insert():
    x = 'Thunderdome'

    t = Text('this\nis\n{x}')
    t.insert(2, 'not')
    assert t.text == 'this\nis\nnot\nThunderdome'

    t1 = Text('this\nis\n{x}')
    t1.insert(2, 'not\nyet')
    assert t1.text == 'this\nis\nnot\nyet\nThunderdome'

    t3 = Text('this\nis\n{x}')
    t3.insert(0, 'and')
    assert t3.text == 'and\nthis\nis\nThunderdome'

    t4 = Text('this\nis\n{x}')
    t4.insert(-1, 'a')
    assert t4.text == 'this\nis\na\nThunderdome'

    t5 = Text('this\nis\n{x}')
    t5.insert(len(t5), 'is it not?')
    assert t5.text == 'this\nis\nThunderdome\nis it not?'

    y = 'is it not?'
    t6 = Text('this\nis\n{x}')
    t6.insert(len(t6), '{y}')
    assert t6.text == 'this\nis\nThunderdome\nis it not?'


def test_len():

    t = Text('1\n2\n\3\n')
    assert len(t) == 3


def test_contains():
    t = Text("and this\nis\none")
    assert "and" in t
    assert "this" in t
    assert "bozo" not in t


def test_or():
    t = Text('one')

    x = 2
    tnew = t | '   two {x}'
    assert tnew.text == 'one\n   two 2'


def test_and():
    t = Text('one')

    x = 2
    tnew = t & '   two {x}'
    assert tnew.text == 'one\n   two {x}'


def test_ior():
    t = Text('one')

    x = 2
    t |= '   two {x}'
    assert t.text == 'one\n   two 2'


def test_iand():
    t = Text('one')

    x = 2
    t &= '   two {x}'
    assert t.text == 'one\n   two {x}'


def test_iadd():
    t = Text()

    t += """
        # this is a script
        # which should be left aligned and compact
            # with one indented line
    """
    assert t.text == "# this is a script\n# which should be left aligned and compact\n    # with one indented line"

    t2 = Text()
    t2 += """
        # this is a script
        # which should be left aligned and compact
            # with one indented line
    """
    assert t2.text == "# this is a script\n# which should be left aligned and compact\n    # with one indented line"


def test_adding_other_text():

    t = Text("this is good")
    u = Text("this too!")

    tu = t + u
    assert tu.text == "this is good\nthis too!"

    t += u
    assert t.text == "this is good\nthis too!"


def test_indexing():
    t = Text('this\nis\nsomething')
    assert t[0] == 'this'
    assert t[1] == 'is'
    assert t[2] == 'something'
    t[1] = 'would be'
    assert t.text == 'this\nwould be\nsomething'


def test_replace():
    t = Text('a\nb\nc\nd')
    assert t.lines == 'a b c d'.split()

    t.replace('b', 'B')
    tres = t.replace('d', 'D')
    assert t.lines == 'a B c D'.split()
    assert tres == t


def test_replace_many():
    t = Text('a\nb\nc\nd')
    assert t.lines == 'a b c d'.split()

    tres = t.replace({'b': 'BEE', 'd': 'DEE'})
    assert t.lines == 'a BEE c DEE'.split()
    assert tres == t


def test_replace_with_text():
    t = Text()
    t += 'this is\nsome\ntext here'

    middle = Text("some incredible\nawesome\nlively")
    t.replace('some', middle)
    assert t.text == 'this is\nsome incredible\nawesome\nlively\ntext here'
    assert len(t) == 5


@pytest.mark.xfail
def test_re_replace():
    t = Text('a\nb\nc\nd')
    assert t.lines == 'a b c d'.split()

    t.re_replace(r'[b]', 'B')
    t.re_replace(r'd', lambda m: m.group(0).upper())
    assert t.lines == 'a B c D'.split()

    t1 = Text('and then there were none'.split())
    t1.re_replace(r'(?P<art>the)', lambda m: '*' + m.art.upper() + '*')
    assert t1.lines == 'and *THE*n *THE*re were none'.split()


def test_set_text():
    t = Text()

    t.text = 'this\nis'
    assert t.text == 'this\nis'
    assert t.lines == ['this', 'is']

    t.lines = ['and', 'one', 'more']
    assert t.text == 'and\none\nmore'


def test_excess_newlines():
    t = Text()

    t.lines = ['too\n', 'many\n', 'newlines\n']
    assert t.text == 'too\nmany\nnewlines'
    assert t.lines == ['too', 'many', 'newlines']


def test_iter():
    t = Text('someday\nsoon')
    assert [x for x in t] == ['someday', 'soon']


def test_init():

    d = 4409

    t = Text('someday\nsoon {d}')
    assert t.text == 'someday\nsoon 4409'

    t = Text(['someday', 'soon {d}'])
    assert t.text == 'someday\nsoon 4409'

    b = 'boy'

    t2 = Text('hey {b}')
    assert t2.text == 'hey boy'

    t3 = Text('hey {b}', interpolate=False)
    assert t3.text == 'hey {b}'

    t4 = Text("""
        Now this
        is more
        like it!
    """)
    assert t4.text == "Now this\nis more\nlike it!"

    t5 = Text(dedent=False, data="""
        Now this
        is more
        like it!
    """)
    assert t5.text == "\n        Now this\n        is more\n        like it!\n    "


def test_str_and_render():
    t = Text('someday\nsoon')

    assert str(t) == 'someday\nsoon'

    assert str(t) == t.render()


def test_repr():
    t = Text('someday\nsoon')

    import re
    assert re.match('Text\(\d+, \d+ lines\)', repr(t))


def test_read(tmpdir):

    p = tmpdir.join("hello.txt")
    p.write("this\nthat\nyonder\n")

    path = str(p)

    t = Text()
    t.read_from(path)
    assert t.lines == 'this that yonder'.split()

    t.read_from(path)
    assert t.lines == 'this that yonder this that yonder'.split()


def test_write(tmpdir):
    p = tmpdir.join("writetest.txt")
    path = str(p)

    t = Text('a\nb\nc\nd')

    t.write_to(path)

    assert p.read() == 'a\nb\nc\nd'



def test_Text_as_file():
    t = Text()
    say = Say()

    # test normal operation
    say.set(files=[t])
    contents = "and\nthis\nworks"
    say(contents)
    assert t.text == contents

    # test blank says (should add just \n)
    say()
    assert t.text == contents + "\n"


def test_Template():
    tstr = """
        Is {name} okay?
        He seems {mood}.
    """
    t = Template(tstr)
    assert str(t) == "Is {name} okay?\nHe seems {mood}."

    name = 'Joe'
    mood = 'edgy'
    assert t.render() == "Is Joe okay?\nHe seems edgy."

    name = 'Bill'
    assert t.render() == "Is Bill okay?\nHe seems edgy."

    mood = 'giddy'
    assert t.render() == "Is Bill okay?\nHe seems giddy."
