from dpatterns_python import observer


def test_attach():
    c1 = observer.Core("Core 1")
    c2 = observer.Core("Core 2")

    v1 = observer.TempViewer()
    v2 = observer.TempViewer()

    c1.attach(v1)
    c1.attach(v2)

    c1.temp = 80
    c1.temp = 90
    c2.temp = 100
