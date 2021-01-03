# Import Libraries
import requests
import numpy as np
import matplotlib
import datetime as dt
import matplotlib.pyplot as plt

# Go to alphavantage documentation to get your own api key and paste it in between "" | https://www.alphavantage.co/
apiKey = ""

# Can be replaced with any Stock Symbol
symbol = "TSLA"

# You can also use 1min, 5min, 15min, 30min & 60min
interval = "1min"
URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&outputsize=full&apikey={apiKey}"
response = requests.get(URL)


# Change to python dictionary format
response = response.json().get(f"Time Series ({interval})")

closeValues = []
dates = []
closeValues, dates = np.array(closeValues), np.array(dates)

"""
NOTE: instead of "4. close" you can also use:
    - "1. open"
    - "2. high"
    - "3. low"
    - "4. close"
    - "5. volume"
"""

for x in response:
    closeValues = np.append(response.get(x).get("4. close"), closeValues)
    dateTime = dt.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
    dates = np.append(dateTime, dates)

closeValues = closeValues.astype(float)

# As the name suggest this will give you the current or last value in the market as USD dollars
currentValue = closeValues[-1]
print(currentValue)

# Visualize data
plt.style.use('dark_background')
plt.figure(figsize=(16, 8))
plt.title(f'Time Series ({interval})')
plt.xlabel('Date')
plt.ylabel(f'Price of {symbol} USD ($)')
plt.plot(dates, closeValues)
plt.show()
