import streamlit as st
import  yfinance as yf
# import plotly.graph_objs as go


st.text("HELLO")

# st.set_page_config(page_title="ALGO BACKTEST", layout= "wide")


# # Fetch daily price data from Yahoo Finance
# data = yf.download('MMM', start='2023-01-01', end='2024-04-01')

# # Calculate rolling mean and standard deviation with a window of 10 days
# rolling_mean = data['Close'].rolling(window=10).mean()
# rolling_std = data['Close'].rolling(window=10).std()
# # Determine the thresholds for buy and short signals
# buy_threshold = rolling_mean - 1.5 * rolling_std
# short_threshold = rolling_mean + 1.5 * rolling_std

# # Initialize variables
# balance = 10000  # Starting balance
# position = None
# buy_signals = []
# sell_signals = []
# short_signals = []
# cover_signals = []
# transactions = []  # To store transaction details
# balance_over_time = []  # To store balance over time

# # Loop through the data to identify buy, sell, short, and cover signals
# for date, close_price, mean, buy_thresh, short_thresh in zip(data.index, data['Close'], rolling_mean, buy_threshold, short_threshold):
#     if close_price < buy_thresh and position is None and balance > 0:
#         buy_signals.append((date, close_price))
#         position = 'long'
#         # Buy action
#         transaction_cost = close_price
#         balance -= transaction_cost
#         transactions.append(('Buy', date, close_price, transaction_cost))
#     elif close_price > mean and position == 'long':
#         sell_signals.append((date, close_price))
#         # Sell action
#         revenue = close_price
#         profit_loss = revenue - transaction_cost
#         balance += revenue
#         transactions.append(('Sell', date, close_price, revenue, profit_loss))
#         position = None
#         balance_over_time.append((date, balance))
#     elif close_price > short_thresh and position is None and balance > 0:
#         short_signals.append((date, close_price))
#         position = 'short'
#         # Short action
#         transaction_cost = close_price
#         balance += transaction_cost
#         transactions.append(('Short', date, close_price, transaction_cost))
#     elif close_price < mean and position == 'short':
#         cover_signals.append((date, close_price))
#         # Cover action
#         revenue = close_price
#         profit_loss = transaction_cost - revenue
#         balance += profit_loss  # Adjust balance with the profit/loss from covering the short
#         transactions.append(('Cover', date, close_price, revenue, profit_loss))
#         position = None
#         balance_over_time.append((date, balance))

# # Print transaction details
# print("Transaction Details:")
# for transaction in transactions:
#     if len(transaction) >= 5:
#         print(f"{transaction[0]} at {transaction[1]} - Price: {transaction[2]}, Amount: {transaction[3]}, Profit/Loss: {transaction[4] if transaction[4] else 'N/A'}")
#     else:
#         print(f"{transaction[0]} at {transaction[1]} - Price: {transaction[2]}, Amount: {transaction[3]}")

# # Print final balance
# print(f"\nFinal Balance: {balance}")

# # Create a candlestick chart
# fig = go.Figure(data=[go.Candlestick(x=data.index,
#                                      open=data['Open'],
#                                      high=data['High'],
#                                      low=data['Low'],
#                                      close=data['Close'])])

# # Plot buy signals
# for date, price in buy_signals:
#     fig.add_trace(go.Scatter(x=[date], y=[price], mode='markers', name='Buy Signal', marker=dict(color='green', size=10)))
#     fig.add_annotation(x=date, y=price, text=f'Buy at ${price:.2f}', showarrow=True, arrowhead=1, arrowcolor='green')

# # Plot sell signals
# for date, price in sell_signals:
#     fig.add_trace(go.Scatter(x=[date], y=[price], mode='markers', name='Sell Signal', marker=dict(color='red', size=10)))
#     fig.add_annotation(x=date, y=price, text=f'Sell at ${price:.2f}', showarrow=True, arrowhead=1, arrowcolor='red')

# # Plot short signals
# for date, price in short_signals:
#     fig.add_trace(go.Scatter(x=[date], y=[price], mode='markers', name='Short Signal', marker=dict(color='blue', size=10)))
#     fig.add_annotation(x=date, y=price, text=f'Short at ${price:.2f}', showarrow=True, arrowhead=1, arrowcolor='blue')

# # Plot cover signals
# for date, price in cover_signals:
#     fig.add_trace(go.Scatter(x=[date], y=[price], mode='markers', name='Cover Signal', marker=dict(color='orange', size=10)))
#     fig.add_annotation(x=date, y=price, text=f'Cover at ${price:.2f}', showarrow=True, arrowhead=1, arrowcolor='orange')

# # Add the rolling mean to the plot
# fig.add_trace(go.Scatter(x=rolling_mean.index, y=rolling_mean, mode='lines', name='6-Month Rolling Mean'))

# # Customize layout
# fig.update_layout(title='MMM Daily Stock Prices with Buy, Sell, Short, and Cover Signals',
#                   xaxis_title='Date',
#                   yaxis_title='Price')

# # Show the candlestick plot
# # fig.show()

# st.plotly_chart(fig,  use_container_width=True)

# # Create a separate plot for balance over time
# balance_dates = [date[0] for date in balance_over_time]
# balance_values = [balance[1] for balance in balance_over_time]
# fig_balance = go.Figure(go.Scatter(x=balance_dates, y=balance_values, mode='lines', name='Balance Over Time', line=dict(color='purple', width=2)))
# fig_balance.update_layout(title='Balance Over Time',
#                           xaxis_title='Date',
#                           yaxis_title='Balance')
# # fig_balance.show()


# st.plotly_chart(fig_balance,  use_container_width=True)