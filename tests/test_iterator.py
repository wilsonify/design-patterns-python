import pytest

from dpatterns_python import iterator


@pytest.mark.parametrize('maxcount', [3, 4])
def test_count_to(maxcount):
    for num in iterator.count_to(maxcount):
        print("{}".format(num))
