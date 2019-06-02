"""
template pattern in python
"""

import inspect

from abc import ABC, abstractmethod


class AbstractClass(ABC):
    """
    This class inherit from Abstract Base Class to allow the use of the @abstractmethod decorator
    """

    def template_method(self):
        """Ths is the template method that contains a collection of
        methods to stay the same, to be overridden, and to be overridden optionally.
        """

        self.__always_do_this()
        self.do_step_1()
        self.do_step_2()
        self.do_this_or()

    def __always_do_this(self):
        # This is a protected method that should not be overridden.

        name = inspect.currentframe().f_code.co_name
        print("{}.{}".format(self.__class__.__name__, name))

    @abstractmethod
    def do_step_1(self):
        """
        This method should be overridden
        :return:
        """

        print("do_step_1")

    @abstractmethod
    def do_step_2(self):
        """
        This method should be overridden
        :return:
        """
        print("do_step_2")

    def do_this_or(self):
        """

        :return:
        """
        print("You can override me but you do not have to")
        print(vars(self))


class ConcreteClassA(AbstractClass):
    """
    This class inherits from the Abstract class featuring the template method.
    """

    def do_step_1(self):
        print("Doing step 1 for ConcreteClassA ...")

    def do_step_2(self):
        print("Doing step 2 for ConcreteClassA ...")


class ConcreteClassB(AbstractClass):
    """
    This class inherits from the Abstract class featuring the template method.
    """

    def do_step_1(self):
        print("Doing step 1 for ConcreteClassB ...")

    def do_step_2(self):
        print("Doing step 2 for ConcreteClassB ...")

    def do_this_or(self):
        print("Doing my own business ...")


def main():
    """

    :return:
    """
    print("==ConcreteClassA==")
    a_instance = ConcreteClassA()
    a_instance.template_method()

    print("==ConcreteClassB==")
    b_instance = ConcreteClassB()
    b_instance.template_method()


if __name__ == "__main__":
    main()
