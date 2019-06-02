"""
visitor pattern in python
"""


class House:
    """
    The class being visited
    """

    def accept(self, visitor):
        """Interface to accept a visitor"""
        visitor.visit(self)  # Triggers the visiting operation!

    def work_on_hvac(self, hvac_specialist):
        """
        # Note that we now have a reference to the HVAC specialist object in the house object!
        :param hvac_specialist:
        :return:
        """
        print(self, "worked on by", hvac_specialist)

    def work_on_electricity(self, electrician):
        """
        # Note that we now have a reference to the electrician object in the house object!
        :param electrician:
        :return:
        """
        print(self, "worked on by", electrician)

    def __str__(self):
        """Simply return the class name when the House object is printed"""
        return self.__class__.__name__


class Visitor:
    """
    Abstract visitor
    """

    def __str__(self):
        """Simply return the class name when the Visitor object is printed"""
        return self.__class__.__name__


class HvacSpecialist(Visitor):  # Inherits from the parent class, Visitor
    """Concrete visitor: HVAC specialist"""

    def visit(self, house):
        """
         # Note that the visitor now has a reference to the house object
        :param house:
        :return:
        """
        house.work_on_hvac(self)


class Electrician(Visitor):  # Inherits from the parent class, Visitor
    """Concrete visitor: electrician"""

    def visit(self, house):
        """
        # Note that the visitor now has a reference to the house object
        :param house:
        :return:
        """
        house.work_on_electricity(self)

    # Create an HVAC specialist


def main():
    """
    Create an electrician
    Create a house
    Let the house accept the HVAC specialist and work on the house by invoking the visit() method
    Let the house accept the electrician and work on the house by invoking the visit() method
    :return:
    """
    hvac = HvacSpecialist()

    electrician = Electrician()

    home = House()

    home.accept(hvac)

    home.accept(electrician)


if __name__ == "__main__":
    main()
