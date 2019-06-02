"""
test factory pattern
"""

import pytest

from dpatterns_python.creational import factory


def test_main():
    """
    call the main
    :return:
    """
    factory.main()


@pytest.mark.parametrize('animal', ['dog', 'cat'])
def test_get_pet(animal):
    """
    test one pet at at time
    :param animal:
    :return:
    """
    pet_animal = factory.get_pet(animal)
    print(pet_animal.speak())
