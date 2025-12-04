import pandas as pd

def run_mean_reversion(df: pd.DataFrame, period: int = 20, threshold: float = 0.02) -> pd.Series:
    df = df.copy()

    df["ma"] = df["price"].rolling(period).mean()
    df["diff"] = (df["price"] - df["ma"]) / df["ma"]

    df["signal"] = (df["diff"] < -threshold).astype(int)

    df["returns"] = df["price"].pct_change().fillna(0)
    df["strategy_ret"] = df["signal"].shift(1).fillna(0) * df["returns"]

    df["strategy_value"] = (1 + df["strategy_ret"]).cumprod()
    df["strategy_value"].fillna(1.0, inplace=True)
    df["strategy_value"].name = f"MeanReversion_{period}"

    return df["strategy_value"]
