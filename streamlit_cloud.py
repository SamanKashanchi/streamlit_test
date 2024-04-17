import streamlit as st
from moviepy.editor import VideoFileClip
import os
import tempfile
import base64
import uuid
import yfinance as yf
import plotly.graph_objs as go

st.set_page_config(
    page_title="Saman Portfolio",
    page_icon="chart_with_upwards_trend"
)

st.title("Short Video Editor 🎬")


   
def get_binary_file_downloader_html(file_path, file_label):
    with open(file_path, 'rb') as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    href = f'data:video/mp4;base64,{b64}'
    return f'<a href="{href}" download="{file_label}">Download url {file_label}</a>'


def split_video_into_chunks(video_path, chunk_duration):


    clip = VideoFileClip(video_path)
    total_duration = clip.duration
    chunks = []
    for i in range(0, int(total_duration), int(chunk_duration)):
        start_time = i
        end_time = min(i + int(chunk_duration), total_duration)
        chunk = clip.subclip(start_time, end_time)
        chunks.append(chunk)
    return chunks


def get_frames(video_path, output_folder, num_frames):

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_folder_path = os.path.join(desktop_path, output_folder)


    st.text(output_folder_path)



    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
        st.text("Made directory")

    clip = VideoFileClip(video_path)

    duration = clip.duration

    interval = duration / num_frames

    for i in range(num_frames):
        t = i * interval
        frame_filename = os.path.join(output_folder_path, f"frame_{i+1:05d}.jpg")

        st.text(frame_filename)
        clip.save_frame(frame_filename, t)
        st.text(f"Saved frame {i+1} at time {t:.2f} seconds")

    st.text("Frames extraction completed.")


st.markdown("---")


st.subheader("Video Splitter")


chunk_size = st.text_input("How many seconds do you want each chunk to be: ")
uploaded_file = st.file_uploader("Upload a video and split into customizbale chunks: ", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    st.video(uploaded_file)

    if st.button("Split Video into Chunks"):


        file_content = uploaded_file.getvalue()
          

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
            temp_file.write(file_content)
            file_name = uploaded_file.name
            temp_file_path = temp_file.name

            # st.markdown(get_binary_file_downloader_html(temp_file.name, file_name), unsafe_allow_html=True)


            # Split the video into chunks
            video_chunks = split_video_into_chunks(temp_file_path, chunk_size)

            # Provide download links for each chunk
            for i, chunk in enumerate(video_chunks):
                chunk_file_path = f"{temp_file_path}_chunk_{i}.mp4"
                chunk.write_videofile(chunk_file_path, codec="libx264", fps=24, audio_codec="aac")

                st.text(f"Link for Video {i}: ")
                st.markdown(get_binary_file_downloader_html(chunk_file_path, f"{file_name}_chunk_{i}.mp4"), unsafe_allow_html=True)


st.subheader("Make Image data set")

uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    # Save the uploaded video to a temporary location
    with st.spinner("Saving uploaded video..."):
        temp_video_path = os.path.join("/tmp", uploaded_file.name)
        with open(temp_video_path, "wb") as f:
            f.write(uploaded_file.getvalue())

    # Get the folder name from the user
    output_folder = st.text_input("Enter the folder name to save frames:")
    num_frames = st.text_input("Enter the number of frames to be extracted:")


    # Button to trigger frame extraction
    if st.button("Extract Frames"):
        # Save frames to the specified folder
        get_frames(temp_video_path, output_folder, int(num_frames))
# # Get user's desktop directory
# desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")

# # Move uploaded file to desktop
# desktop_file_path = os.path.join(desktop_dir, file_name)

# st.text(desktop_file_path)

# os.rename(file_name, desktop_file_path)

# st.info(f"File has been downloaded to your desktop.")

st.subheader("Algo BackTesting")


# # Fetch daily price data from Yahoo Finance
# data = yf.download('MMM', start='2024-01-01', end='2024-04-01')

# # Calculate rolling mean and standard deviation with a window of 6 months
# rolling_mean = data['Close'].rolling(window=10).mean()
# rolling_std = data['Close'].rolling(window=10).std()
# # Determine the thresholds for buy and short signals
# buy_threshold = rolling_mean - 0.07757002261912865 * rolling_std
# short_threshold = rolling_mean + 0.08201316274413653 * rolling_std

# # Initialize variables
# balance = 10000  # Starting balance
# position = None
# buy_signals = []
# sell_signals = []
# short_signals = []
# cover_signals = []
# transactions = []  # To store transaction details

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
#         print(f'New Balance after selling: {balance}')
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
#         print(f'New Balance after covering: {balance}')

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
# fig.update_layout(title='AAPL Daily Stock Prices with Buy, Sell, Short, and Cover Signals',
#                   xaxis_title='Date',
#                   yaxis_title='Price')

# st.plotly_chart(fig)


    