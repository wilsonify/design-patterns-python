"""
test iterator pattern
"""

import pytest

from dpatterns_python.behavioral import iterator


@pytest.mark.parametrize('maxcount', [3, 4])
def test_count_to(maxcount):
    """
    iterate
    :param maxcount:
    :return:
    """
    for num in iterator.count_to(maxcount):
        print("{}".format(num))
