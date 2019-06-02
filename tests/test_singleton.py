from dpatterns_python import singleton


def test_singleton():
    # Let's create a singleton object and add our first acronym
    x = singleton.Singleton(HTTP="Hyper Text Transfer Protocol")
    # Print the object
    print(x)

    # Let's create another singleton object and if it refers to the same attribute dictionary by adding another acronym.
    y = singleton.Singleton(SNMP="Simple Network Management Protocol")
    # Print the object
    print(y)
