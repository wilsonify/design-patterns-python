"""
test bridge pattern
"""

import pytest

from dpatterns_python.structural import bridge


def test_main():
    """
    call the main
    :return:
    """
    bridge.main()


@pytest.mark.parametrize(('inputs'), ([1, 2, 3], [2, 3, 4]))
def test_draw(inputs):
    """
    test one circle at a time
    :param inputs:
    :return:
    """
    circle1 = bridge.Circle(*inputs, bridge.DrawingAPIOne())
    circle1.draw()
