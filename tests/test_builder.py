from dpatterns_python.creational import builder


def test_get_car():
    skylark_builder = builder.SkyLarkBuilder()
    director = builder.Director(skylark_builder)
    director.construct_car()
    car = director.get_car()
    print(car)
