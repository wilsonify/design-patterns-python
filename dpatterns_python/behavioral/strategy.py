"""
strategy pattern in python
"""
from types import MethodType


class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, function):
        self.name = "Default Strategy"
        self.execute = MethodType(function, self)


def strategy_one(self):
    """
    # Replacement method 1
    :param self:
    :return:
    """
    self.name = "Strategy One"
    print("{} is used to execute method 1".format(self.name))


def strategy_two(self):
    """
    # Replacement method 2
    :param self:
    :return:
    """
    self.name = "Strategy Two"
    print("{} is used to execute method 2".format(self.name))


def strategy_three(self):
    """
    # Replacement method 3
    :param self:
    :return:
    """
    self.name = "Strategy Three"
    print("{} is used to execute method 2".format(self.name))


def main():
    """
    Let's create our default strategy
    Let's execute our default strategy
    Let's create the first variation of our default strategy by providing a new behavior
    Let's set its name
    Let's execute the strategy
    :return:
    """

    strategy1 = Strategy(strategy_one)
    strategy1.execute()  # pylint: disable=not-callable

    strategy2 = Strategy(strategy_two)
    strategy2.execute()  # pylint: disable=not-callable

    strategy3 = Strategy(strategy_three)
    strategy3.execute()  # pylint: disable=not-callable


if __name__ == "__main__":
    main()
