import plotly.graph_objects as go
import pandas as pd


def price_and_strategy_chart(
    df_price: pd.DataFrame,
    strategy_series: pd.Series | None = None,
    title: str = "Prix et stratégie",
):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df_price.index,
            y=df_price["price"],
            name="Prix",
            mode="lines",
        )
    )

    if strategy_series is not None:
        initial_price = df_price["price"].iloc[0]

        strat_scaled = (
            strategy_series
            .reindex(df_price.index, method="ffill")
            * initial_price
        )

        fig.add_trace(
            go.Scatter(
                x=df_price.index,
                y=strat_scaled,
                name="Stratégie (échelle prix)",
                mode="lines",
            )
        )

    fig.update_layout(title=title, xaxis_title="Date", yaxis_title="Valeur")
    return fig
