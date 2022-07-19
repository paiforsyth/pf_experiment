from pfhedge.instruments import BrownianStock, EuropeanOption
def simulate_european():
    n_paths = 10000
    stock = BrownianStock()
    option = EuropeanOption(stock)
    option.simulate(n_paths=n_paths)
    print(option.payoff().shape)


if __name__ =="__main__":
    simulate_european()