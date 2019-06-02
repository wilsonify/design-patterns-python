"""
abstract factory pattern in python
"""


class Dog:
    """One of the objects to be returned"""

    @staticmethod
    def speak():
        """
        the dog goes woof
        :return:
        """
        return "Woof!"

    def __str__(self):
        return "Dog"


class DogFactory:
    """Concrete Factory"""

    @staticmethod
    def get_pet():
        """Returns a Dog object"""
        return Dog()

    @staticmethod
    def get_food():
        """Returns a Dog Food object"""
        return "Dog Food!"


class PetStore:
    """ PetStore houses our Abstract Factory """

    def __init__(self, pet_factory=None):
        """ pet_factory is our Abstract Factory """

        self._pet_factory = pet_factory

    def show_pet(self):
        """ Utility method to display the details of the objects returned by the DogFactory """

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'!".format(pet_food))

    def show_pet_sounds(self):
        """
        extra sounds when walking into pet shop
        :return:
        """
        self.show_pet()
        self.show_pet()


# Create a Concrete Factory
FACTORY = DogFactory()

# Create a pet store housing our Abstract Factory
SHOP = PetStore(FACTORY)

# Invoke the utility method to show the details of our pet
SHOP.show_pet()
