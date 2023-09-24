import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import requests
from datetime import datetime
app = dash.Dash(__name__)
# Create Web GUI
app.layout = html.Div([
    html.H1("Stock Candlestick Chart"),
    dcc.Dropdown(
        id='stock-ticker-dropdown',
        options=[
            {'label': 'GOOG', 'value': 'GOOG'},
            {'label': 'AAPL', 'value': 'AAPL'},
            {'label': 'MSFT', 'value': 'MSFT'},
            {'label': 'NVDA', 'value': 'NVDA'}
        ],
        value='GOOG'
    ),
    dcc.Graph(id='candlestick-chart')
])

@app.callback(
    Output('candlestick-chart', 'figure'),
    [Input('stock-ticker-dropdown', 'value')]
)
def update_candlestick_chart(selected_ticker):
    # Make an API request to the Flask server
    response = requests.post('http://127.0.0.1:5000/get_stock_data', json={'ticker': selected_ticker})
    stock_data = response.json()

    # Create a candlestick chart
    figure = {
        'data': [
            go.Candlestick(
                x=[data['Date'] for data in stock_data],
                open=[data['Open'] for data in stock_data],
                high=[data['High'] for data in stock_data],
                low=[data['Low'] for data in stock_data],
                close=[data['Close'] for data in stock_data],
                name=selected_ticker,
            )
        ],
        'layout': {
            'title': f'{selected_ticker} Candlestick Chart',
            'xaxis': {
                'rangeslider': {'visible': False},
                'type': 'category',  # Set the x-axis type to 'category'
                'tickmode': 'array',
                'tickvals': [i for i in range(0, len(stock_data), 7)],  # Display every 7th date
                'ticktext': [datetime.strptime(data['Date'], '%a, %d %b %Y %H:%M:%S %Z').strftime('%d-%b-%Y') for data in stock_data[::7]],
                'title': 'Date'
            },
            'yaxis': {'title': 'Price'}
        }
    }

    return figure

if __name__ == '__main__':
    app.run_server(debug=True)
