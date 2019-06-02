"""
command pattern in python
"""


class Command:
    """
    Command
    """

    @staticmethod
    def execute():
        """
        execute
        :return:
        """
        print("execute")


class Copy(Command):
    """
    Copy
    """

    def execute(self):
        print("Copying ...")


class Paste(Command):
    """
    Paste
    """

    def execute(self):
        print("Pasting ...")


class Save(Command):
    """
    Save
    """

    def execute(self):
        print("Saving ...")


class Macro:
    """
    Macro
    """

    def __init__(self):
        self.commands = []

    def add(self, command):
        """
        add
        :param command:
        :return:
        """
        self.commands.append(command)

    def run(self):
        """
        run
        :return:
        """
        for command in self.commands:
            command.execute()


def main():
    """

    :return:
    """
    macro = Macro()
    macro.add(Copy())
    macro.add(Paste())
    macro.add(Save())
    macro.run()


if __name__ == "__main__":
    main()
