import streamlit as st
import  yfinance as yf
import pandas as pd
import plotly.graph_objs as go

st.set_page_config(page_title="ALGO BACKTEST", layout= "wide")

st.text("HELLO")

data = pd.read_excel("DATA_MMM.xlsx")

st.dataframe(data)

# Calculate rolling mean and standard deviation with a window of 10 days
rolling_mean = data['Close'].rolling(window=10).mean()
rolling_std = data['Close'].rolling(window=10).std()
# Determine the thresholds for buy and short signals
buy_threshold = rolling_mean - 1.5 * rolling_std
short_threshold = rolling_mean + 1.5 * rolling_std

# # Initialize variables
balance = 10000  # Starting balance
position = None
buy_signals = []
sell_signals = []
short_signals = []
cover_signals = []
balance_over_time = []  # To store balance over time
balance_over_time.append((data['Date'][0], balance))

# Loop through the data to identify buy, sell, short, and cover signals
for date, close_price, mean, buy_thresh, short_thresh in zip(data['Date'], data['Close'], rolling_mean, buy_threshold, short_threshold):
    if close_price < buy_thresh and position is None and balance > close_price:

        buy_signals.append((date, close_price))
        # Buy action

        price_executed = close_price
        balance_over_time.append((date , balance))
        position = 'long'

    elif close_price > mean and position == 'long':

        sell_signals.append((date, close_price))
        # Sell action

        profit_loss = close_price -  price_executed
        st.text(balance)

        st.text(profit_loss)

        balance += profit_loss

        st.text(balance)

        balance_over_time.append((date, balance))
        position = None

    # elif close_price > short_thresh and position is None and balance > close_price:

    #     short_signals.append((date, close_price))
    #     # Short action

    #     price_executed = close_price
    #     balance -= close_price
    #     balance_over_time.append((date, balance))
    #     position = 'short'

    # elif close_price < mean and position == 'short':
    #     cover_signals.append((date, close_price))
    #     # Cover action

    #     profit_loss = price_executed - close_price
    #     balance += profit_loss  # Adjust balance with the profit/loss from covering the short
    #     balance_over_time.append((date, balance))
    #     position = None

# Print final balance
print(f"\nFinal Balance: {balance}")

# Create a candlestick chart
fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                                     open=data['Open'],
                                     high=data['High'],
                                     low=data['Low'],
                                     close=data['Close'])])

# Plot buy signals
for date, price in buy_signals:
    fig.add_trace(go.Scatter(x=[date], y=[price], mode='markers', name='Buy Signal', marker=dict(color='green', size=10)))
    fig.add_annotation(x=date, y=price, text=f'Buy at ${price:.2f}', showarrow=True, arrowhead=1, arrowcolor='green')

# Plot sell signals
for date, price in sell_signals:
    fig.add_trace(go.Scatter(x=[date], y=[price], mode='markers', name='Sell Signal', marker=dict(color='red', size=10)))
    fig.add_annotation(x=date, y=price, text=f'Sell at ${price:.2f}', showarrow=True, arrowhead=1, arrowcolor='red')

# Plot short signals
for date, price in short_signals:
    fig.add_trace(go.Scatter(x=[date], y=[price], mode='markers', name='Short Signal', marker=dict(color='blue', size=10)))
    fig.add_annotation(x=date, y=price, text=f'Short at ${price:.2f}', showarrow=True, arrowhead=1, arrowcolor='blue')

# Plot cover signals
for date, price in cover_signals:
    fig.add_trace(go.Scatter(x=[date], y=[price], mode='markers', name='Cover Signal', marker=dict(color='orange', size=10)))
    fig.add_annotation(x=date, y=price, text=f'Cover at ${price:.2f}', showarrow=True, arrowhead=1, arrowcolor='orange')

# Add the rolling mean to the plot
# fig.add_trace(go.Scatter(x=rolling_mean["Date"], y=rolling_mean, mode='lines', name='6-Month Rolling Mean'))

# Customize layout
fig.update_layout(title='MMM Daily Stock Prices with Buy, Sell, Short, and Cover Signals',
                  xaxis_title='Date',
                  yaxis_title='Price')

# Show the candlestick plot
# fig.show()

st.plotly_chart(fig,  use_container_width=True)

# Create a separate plot for balance over time
balance_dates = [date[0] for date in balance_over_time]
balance_values = [balance[1] for balance in balance_over_time]
fig_balance = go.Figure(go.Scatter(x=balance_dates, y=balance_values, mode='lines', name='Balance Over Time', line=dict(color='purple', width=2)))
fig_balance.update_layout(title='Balance Over Time',
                          xaxis_title='Date',
                          yaxis_title='Balance')
# fig_balance.show()


st.plotly_chart(fig_balance,  use_container_width=True)