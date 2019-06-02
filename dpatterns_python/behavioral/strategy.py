"""
strategy pattern in python
"""
import types


class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, function=None):
        self.name = "Default Strategy"

        # If a reference to a function is provided, replace the execute() method with the given function
        if function:
            self.execute = types.MethodType(function, self)

    # pylint: disable=method-hidden
    def execute(self):
        """
        # This gets replaced by another version if another strategy is provided.
        The default method that prints the name of the strategy being used
        :return:
        """
        print("{} is used!".format(self.name))


# Replacement method 1
def strategy_one(self):
    """

    :param self:
    :return:
    """
    print("{} is used to execute method 1".format(self.name))


# Replacement method 2
def strategy_two(self):
    """

    :param self:
    :return:
    """
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

    strategy0 = Strategy()

    strategy0.execute()  # pylint: disable= not-callable

    strategy1 = Strategy(strategy_one)
    strategy1.name = "Strategy One"
    strategy1.execute()  # pylint: disable= not-callable

    strategy2 = Strategy(strategy_two)
    strategy2.name = "Strategy Two"
    strategy2.execute()  # pylint: disable= not-callable


if __name__ == "__main__":
    main()
