"""
Main Flask application for Google Cloud Run
Serves all API endpoints and static files
"""

from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import yfinance as yf
import json
import os
from datetime import datetime, timedelta
import traceback

app = Flask(__name__, static_folder='public', static_url_path='')
CORS(app)

# Serve index.html at root
@app.route('/')
def serve_index():
    return send_from_directory('public', 'index.html')

# Serve static files
@app.route('/<path:path>')
def serve_static(path):
    if os.path.exists(os.path.join('public', path)):
        return send_from_directory('public', path)
    return send_from_directory('public', 'index.html')

# Stock data endpoint
@app.route('/api/stock/<symbol>')
def get_stock(symbol):
    try:
        interval = request.args.get('interval', '1d')
        period = request.args.get('period', '1mo')

        ticker = yf.Ticker(symbol)
        df = ticker.history(period=period, interval=interval)

        if df.empty:
            return jsonify({'error': True, 'message': f'No data found for {symbol}'}), 404

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
        return jsonify({'error': True, 'message': str(e)}), 500

# Stock list endpoint
@app.route('/api/stocks/list')
def get_stock_list():
    try:
        with open('public/stocks-database.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# Stock prices endpoint
@app.route('/api/stocks/prices')
def get_stock_prices():
    try:
        symbols_param = request.args.get('symbols', '')
        if not symbols_param:
            return jsonify({'error': True, 'message': 'symbols parameter required'}), 400

        symbols = symbols_param.split(',')
        prices = {}

        for symbol in symbols[:10]:  # Limit to 10 at a time
            try:
                ticker = yf.Ticker(symbol)
                info = ticker.info
                prices[symbol] = {
                    'price': info.get('currentPrice', info.get('regularMarketPrice', 0)),
                    'currency': info.get('currency', 'USD'),
                    'marketCap': info.get('marketCap', 0),
                    'volume': info.get('volume', 0)
                }
            except Exception as e:
                prices[symbol] = {'error': str(e)}

        return jsonify({'success': True, 'prices': prices})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# Momentum screener endpoint
@app.route('/api/screener/momentum')
def momentum_screener():
    try:
        # Import the screener logic
        from api.screener.momentum import handler

        # Create a mock request handler
        class MockHandler:
            def __init__(self):
                self.response_data = None
                self.status_code = 200

            def send_response(self, code):
                self.status_code = code

            def send_header(self, key, value):
                pass

            def end_headers(self):
                pass

            def wfile_write(self, data):
                self.response_data = data

        # Get stocks to analyze
        stocks = [
            {'symbol': 'AAPL', 'name': 'Apple Inc.', 'exchange': 'NASDAQ'},
            {'symbol': 'MSFT', 'name': 'Microsoft Corporation', 'exchange': 'NASDAQ'},
            {'symbol': 'GOOGL', 'name': 'Alphabet Inc.', 'exchange': 'NASDAQ'},
            {'symbol': 'AMZN', 'name': 'Amazon.com Inc.', 'exchange': 'NASDAQ'},
            {'symbol': 'NVDA', 'name': 'NVIDIA Corporation', 'exchange': 'NASDAQ'},
            {'symbol': 'META', 'name': 'Meta Platforms Inc.', 'exchange': 'NASDAQ'},
            {'symbol': 'TSLA', 'name': 'Tesla Inc.', 'exchange': 'NASDAQ'},
            {'symbol': 'V', 'name': 'Visa Inc.', 'exchange': 'NYSE'},
            {'symbol': 'JPM', 'name': 'JPMorgan Chase', 'exchange': 'NYSE'},
            {'symbol': 'WMT', 'name': 'Walmart Inc.', 'exchange': 'NYSE'},
        ]

        results = []
        for stock in stocks:
            try:
                ticker = yf.Ticker(stock['symbol'])
                hist = ticker.history(period='1y')

                if hist.empty or len(hist) < 60:
                    continue

                prices = [float(p) for p in hist['Close'].values]
                current_price = prices[-1]

                # Simple momentum calculation
                price_3m = prices[-63] if len(prices) >= 63 else prices[0]
                gain_3m = ((current_price - price_3m) / price_3m) * 100

                # Pattern score (simplified)
                recent_gain = ((prices[-1] - prices[-21]) / prices[-21]) * 100 if len(prices) >= 21 else 0
                pattern_score = min(100, max(0, recent_gain * 2))

                # Potential return (simplified)
                low_52w = min(prices)
                distance_from_low = ((current_price - low_52w) / low_52w) * 100
                potential = gain_3m * 2

                if distance_from_low < 200:
                    potential *= 1.5

                final_score = (pattern_score * 0.3) + (min(500, max(0, potential)) * 0.7)

                if final_score > 20:
                    results.append({
                        'symbol': stock['symbol'],
                        'name': stock['name'],
                        'exchange': stock['exchange'],
                        'pattern_score': round(pattern_score, 2),
                        'potential_return': round(min(500, max(0, potential)), 2),
                        'final_score': round(final_score, 2),
                        'current_price': round(current_price, 2),
                        'timeframe_scores': {
                            '1M': round(pattern_score, 2),
                            '3M': round(pattern_score * 0.9, 2),
                            '6M': round(pattern_score * 0.8, 2),
                            '1Y': round(pattern_score * 0.7, 2)
                        }
                    })
            except Exception as e:
                print(f"Error analyzing {stock['symbol']}: {e}")
                continue

        # Sort by final score
        results.sort(key=lambda x: x['final_score'], reverse=True)

        # Add ranks
        for i, stock in enumerate(results):
            stock['rank'] = i + 1

        return jsonify({
            'success': True,
            'stocks': results,
            'count': len(results),
            'analyzed': len(stocks)
        })

    except Exception as e:
        print(f"Screener error: {traceback.format_exc()}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
