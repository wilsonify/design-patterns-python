from dpatterns_python.behavioral import chain


def test_delegate():
    c = chain.Client()
    requests_list = [2, 5, 30]
    c.delegate(requests_list)
