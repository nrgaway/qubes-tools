import six
import os
from say import Text
from say.textrange import TextRange
import pytest


def test_basic():
    t = Text('a\nb\nc\nd')
    assert t.lines == 'a b c d'.split()

    tr = TextRange(t, 1, 3)
    assert tr.text == 'b\nc'
    assert tr.lines == ['b', 'c']

    tr += 'hey!'
    assert t.lines == 'a b c hey! d'.split()

    assert tr.text == 'b\nc\nhey!'
    assert tr.lines == ['b', 'c', 'hey!']


def test_more_slicing():
    t = Text('a\nb\nc\nd')
    assert t.lines == 'a b c d'.split()

    tr2 = TextRange(t, 2)
    assert tr2.lines == ['c', 'd']

    tr3 = TextRange(t, None, -1)
    assert tr3.lines == ['a', 'b', 'c']

    tr4 = TextRange(t, -2)
    assert tr4.lines == [ 'c', 'd']


def test_ior():
    t = Text('a\nb\nc\nd')
    assert t.lines == 'a b c d'.split()

    tr2 = TextRange(t, 2)
    assert tr2.lines == ['c', 'd']

    tr2 |= "  yo\n   mo"
    assert tr2.lines == ['c', 'd', '  yo', '   mo']
    assert t.lines == ['a', 'b', 'c', 'd', '  yo', '   mo']

    tr3 = TextRange(t, 0, 2)
    tr3 |= '    hey'
    assert tr3.lines == ['a', 'b', '    hey']
    assert t.lines == ['a', 'b', '    hey',  'c', 'd', '  yo', '   mo']

    assert tr3.text == 'a\nb\n    hey'


def test_modifications():
    t = Text('a\nb\nc\nd')
    assert t.lines == 'a b c d'.split()

    tr = TextRange(t, 0, 1)
    assert tr.lines == ['a']

    x = 12
    tr.append("{x}")
    assert tr.lines == ['a', '12']
    assert t.lines == 'a 12 b c d'.split()

    y, z = 10, "zed"
    tr.extend(["{y}", "{z}"])
    assert tr.lines == 'a 12 10 zed'.split()
    assert t.lines == 'a 12 10 zed b c d'.split()

    zz = "zoro"
    tr.insert(0, "{zz}")
    assert tr.lines == 'zoro a 12 10 zed'.split()
    assert t.lines == 'zoro a 12 10 zed b c d'.split()

    tr[1] = "woot"
    assert tr.lines == 'zoro woot 12 10 zed'.split()
    assert t.lines == 'zoro woot 12 10 zed b c d'.split()

    assert len(tr) == 5
    assert len(t) == 8

    assert list(tr) == 'zoro woot 12 10 zed'.split()
    assert list(t) == 'zoro woot 12 10 zed b c d'.split()

    assert tr.text == 'zoro\nwoot\n12\n10\nzed'

def test_indexing():

    t = Text('a\nb\nc\nd')
    assert t.lines == 'a b c d'.split()

    tr = TextRange(t, 1, 3)
    assert tr.text == 'b\nc'
    assert tr.lines == ['b', 'c']

    assert tr[0] == 'b'
    assert tr[1] == 'c'

    from pytest import raises

    with raises(IndexError):
        assert tr[2] == 'd'


def test_replace():
    t = Text('a\na\na\nb\na')
    assert t.lines == 'a a a b a'.split()

    tr = TextRange(t, 2, 4)
    assert tr.lines == 'a b'.split()

    tr.replace('a', 'A')
    assert tr.lines == 'A b'.split()
    assert t.lines == 'a a A b a'.split()


def test_replace_many():
    t = Text('a\na\na\nb\na')
    assert t.lines == 'a a a b a'.split()

    tr = TextRange(t, 2, 4)
    assert tr.lines == 'a b'.split()

    tr.replace({'a': 'A', 'b': 'BEE'})
    assert tr.lines == 'A BEE'.split()
    assert t.lines == 'a a A BEE a'.split()


def test_re_replace():
    t = Text('a\na\na\nb\na')
    assert t.lines == 'a a a b a'.split()

    tr = TextRange(t, 2, 4)
    assert tr.lines == 'a b'.split()

    tr.re_replace(r'[b]', 'B')
    tr.re_replace(r'a', lambda m: m.group(0).upper())
    assert t.lines == 'a a A B a'.split()


def test_interpolation():
    x = 21
    t = Text("Joe,\nthis is {x}")
    assert t.text == 'Joe,\nthis is 21'

    tr = TextRange(t, 1, 3)

    tr += 'and {x}'
    assert tr.text == 'this is 21\nand 21'

    tr &= 'and {x}'
    assert tr.text == 'this is 21\nand 21\nand {x}'

    assert t.text == 'Joe,\nthis is 21\nand 21\nand {x}'


def test_replace():
    t = Text('a\nb\nc\nd')
    assert t.lines == 'a b c d'.split()
    tr = TextRange(t, 1, 3)
    assert tr.lines == ['b', 'c']

    tr.replace('b', 'B')
    assert tr.lines == ['B', 'c']


def test_property_set():
    t = Text('a\nb\nc\nd')
    assert t.lines == 'a b c d'.split()

    tr = TextRange(t, 1, 3)
    tr.text = 'o\np'
    assert t.lines == 'a o p d'.split()

    tr.text = ['a', 'b']
    assert t.lines == 'a a b d'.split()

    tr.lines = ['f', 'g', 'h']
    assert t.lines == 'a f g h d'.split()


def test_read(tmpdir):

    p = tmpdir.join("hello.txt")
    p.write("this\nthat\nyonder\n")

    path = str(p)

    t = Text('a\nb\nc\nd')
    assert t.lines == 'a b c d'.split()

    tr = TextRange(t, 1, 3)
    tr.read_from(path)

    assert t.lines == 'a b c this that yonder d'.split()


def test_write(tmpdir):
    p = tmpdir.join("writetest.txt")
    path = str(p)

    t = Text('a\nb\nc\nd')
    assert t.lines == 'a b c d'.split()

    tr = TextRange(t, 1, 3)
    tr.write_to(path)

    assert p.read() == 'b\nc'


def test_repr_and_str():
    t = Text('a\nb\nc\nd')
    assert t.lines == 'a b c d'.split()

    tr = TextRange(t, 1, 3)

    trr = repr(tr)
    assert trr.startswith('TextRange(') and '1:3 of' in trr

    assert str(tr) == 'b\nc'
