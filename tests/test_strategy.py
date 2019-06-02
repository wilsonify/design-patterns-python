from dpatterns_python.behavioral import strategy


def test_execute():
    # Let's create our default strategy
    s0 = strategy.Strategy()
    # Let's execute our default strategy
    s0.execute()

    # Let's create the first varition of our default strategy by providing a new behavior
    s1 = strategy.Strategy(strategy.strategy_one)
    # Let's set its name
    s1.name = "Strategy One"
    # Let's execute the strategy
    s1.execute()

    s2 = strategy.Strategy(strategy.strategy_two)
    s2.name = "Strategy Two"
    s2.execute()
