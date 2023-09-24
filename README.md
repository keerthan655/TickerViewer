# TickerViewer

This is a simple web application that allows you to select a stock ticker (e.g., GOOG, AAPL, MSFT, NVDA), fetch data from Yahoo Finance, and display it as a candlestick chart. Dash will be used for the clientside web GUI and flask will used as the server to fetch data.

## Prerequisites

Before running this application, ensure you have the following prerequisites installed on your system:

- Python (version 3.6 or higher)
- pip (Python package manager)

## Installation

1. Download the application source code as a ZIP file.

2. Extract the contents of the ZIP file to a directory of your choice.

3. Open your terminal or command prompt and navigate to the project directory:

   ```bash
   cd path/to/TickerViewer
   
4. Install the required python packages
   ```bash
   pip install -r requirements.txt
   
## Usage

1. Start Flask server
    ```bash
   python server.py

The server will run at http://127.0.0.1:5000/


2. Open another terminal and navaigate to the project directory again then start the Dash client
   ```bash
   cd path/to/TickerViewer
   python client.py
   
The Dash app will run at http://127.0.0.1:8050/

3. Access the Dash application in your web browser by visiting http://127.0.0.1:8050/

4. Use the dropdown list to select a stock ticker (e.g., GOOG, AAPL, MSFT, NVDA).

5. The candlestick chart will display the last 2 years of daily data for the selected stock ticker.
