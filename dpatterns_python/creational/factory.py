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


def main():
    """
    try out the pet factory
    :return:
    """
    dog1 = get_pet("dog")

    print(dog1.speak())

    cat1 = get_pet("cat")

    print(cat1.speak())


if __name__ == "__main__":
    main()
