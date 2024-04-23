import streamlit as st
import  yfinance as yf
import pandas as pd
import plotly.graph_objs as go

import matplotlib.pyplot as plt
import seaborn as sns
import warnings

from scipy.stats import shapiro
import statsmodels.api as sm
import numpy as np

st.set_page_config(page_title="ALGO BACKTEST")


# Add elements to the sidebar
st.sidebar.title('Sidebar Title')
st.sidebar.header('Header')
st.sidebar.subheader('Subheader')
st.sidebar.text('Text')
st.sidebar.markdown('Markdown')
st.sidebar.checkbox('Checkbox')
st.sidebar.radio('Radio', ['Option 1', 'Option 2'])
st.sidebar.selectbox('Selectbox', ['Option 1', 'Option 2'])
st.sidebar.multiselect('Multiselect', ['Option 1', 'Option 2', 'Option 3'])
st.sidebar.slider('Slider', min_value=0, max_value=100)
st.sidebar.number_input('Number Input')
st.sidebar.text_input('Text Input')
st.sidebar.text_area('Text Area')
st.sidebar.date_input('Date Input')
st.sidebar.time_input('Time Input')
st.sidebar.file_uploader('File Uploader')
st.sidebar.color_picker('Color Picker')

warnings.filterwarnings("ignore")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("MEAN REVERSION")

st.write("Mean reversion is a financial theory that suggests that asset prices and returns tend to revert to their historical average over time. It is based on the idea that when prices deviate significantly from their average or mean, they are likely to move back towards that mean in the future. This phenomenon is observed in various financial markets and can be driven by a variety of factors.  Mean reversion is often attributed to the idea of market inefficiency. If markets were perfectly efficient, prices would always reflect all available information, and there would be no tendency for prices to revert to a mean.")
ticker = st.selectbox('Please pick a ticker', ['COKE', "MMM", "MNSO", 'OXM'])

data = pd.read_excel("DATA_"+ticker+".xlsx")

st.dataframe(data, use_container_width = True)

returns = data['Close'].pct_change().dropna()  # Calculate daily returns
plt.figure(figsize=(10, 6))
sns.distplot(returns, bins=150, color='blue', kde=True)
plt.title('Distribution of Daily Returns')
plt.xlabel('Daily Returns')
plt.ylabel('Frequency')
st.pyplot()

statistic, p_value = shapiro(returns)

alpha = 0.05
if p_value > alpha:
    st.text("The p value for the  Shaprio-Wilk Test: " + str(p_value))
    st.text("The data looks normally distributed (fail to reject H0)")
else:
    st.text("The p value for the  Shaprio-Wilk Test: " + str(p_value))
    st.text("The data does not look normally distributed (reject H0)")

def check_stationarity(data):
    # Perform stationarity test (e.g., Augmented Dickey-Fuller test)
    result = sm.tsa.adfuller(data)
    return result[1] < 0.05  # Check if p-value is less than 0.05

stationary = check_stationarity(returns)
st.text("Is the time series stationary?" + str(stationary))

# 2. Mean and Standard Deviation
mean_return = np.mean(returns)
std_return = np.std(returns)
st.text("Mean return:" + str(mean_return))
st.text("Standard deviation of return: " + str(std_return))
# 3. Autocorrelation
autocorr = np.correlate(returns, returns, mode='full')
st.text("Autocorrelation: ")

plt.figure(figsize=(10, 5))
plt.plot(autocorr, marker='o', linestyle='-', color='b')
plt.title('Autocorrelation of Returns')
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.grid(True)
plt.show()
st.pyplot()


# 4. Half-Life of Mean Reversion (example using exponential decay)
def half_life(data):
    lag = sm.tsa.acf(data, nlags=1)[1]
    return -np.log(2) / np.log(1 - lag)

hl_mean_reversion = half_life(returns)
st.text("Half-life of mean reversion:" + str(hl_mean_reversion))

# 5. Cointegration (not applicable to single asset)
# Skip for this example

# 6. Volatility (example using rolling standard deviation)
rolling_std = pd.Series(returns).rolling(window=10).std()
plt.plot(rolling_std)
plt.title("Rolling Standard Deviation (Volatility)")
plt.xlabel("Time")
plt.ylabel("Volatility")
st.pyplot()


std_input = st.text_input("PLease Enter The Standered Deviation level you want to execute ", "")
mean_input = st.text_input("PLease Enter The Mean window level you want to execute ", "")


if std_input != "" and mean_input != "":
    # Calculate rolling mean and standard deviation with a window of 10 days
    rolling_mean = data['Close'].rolling(window=10).mean()
    rolling_std = data['Close'].rolling(window=10).std()
    # Determine the thresholds for buy and short signals
    buy_threshold = rolling_mean - float(std_input)* rolling_std
    short_threshold = rolling_mean + float(std_input)  * rolling_std

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


            balance += profit_loss


            balance_over_time.append((date, balance))
            position = None

        elif close_price > short_thresh and position is None and balance > close_price:

            short_signals.append((date, close_price))
            # Short action

            price_executed = close_price
            balance_over_time.append((date, balance))
            position = 'short'

        elif close_price < mean and position == 'short':
            cover_signals.append((date, close_price))
            # Cover action

            profit_loss = price_executed - close_price

            balance += profit_loss  # Adjust balance with the profit/loss from covering the short
            

            balance_over_time.append((date, balance))
            position = None

    # Print final balance
    st.text(f"\nFinal Balance: {balance}")

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
    fig.update_layout(title=ticker +' Daily Stock Prices with Buy, Sell, Short, and Cover Signals',
                      xaxis_title='Date',
                      yaxis_title='Price')

    # Show the candlestick plot
    # fig.show()

    st.plotly_chart(fig)
    # Create a separate plot for balance over time
    balance_dates = [date[0] for date in balance_over_time]
    balance_values = [balance[1] for balance in balance_over_time]
    fig_balance = go.Figure(go.Scatter(x=balance_dates, y=balance_values, mode='lines', name='Balance Over Time', line=dict(color='purple', width=2)))
    fig_balance.update_layout(title='Balance Over Time',
                              xaxis_title='Date',
                              yaxis_title='Balance')
    # fig_balance.show()


    st.plotly_chart(fig_balance)