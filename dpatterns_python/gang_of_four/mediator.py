"""
mediator pattern in python
"""


class Colleague:
    """
    Colleague
    """

    def __init__(self, mediator, identity):
        self._mediator = mediator
        self._id = identity

    def get_id(self):
        """
        get_id
        :return:
        """
        return self._id

    @staticmethod
    def send(msg):
        """
        send
        :param msg:
        :return:
        """
        print("send")
        print("msg = {}".format(msg))

    @staticmethod
    def receive(msg):
        """
        receive
        :param msg:
        :return:
        """
        print("receive")
        print("msg = {}".format(msg))


class ConcreteColleague(Colleague):
    """
    ConcreteColleague
    """

    def __init__(self, mediator, identity):
        print("initializing ConcreteColleague")
        super().__init__(mediator, identity)

    def send(self, msg):
        print("Message '" + msg + "' sent by Colleague " + str(self._id))
        self._mediator.distribute(self, msg)

    def receive(self, msg):
        print("Message '" + msg + "' received by Colleague " + str(self._id))


class Mediator:
    """
    Mediator
    """

    @staticmethod
    def add(colleague):
        """

        :param colleague:
        :return:
        """
        print("add")
        print("colleague = {}".format(colleague))

    @staticmethod
    def distribute(sender, msg):
        """

        :param sender:
        :param msg:
        :return:
        """
        print("distribute")
        print("sender = {}".format(sender))
        print("msg = {}".format(msg))


class ConcreteMediator(Mediator):
    """
    ConcreteMediator
    """

    def __init__(self):
        Mediator.__init__(self)
        self._colleague = []

    def add(self, colleague):
        self._colleague.append(colleague)

    def distribute(self, sender, msg):
        for colleague in self._colleague:
            if colleague.get_id() != sender.get_id():
                colleague.receive(msg)


def main():
    """

    :return:
    """
    mediator = ConcreteMediator()

    colleague1 = ConcreteColleague(mediator, 1)
    colleague2 = ConcreteColleague(mediator, 2)
    colleague3 = ConcreteColleague(mediator, 3)

    mediator.add(colleague1)
    mediator.add(colleague2)
    mediator.add(colleague3)

    colleague1.send("Good Morning!")


if __name__ == "__main__":
    main()
