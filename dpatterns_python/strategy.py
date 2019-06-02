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


# Let's create our default strategy
S0 = Strategy()
# Let's execute our default strategy
S0.execute()  # pylint: disable= not-callable

# Let's create the first variation of our default strategy by providing a new behavior
S1 = Strategy(strategy_one)
# Let's set its name
S1.name = "Strategy One"
# Let's execute the strategy
S1.execute()  # pylint: disable= not-callable

S2 = Strategy(strategy_two)
S2.name = "Strategy Two"
S2.execute()  # pylint: disable= not-callable
