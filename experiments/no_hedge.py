from pfhedge.instruments import BrownianStock, EuropeanOption
def simulate_european():
    n_paths = 100000
    stock = BrownianStock()
    option = EuropeanOption(stock)
    result = option.simulate(n_paths=n_paths)