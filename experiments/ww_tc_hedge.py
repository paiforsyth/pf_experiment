import pandas as pd
from pfhedge import Hedger
from pfhedge.instruments import BrownianStock, EuropeanOption
import plotly.express as px
from pfhedge.nn import BlackScholes, WhalleyWilmott
import torch


def simulate_european_bsm(n_paths: int=10000, steps: int=10000, cost: float = 0.01, risk_aversion: float=1):
    torch.manual_seed(42)
    stock = BrownianStock(dt=1/steps,cost=cost)
    option = EuropeanOption(stock,strike=1.0,call=False,)
    option.simulate(n_paths=n_paths)
    model = WhalleyWilmott(option, a=risk_aversion)
    hedger = Hedger(model=model, inputs=model.inputs())
    result = hedger.compute_pl(derivative=option)
    short_result = result
    return short_result


def get

def plot_european_bsm(n_paths:int=10000):
    payoff_name = "payoff"
    n_bins = 100
    font_size=60
    tick_font_size = 30
    short_result = simulate_european_bsm(n_paths=n_paths)
    df = pd.DataFrame(short_result.numpy(), columns=[payoff_name])
    fig = px.histogram(df , histnorm='probability density', x=payoff_name,range_x=[-0.2,0], nbins=n_bins)
    fig.update_xaxes(dict(title_font_size=font_size, tickfont=dict(size=tick_font_size)))
    fig.update_yaxes(dict(title_font_size=font_size))
    fig.show()

if __name__ =="__main__":
    plot_european_bsm()

