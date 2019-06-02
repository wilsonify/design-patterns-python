"""
memento pattern in python
"""

import pickle


class Originator:
    """
    Originator
    """

    state = None

    def __init__(self):
        pass

    def create_memento(self):
        """

        :return:
        """
        return pickle.dumps(vars(self))

    def set_memento(self, memento):
        """

        :param memento:
        :return:
        """
        previous_state = pickle.loads(memento)
        vars(self).update(previous_state)


def main():
    """

    :return:
    """
    originator = Originator()

    print(vars(originator))

    memento = originator.create_memento()

    originator.state = True

    print(vars(originator))

    originator.set_memento(memento)

    print(vars(originator))


if __name__ == "__main__":
    main()
