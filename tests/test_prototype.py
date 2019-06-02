from dpatterns_python import prototype as pt


def test_clone():
    c = pt.Car()
    prototype = pt.Prototype()
    prototype.register_object('skylark', c)
    c1 = prototype.clone('skylark')
    print(c1)
