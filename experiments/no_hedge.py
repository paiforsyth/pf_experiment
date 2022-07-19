import pandas as pd
import torch
from pfhedge.instruments import BrownianStock, EuropeanOption
import plotly.express as px
def simulate_european_no_hedge(n_paths: int=10000):
    torch.manual_seed(42)
    stock = BrownianStock()
    option = EuropeanOption(stock,strike=1.0,call=False)
    option.simulate(n_paths=n_paths)
    result =option.payoff()
    short_result = -result
    return short_result

def plot_european_no_hedge(n_paths: int=100000):
    n_bins = 200
    tick_font_size = 20
    font_size = 60
    payoff_name = "payoff"
    short_result = simulate_european_no_hedge(n_paths)
    df = pd.DataFrame(short_result.numpy(), columns=[payoff_name])
    fig = px.histogram(df , histnorm='probability density', x=payoff_name,range_x=[-0.2,0], nbins=n_bins)
    fig.update_xaxes(dict(title_font_size=font_size, tickfont=dict(size=tick_font_size)))
    fig.update_yaxes(dict(title_font_size=font_size), tickfont=dict(size=tick_font_size))
    fig.show()


if __name__ =="__main__":
    plot_european_no_hedge()