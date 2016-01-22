
from say import *
from say.styling import StyleDef
import six


def test_basic_styling():
    fmt = Fmt()

    assert fmt('this', style='green+underline') == six.u('\x1b[32;4mthis\x1b[0m')
    assert fmt('this', style='bold+red') == six.u('\x1b[31;1mthis\x1b[0m')


def test_readme_example():
    fmt = Fmt()
    fmt.style(stars=lambda x: fmt('*** ', style='red') + \
                              fmt(x,      style='black') + \
                              fmt(' ***', style='red'))

    message = 'Warning, problem!'
    assert fmt(message, style='stars') == six.u('\x1b[31m*** \x1b[0m\x1b[30mWarning, problem!\x1b[0m\x1b[31m ***\x1b[0m')


def test_readme_example2():
    fmt = Fmt()
    name = 'Joe'
    assert six.u('His name is ') + fmt(name, style='blue+underline') == six.u('His name is \x1b[34;4mJoe\x1b[0m')
    assert fmt('His name is {name:style=blue+underline}') == six.u('His name is \x1b[34;4mJoe\x1b[0m')
    assert fmt('His name is {name:style="blue+underline"}') == six.u('His name is \x1b[34;4mJoe\x1b[0m')
    assert fmt("His name is {name:style='blue+underline'}") == six.u('His name is \x1b[34;4mJoe\x1b[0m')


def test_wrapping_example():
    fmt = Fmt()
    text = "Move over, Coke. It looks like Apple is the real thing. The tech giant has ended Coca-Cola's 13-year run as the world's most valuable brand on a highly regarded annual list."

    fmt = Fmt()
    fmt.set(prefix=numberer(template=color('{n:>3}: ', fg='blue')), \
            wrap=40)
    assert fmt(text) == six.u("\x1b[34m  1: \x1b[0mMove over, Coke. It looks\n\x1b[34m  2: \x1b[0mlike Apple is the real\n\x1b[34m  3: \x1b[0mthing. The tech giant has\n\x1b[34m  4: \x1b[0mended Coca-Cola's 13-year\n\x1b[34m  5: \x1b[0mrun as the world's most\n\x1b[34m  6: \x1b[0mvaluable brand on a highly\n\x1b[34m  7: \x1b[0mregarded annual list.")

    # now reset so numbering starts back at 1
    fmt = Fmt()
    fmt.set(prefix=numberer(template=color('{n:>3}: ', fg='blue')), \
            wrap=40)
    assert fmt(text, style='red') == six.u("\x1b[34m  1: \x1b[0m\x1b[31mMove over, Coke. It looks\x1b[0m\n\x1b[34m  2: \x1b[0m\x1b[31mlike Apple is the real\x1b[0m\n\x1b[34m  3: \x1b[0m\x1b[31mthing. The tech giant has\x1b[0m\n\x1b[34m  4: \x1b[0m\x1b[31mended Coca-Cola's 13-year\x1b[0m\n\x1b[34m  5: \x1b[0m\x1b[31mrun as the world's most\x1b[0m\n\x1b[34m  6: \x1b[0m\x1b[31mvaluable brand on a highly\x1b[0m\n\x1b[34m  7: \x1b[0m\x1b[31mregarded annual list.\x1b[0m")


def test_color():
    assert color('text', fg='green') == '\x1b[32mtext\x1b[0m'
    assert color('more', fg='blue', bg='yellow') == '\x1b[34;43mmore\x1b[0m'


def test_styled():
    assert color('test', fg='green', style='bold') == styled('test', 'green+bold')
    assert color('test', fg='green', style='bold') == styled('test', 'bold+green')
    assert color('test', fg='green', bg='red', style='bold') == styled('test', 'green+red+bold')
    assert color('test', fg='green', bg='red', style='bold') == styled('test', 'bold+green+red')
    assert color('test', fg='green', bg='red', style='bold') == styled('test', 'bold|green|red')
    assert color('test', fg='green', bg='red', style='bold') == styled('test', 'bold,green,red')


def test_in_or_out():
    fmt = Fmt()

    x = 12
    assert fmt(x, style='blue+white+underline') == fmt("{x:style=blue+white+underline}")

    fmt.style(bwu=autostyle('blue+white+underline'))
    fmt.style(bwu2='blue+white+underline')

    assert fmt(x, style='bwu') == fmt(x, style='blue+white+underline')
    assert fmt(x, style='bwu') == fmt(x, style='bwu2')


def test_Relative():
    assert Relative(4) == 4
    assert Relative(+4) == Relative(4)
    assert Relative(-5) == -5
    assert Relative(0) == 0
    assert Relative(1) + Relative(2) == Relative(3)
    assert Relative(1) + 2 == 3
    assert 1 - Relative(1) == 0
    assert Relative(2) - Relative(-1) == Relative(3)
    assert Relative(5) - Relative(2) == Relative(3)
    assert 1 + Relative(2) == 3
    assert repr(Relative(4)) == 'Relative(+4)'
    assert repr(Relative(-5)) == 'Relative(-5)'
    assert repr(Relative(0)) == 'Relative(0)'


def test_StyleDef_basic():
    """
    Minimal test of evovling StyleDef object
    """
    s = StyleDef(name='test', join=False)
    assert s("this") == "this"
