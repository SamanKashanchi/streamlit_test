import streamlit as st
import  yfinance as yf
import pandas as pd
import plotly.graph_objs as go

import matplotlib.pyplot as plt
import warnings

from scipy.stats import shapiro
import statsmodels.api as sm
import numpy as np
import requests
from streamlit_lottie import st_lottie


# Load your profile picture
profile_pic = 'profile_pic.jpeg'  

# st.sidebar.image(profile_pic, caption='Your Name', use_column_width=True)
st.sidebar.image(profile_pic, caption='Saman Kashanchi', use_column_width=True)

def gradient(color1, color2, color3, content1, content2):
    # Create an HTML structure with styling for a gradient header
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};font-family:Calibri;">{content1}</span><br>'
                 f'<span style="color:white;font-size:14px;font-family:Calibri;">{content2}</span></h1>',
                unsafe_allow_html=True)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_gif = load_lottieurl("https://lottie.host/155bf63c-c86c-41c5-a157-6c07916e6cbc/sftMI66ekO.json")

with st.container():
    # Divide the container into two columns, with widths 8 and 3
    col1, col2 = st.columns([8, 3])

with col1:
    # Call the "gradient" function to display a gradient title
    gradient('#FF5733','#1B1464','e0fbfc',f"Algo Trading", 'Algorithmic trading is the practice of executing trades using computer programs grounded in strategies that typically rely on statistical methods for decision-making.')    
# Inside the second column (col2):
with col2:
    # Display a Lottie animation using the st_lottie function
    st_lottie(lottie_gif, height=280, key="data")


journey, backtest, optimization = st.tabs(["My Journey Into Algorithmic Trading", "Live Strategy BackTester", "Strategy Optimization"])

with journey:
    st.subheader("Where it all began")
    st.write("In the sophomore year of 2020, I was introduced to a friend in a data mining class who had recently switched from finance. He shared insights into financial markets and trading. That summer, many of us missed out on internship opportunities due to the outbreak of COVID-19. So, I decided to gather a group of friends from diverse backgrounds to work on a project together over the summer. The group consisted of computer scientists, mathematicians, and finance majors, totaling six people. Throughout the summer, we met for hours each week, delving into understanding the foreign exchange markets and devising strategies to capitalize on arbitrage opportunities arising from currency mispricing. After two months of countless backtests and learning from mistakes, we developed our very first trading strategies.")

with backtest:
    st.title("MEAN REVERSION")
    
    
    warnings.filterwarnings("ignore")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    st.write("Mean reversion is a financial theory that suggests that asset prices and returns tend to revert to their historical average over time. It is based on the idea that when prices deviate significantly from their average or mean, they are likely to move back towards that mean in the future. This phenomenon is observed in various financial markets and can be driven by a variety of factors.  Mean reversion is often attributed to the idea of market inefficiency. If markets were perfectly efficient, prices would always reflect all available information, and there would be no tendency for prices to revert to a mean.")
    ticker = st.selectbox('Please pick a ticker', ['COKE', "MMM", "MNSO", 'OXM'])
    
    data = pd.read_excel("DATA_"+ticker+".xlsx")
    
    st.dataframe(data, use_container_width = True)
    
    returns = data['Close'].pct_change().dropna()  # Calculate daily returns
    
    plt.figure(figsize=(10, 6))
    plt.hist(returns, bins=150, color='blue', density=True)
    plt.title('Distribution of Daily Returns')
    plt.xlabel('Daily Returns')
    plt.ylabel('Frequency')
    
    # Display the plot using Streamlit
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
