import streamlit as st


def select_asset():
    return st.text_input("Ticker (ex: AAPL, MSFT, BTC-USD)", value="AAPL").upper()



def select_period():
    return st.selectbox(
        "Période :",
        ["1mo", "3mo", "6mo", "1y", "5y", "max"],
        index=3,
    )


def select_interval():
    return st.selectbox(
        "Intervalle :",
        ["1d", "1h", "30m"],
        index=0,
    )


def select_strategy():
    return st.radio(
        "Stratégie :",
        ["Buy & Hold", "Momentum", "Mean Reversion"],
        index=0,
        horizontal=True,
    )


def momentum_period_slider(default: int = 3):
    return st.slider("Période de la moyenne mobile (jours) :", 3, 5, 100, default)
