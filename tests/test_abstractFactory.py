from dpatterns_python import abstract_factory


def test_show_pet():
    factory = abstract_factory.DogFactory()
    shop = abstract_factory.PetStore(factory)
    shop.show_pet()
