"""
Test separable utility functions used in say
"""

import six
import sys
from say.util import *
import pytest


def test_is_string():
    assert is_string("")
    assert is_string("This")
    assert is_string(six.u("this"))
    assert stringify(six.u("a\u2014b"))

    assert not is_string(1)
    assert not is_string(None)
    assert not is_string([1, 2, 3])
    assert not is_string(['a', 'b', 'c'])


def test_stringify():
    assert stringify('this') == 'this'
    assert stringify(4) == '4'
    assert stringify(six.u("\u2014")) == six.u("\u2014")


@pytest.mark.xfail
def test_opened():
    raise NotImplementedError('TBD')


def test_encoded():

    tests = {
        ('this', None): 'this',
        ('this', 'utf-8'): six.b('this'),
        (six.u('this'), 'utf-8'): six.b('this'),
        (six.u('this\u2012and'), 'utf-8'): six.b('this\xe2\x80\x92and'),
        (six.u('this\u2012and'), None): six.u('this\u2012and'),
    }

    for data, answer in tests.items():
        (text, encoding) = data
        assert encoded(text, encoding) == answer


@pytest.mark.skipif('sys.version_info[:2] > (3,2)')
def test_encoded2():

    # Currently fail this test on py33 and py34. Seems to relate to a routine
    # that previously accepted strings only accepting bytes in py33 or later.
    # Only affects encodings that are byte-oriented, such as base64. Not
    # clear if makes sense to continue supporting them.

    tests = {
        (six.u('this-and'), 'base64'): 'dGhpcy1hbmQ=\n',
    }

    for data, answer in tests.items():
        (text, encoding) = data
        assert encoded(text, encoding) == answer


def test_flatten(*args):

    tests = [
        (1,       [1]),
        ([1],     [1]),
        ('one',   ['one']),
        (['one'], ['one']),
        ([2, 3, 4], [2, 3, 4])

    ]

    for data, answer in tests:
        assert [x for x in flatten(data)] == answer


def test_next_str():

    def gen():
        n = 1
        while True:
            yield str(n)
            n += 1

    g = gen()

    for i in range(1, 5):
        assert next_str(g) == str(i)

    assert next_str(None) == ''

    for gg in [1, 1.1, 'string', list, [1, 2, 3], {'a': 'A'}]:
        assert next_str(gg) == str(gg)


@pytest.mark.skipif('True')
def test_csv_split():
    # no quotes
    assert csv_split('x,y,z') == ['x', 'y', 'z']

    # double quotes
    assert csv_split('x,y="simple",z') == ['x', 'y="simple"', 'z']
    assert csv_split('x,y="internal comma,",z') == ['x', 'y="internal comma,"', 'z']

    # single quotes
    assert csv_split("x,y='simple',z") == ['x', "y='simple'", 'z']
    assert csv_split("x,y='internal comma,',z") == ['x', "y='internal comma,'", 'z']
