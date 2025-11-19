import pandas as pd
import numpy as np

def sharpe(series):
    returns = series.pct_change().dropna()
    return (returns.mean() / returns.std()) * np.sqrt(252)

def max_drawdown(series):
    roll_max = series.cummax()
    drawdown = (series - roll_max) / roll_max
    return drawdown.min()
