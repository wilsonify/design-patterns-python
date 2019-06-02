"""
state pattern in python
"""


class AtmState:
    """
    AtmState
    """

    name = "state"
    allowed = []

    def go_next(self, state):
        """
        switch state
        :param state:
        :return:
        """
        if state.name in self.allowed:
            print("Current State: ", self, " switched to: ", state.name)
            self.__class__ = state

        else:
            print(
                "Current State: ", self, " switching to: ", state.name, " not possible!"
            )

    def __str__(self):
        return self.name


class Off(AtmState):
    """
    turn it off
    """

    name = "off"
    allowed = ["on"]


class On(AtmState):
    """
    turn it on
    """

    name = "on"
    allowed = ["off"]


class ATM:
    """
    ATM
    """

    def __init__(self):
        self.current = Off()

    def set_state(self, state):
        """

        :param state:
        :return:
        """
        self.current.go_next(state)


def main():
    """

    :return:
    """
    atm = ATM()

    atm.set_state(On)
    atm.set_state(Off)
    atm.set_state(Off)


if __name__ == "__main__":
    main()
