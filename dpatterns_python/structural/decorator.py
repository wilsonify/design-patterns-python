"""
decorator pattern in python
"""

from functools import wraps


def make_blink(function):
    """Defines the decorator"""

    # This makes the decorator transparent in terms of its name and docstring
    @wraps(function)
    # Define the inner function
    def decorator():
        # Grab the return value of the function being decorated
        ret = function()

        # Add new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"

    return decorator


# Apply the decorator here!
@make_blink
def hello_world():
    """Original function! """

    return "Hello, World!"


def main():
    """
    Check the result of decorating
    Check if the function name is still the same name of the function being decorated
    Check if the docstring is still the same as that of the function being decorated
    :return:
    """

    print(hello_world())
    print(hello_world.__name__)
    print(hello_world.__doc__)


if __name__ == "__main__":
    main()
