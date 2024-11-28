import pytest
from printCharEvenIndicesString import getCharAtIndicesInString

def testprintCharAtEvenIndece():
    result = getCharAtIndicesInString("abcdef")
    print(result)
    assert result == "bdf"
