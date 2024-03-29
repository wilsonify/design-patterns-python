"""
prototype pattern in python
"""

import copy


class Prototype:
    """
    Prototype
    """

    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:
    """
    Car
    """

    def __init__(self):
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return "{} | {} | {}".format(self.name, self.color, self.options)


def main():
    """
    try out a prototype car
    :return:
    """
    car0 = Car()
    prototype1 = Prototype()
    prototype1.register_object("skylark", car0)

    clone1 = prototype1.clone("skylark")

    print(clone1)


if __name__ == "__main__":
    main()
