import plotly.express as px
import pandas as pd

from experiments.bsm_hedge import simulate_european_bsm
from experiments.no_hedge import simulate_european_no_hedge

payoff_name = "payoff"

hedging_column = "hedging"


def make_hedging_comparison(n_paths: int=10000) -> pd.DataFrame:
    no_hedging_name = "None"
    bsm_hedging_name ="Black-Scholes-Merton"
    no_hedge = pd.DataFrame(simulate_european_no_hedge(n_paths=n_paths).numpy(), columns=[payoff_name])
    bsm_hedge = pd.DataFrame(simulate_european_bsm(n_paths=n_paths).numpy(), columns=[payoff_name])
    no_hedge[hedging_column]=no_hedging_name
    bsm_hedge[hedging_column] = bsm_hedging_name
    df = pd.concat([no_hedge, bsm_hedge], axis=0)
    return df

def plot_hedging_comparison():
    df = make_hedging_comparison(
    )
    n_bins=100
    fig = px.histogram(df , histnorm='probability density', x=payoff_name,range_x=[-0.2,0], nbins=n_bins, color=hedging_column)
    fig.update_xaxes(dict(title_font_size=40))
    fig.update_yaxes(dict(title_font_size=40))
    fig.update_xaxes(dict(title_font_size=font_size, tickfont=dict(size=tick_font_size)))
    fig.update_yaxes(dict(title_font_size=font_size))
    fig.show()

if __name__ == "__main__":
    plot_hedging_comparison()
