"""
facade pattern in python
"""


class SubsystemA:
    """
    SubsystemA
    """

    @staticmethod
    def method1():
        """
        method1
        :return:
        """
        print("SubsystemA method1 ...")

    @staticmethod
    def method2():
        """
        method2
        :return:
        """
        print("SubsystemA method2 ...")


class SubsystemB:
    """
    SubsystemB
    """

    @staticmethod
    def method1():
        """
        method1
        :return:
        """
        print("SubsystemB method1 ...")

    @staticmethod
    def method2():
        """
        method2
        :return:
        """
        print("SubsystemB method2 ...")


class Facade:
    """
    Facade
    """

    def __init__(self):
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()

    def method(self):
        """

        :return:
        """
        self._subsystem_a.method1()
        self._subsystem_a.method2()

        self._subsystem_b.method1()
        self._subsystem_b.method2()


def main():
    """

    :return:
    """
    facade = Facade()
    facade.method()


if __name__ == "__main__":
    main()
