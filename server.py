#!/usr/bin/env python3
"""
Simple Flask server to fetch stock data and bypass CORS issues.
Install dependencies: pip install flask flask-cors yfinance
Run: python3 server.py
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import yfinance as yf
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/stock/<symbol>')
def get_stock_data(symbol):
    """Fetch stock data for given symbol and parameters."""
    try:
        # Get parameters from query string
        interval = request.args.get('interval', '1d')
        period = request.args.get('period', '1mo')

        print(f"Fetching {symbol} with interval={interval}, period={period}")

        # Fetch data using yfinance
        ticker = yf.Ticker(symbol)
        df = ticker.history(period=period, interval=interval)

        if df.empty:
            return jsonify({
                'error': True,
                'message': f'No data found for {symbol}'
            }), 404

        # Convert DataFrame to format expected by TradingView Lightweight Charts
        data = []
        for index, row in df.iterrows():
            data.append({
                'time': int(index.timestamp()),
                'open': float(row['Open']),
                'high': float(row['High']),
                'low': float(row['Low']),
                'close': float(row['Close']),
                'volume': int(row['Volume']) if 'Volume' in row else 0
            })

        return jsonify({
            'success': True,
            'symbol': symbol,
            'interval': interval,
            'period': period,
            'data': data,
            'count': len(data)
        })

    except Exception as e:
        print(f"Error fetching {symbol}: {str(e)}")
        return jsonify({
            'error': True,
            'message': str(e)
        }), 500

@app.route('/api/health')
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'ok',
        'message': 'Stock data server is running'
    })

@app.route('/')
def index():
    """Root endpoint."""
    return jsonify({
        'message': 'Stock Data API Server',
        'endpoints': {
            '/api/health': 'Health check',
            '/api/stock/<symbol>': 'Get stock data (params: interval, period)'
        }
    })

if __name__ == '__main__':
    print("=" * 60)
    print("Stock Data Server Starting...")
    print("=" * 60)
    print("Server will run on: http://localhost:5001")
    print("Health check: http://localhost:5001/api/health")
    print("Example: http://localhost:5001/api/stock/BBCA.JK?interval=1d&period=1mo")
    print("=" * 60)
    print("\nPress Ctrl+C to stop the server\n")

    app.run(host='0.0.0.0', port=5001, debug=True)
