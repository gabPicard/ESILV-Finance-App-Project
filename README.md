# PGLFF---Project  
(The website doesn't work on the campus Wi-FI)   
## Single Asset Analysis (Quant A)

This part focuses on the univariate analysis of financial assets. It allows users to visualize historical data, backtest trading strategies, and evaluate performance metrics in real-time.

### Key Features
 **Data Ingestion**: The `get_history` module fetches raw market data via `yfinance`. It specifically processes the **Close price**, handling MultiIndex formatting to ensure a clean time-series structure labeled as `price`.
 **Automatic Refresh**: The dashboard updates automatically every **5 minutes** to capture the latest market movements.
 **Interactive Controls**: Users can customize the analysis via the sidebar:
 **Asset Selection**: Choose from a predefined list of tickers.
 **Timeframe**: Select period (e.g., 1y, 5y) and interval (e.g., 1d, 1h).
 **Strategy Parameters**: Dynamic parameter tuning (e.g., Moving Average window size).

### Implemented Strategies
The module supports backtesting for three distinct strategies:
1.  **Buy & Hold**: Normalizes the asset price series to track the cumulative return of a long position from the start date.(See file: src/strategies/buy_and_hold.py)  

2.  **Momentum**: A trend-following strategy using Moving Averages.(See file: src/strategies/momentum.py)

3.  **Mean Reversion**: A counter-trend strategy based on price deviation from a moving average. (See file: src/strategies/mean_reversion.py)  

    

### Performance Metrics
The backtesting engine (`src.evaluation.backtesting`) calculates key indicators based on the strategy's equity curve:
**Total Return**: Overall percentage gain or loss.
**Annualized Volatility**: Standard deviation of returns scaled to a yearly basis.
**Sharpe Ratio**: Risk-adjusted return metric.
**Max Drawdown**: The maximum observed loss from a peak to a trough.

### Visualizations
**Main Chart**: An interactive Plotly graph overlaying the raw asset price and the strategy's equity curve.
**Raw Data**: An expandable view of the underlying dataframe showing Date and Price.



##  Multi-Asset Portfolio (Quant B)

This module extends the platform to multivariate analysis, allowing users to construct, simulate, and analyze a portfolio composed of multiple financial assets. It is designed to evaluate how diversification and rebalancing strategies impact overall performance.

### Key Features & Workflow
**Dynamic Asset Selection**: Users can input a custom list of tickers (e.g., AAPL, MSFT, GLD) to construct a portfolio of at least three assets. The system validates tickers in real-time, filtering out invalid inputs, and fetches historical data for the selected period.

**Live Market Data**: Similar to the single-asset module, this page automatically refreshes every 5 minutes to display the latest prices and daily variations for all portfolio components.

**Custom Allocation & Normalization**: The dashboard provides interactive sliders to assign specific weights to each asset. The system automatically normalizes these inputs to ensure the total allocation always equals 100%. If all weights are set to zero, an equal-weight distribution is applied by default. (`src/portfolio/weights.py`)  

**Rebalancing Strategies**: Users can define how the portfolio is managed over time by selecting a rebalancing frequency. Options include "Daily" (constant weights), "Monthly", "Quarterly", or "None" (Buy and Hold).

### Performance Analysis & Visualization
**Comparative Charting (Base 100)**: The main visualization overlays the normalized performance of the entire portfolio against each individual asset. This "Base 100" approach allows for an instant visual comparison of relative growth regardless of the raw price differences.

**Risk/Return Metrics**: A detailed statistics table reports the portfolio's Annual Return, Annual Volatility, Sharpe Ratio, and Max Drawdown, providing a comprehensive view of risk-adjusted performance.(`src/portfolio/portfolio_engine.py`)  

**Diversification Analysis**: A dedicated section quantifies the benefits of diversification. It calculates the "Volatility Reduction" by comparing the weighted average volatility of individual assets against the actual volatility of the portfolio.

**Correlation Matrix**: Shows the relationships between assets, the module generates a color-coded correlation heatmap.(`src/portfolio/correlations.py`)  

##  Settings & Configuration

This module acts as the control center for the application, providing a graphical interface to manage global parameters and persistent data without modifying the source code. It relies on a YAML-based configuration system to ensure that user preferences are saved and reloaded automatically upon every launch.

### Key Features & Workflow
**Centralized Configuration Management**: The application loads and writes to a local `config.yaml` file. This persistence layer ensures that any changes made to asset lists or parameters are saved for future sessions.  

**Asset List Management**: The interface is divided into specific tabs to manage different groups of financial assets:
     **Report Assets**: Users can add or remove the specific tickers that are processed in the automated daily cron report.
     **Portfolio Assets & Defaults**: Allows the customization of the default tickers that appear when opening the Portfolio Analysis page, streamlining the user experience.  

**Report Parameters**: A dedicated settings tab enables users to define the temporal scope of the analysis. Users can adjust the historical lookback period (e.g., "1 Year", "YTD") and the data interval (e.g., "1 Day", "1 Hour") used for data fetching.  

**Live Validation & Feedback**: The system provides immediate visual feedback (success messages or warnings) when adding or deleting items. It filters inputs to ensure tickers are formatted correctly (uppercase, stripped of spaces) before saving.  

**Transparency**: A "View Full Configuration" expander allows advanced users to inspect the raw YAML data structure directly within the dashboard to verify the current state of the application.  

