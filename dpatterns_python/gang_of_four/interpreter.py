"""
interpreter pattern in python
"""

from abc import abstractmethod


class AbstractExpression:
    """
    AbstractExpression
    """

    @abstractmethod
    def interpret(self):
        """
        interpret
        :return:
        """
        print("interpret")


class NonTerminalExpression(AbstractExpression):
    """
    NonTerminalExpression
    """

    def __init__(self, expression):
        self._expression = expression

    def interpret(self):
        print("Non-terminal expression being interpreted ...")
        self._expression.interpret()


class TerminalExpression(AbstractExpression):
    """
    TerminalExpression
    """

    def interpret(self):
        print("Terminal expression being interpreted ...")


def main():
    """

    :return:
    """
    ast = NonTerminalExpression(NonTerminalExpression(TerminalExpression()))
    ast.interpret()


if __name__ == "__main__":
    main()
