class SubsystemA:
    @staticmethod
    def method1():
        print('SubsystemA method1 ...')

    @staticmethod
    def method2():
        print('SubsystemA method2 ...')


class SubsystemB:

    @staticmethod
    def method1():
        print('SubsystemB method1 ...')

    @staticmethod
    def method2():
        print('SubsystemB method2 ...')


class Facade:

    def __init__(self):
        self._subsystem_A = SubsystemA()
        self._subsystem_B = SubsystemB()

    def method(self):
        self._subsystem_A.method1()
        self._subsystem_A.method2()

        self._subsystem_B.method1()
        self._subsystem_B.method2()


def main():
    facade = Facade()
    facade.method()


if __name__ == "__main__":
    main()
