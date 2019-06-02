from dpatterns_python.structural import decorator


def test_hello_world():
    print(decorator.hello_world())

    print(decorator.hello_world.__name__)

    print(decorator.hello_world.__doc__)
