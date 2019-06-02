import pytest

from dpatterns_python import bridge


@pytest.mark.parametrize(('inputs'), ([1, 2, 3], [2, 3, 4]))
def test_draw(inputs):
    circle1 = bridge.Circle(*inputs, bridge.DrawingAPIOne())
    circle1.draw()
