from dpatterns_python import proxy


def test_produce():
    p = proxy.Proxy()

    p.produce()  # Make the proxy: Artist produce until Producer is available

    p.occupied = 'Yes'

    p.produce()
