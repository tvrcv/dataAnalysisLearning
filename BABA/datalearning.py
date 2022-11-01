import numpy as np
import pandas as pd
import yfinance as yf
from matplotlib import pyplot as plt
# Set the start and end date
start_date = '2020-10-31'
end_date = '2022-10-31'

ticker_list = ['BABA', 'MSFT', 'META', 'SPOT']

# Create placeholder for data
data = pd.DataFrame(columns=ticker_list)
# Fetch the data
for ticker in ticker_list:
    data[ticker] = yf.download(ticker, start_date, end_date)['Close']

# Plot all the close prices
data.plot(figsize=(10, 5))

# Show the legend
plt.legend()

# Define the label for the title of the figure
plt.title("Close Price", fontsize=16)

# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)

# Plot the grid lines

plt.grid(which="major", color='k', linestyle='-.', linewidth=0.4)
plt.show()

# possible ideas
# finding a connection between a significant stock price change
# and an event in real life
