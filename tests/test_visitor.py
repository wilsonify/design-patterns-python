from dpatterns_python.behavioral import visitor


def test_accept():
    # Create an HVAC specialist
    hv = visitor.HvacSpecialist()
    # Create an electrician
    e = visitor.Electrician()

    # Create a house
    home = visitor.House()

    # Let the house accept the HVAC specialist and work on the house by invoking the visit() method
    home.accept(hv)

    # Let the house accept the electrician and work on the house by invoking the visit() method
    home.accept(e)
