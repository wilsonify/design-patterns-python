"""
factory pattern in python
"""


class Dog:
    """
    A simple dog class
    """

    def __init__(self, name):
        self._name = name

    @staticmethod
    def speak():
        """
        the dog goes woof
        :return:
        """
        return "Woof!"


class Cat:
    """
    A simple dog class
    """

    def __init__(self, name):
        """
        new cat
        :param name:
        """
        self._name = name

    @staticmethod
    def speak():
        """
        the cat goes meow
        :return:
        """
        return "Meow!"


def get_pet(pet="dog"):
    """The factory method"""

    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))

    return pets[pet]


DOG = get_pet("dog")

print(DOG.speak())

CAT = get_pet("cat")

print(CAT.speak())
