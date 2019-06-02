"""
builder pattern in python
"""


class Director:
    """Director"""

    def __init__(self, builder_type):
        self._builder = builder_type

    def construct_car(self):
        """
        construct_car
        :return:
        """
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        """
        get_car
        :return:
        """
        return self._builder.car


class Builder:
    """Abstract Builder"""

    def __init__(self):
        self.car = None

    def create_new_car(self):
        """
        create_new_car
        :return:
        """
        self.car = Car()


class SkyLarkBuilder(Builder):
    """Concrete Builder --> provides parts and tools to work on the parts """

    def add_model(self):
        """
        add_model
        :return:
        """
        self.car.model = "Skylark"

    def add_tires(self):
        """
        add_tires
        :return:
        """
        self.car.tires = "Regular tires"

    def add_engine(self):
        """
        add_engine
        :return:
        """
        self.car.engine = "Turbo engine"


class Car:
    """Product"""

    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return "{} | {} | {}".format(self.model, self.tires, self.engine)


def main():
    """
    try out the builder
    :return:
    """
    builder1 = SkyLarkBuilder()
    director1 = Director(builder1)
    director1.construct_car()
    car1 = director1.get_car()
    print(car1)


if __name__ == "__main__":
    main()
