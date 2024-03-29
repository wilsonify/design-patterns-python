"""
iterator pattern in python
"""


def count_to(count):
    """Our iterator implementation"""

    # Our list
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

    # Our built-in iterator
    # Creates a tuple such as (1, "eins")
    iterator = zip(range(count), numbers_in_german)

    # Iterate through our iterable list
    # Extract the German numbers
    # Put them in a generator called number
    for _, number in iterator:
        # Returns a 'generator' containing numbers in German
        yield number


def main():
    """
    Let's test the generator returned by our iterator
    :return:
    """

    for num in count_to(3):
        print("{}".format(num))

    for num in count_to(4):
        print("{}".format(num))


if __name__ == "__main__":
    main()
