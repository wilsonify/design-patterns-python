import pytest

from dpatterns_python.creational import factory


@pytest.mark.parametrize('animal', ['dog', 'cat'])
def test_get_pet(animal):
    d = factory.get_pet(animal)
    print(d.speak())
