import os
import tempfile

import pytest

import solutions

def test_biggest1():
    t = [5, 6, 9, 12, -5, 2]
    assert solutions.biggest(t) == 12

def test_biggest2():
    t = [5, 6, 9, 12, -5, 2]
    assert solutions.biggest2(t) == [12, 9]

def test_biggestn():
    t = [5, 6, 9, 12, -5, 2]
    assert solutions.biggestn(t, 1) == [12]
    assert solutions.biggestn(t, 2) == [12, 9]
    assert solutions.biggestn(t, 3) == [12, 9, 6]
    assert solutions.biggestn(t, 4) == [12, 9, 6, 5]



def test_ffstring():
    fname = tempfile.mktemp()
    with open(fname, "w") as f:
        f.write("py\nthon\n\nruby\nperl")
    assert solutions.ffindstring(fname, "y\nt")
    assert not solutions.ffindstring(fname, "python")
    assert solutions.ffindstring(fname, "ruby")
    os.unlink(fname)
        

def test_panagram():
    assert solutions.panagram("the quick brown fox jumps over the lazy dog")
    assert not solutions.panagram("the quick brown fox jumped over the lazy dog")


def test_breakdown():
    denominations = {1000: 2, 500:4, 100: 5, 50: 2, 20: 2, 10:1, 5:1, 1:5}
    d = solutions.breakdown(750, denominations)
    assert d == {500: 1, 100: 2, 50: 1}
    assert denominations == {1000: 2, 500:3, 100: 3, 50: 1, 20: 2, 10:1, 5:1, 1:5}
    d = solutions.breakdown(1516, denominations)
    assert d == {1000: 1, 500: 1, 10: 1, 5:1, 1:1}
    assert denominations == {1000: 1, 500:2, 100: 3, 50: 1, 20: 2, 10:0, 5:0, 1:4}
    with pytest.raises(solutions.NotAvailable):
        d = solutions.breakdown(9516, denominations)
    assert denominations == {1000: 1, 500:2, 100: 3, 50: 1, 20: 2, 10:0, 5:0, 1:4}

    
