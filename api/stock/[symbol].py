"""
Vercel serverless function to fetch stock data.
Endpoint: /api/stock/[symbol]?interval=1d&period=1mo
"""

from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import yfinance as yf
import json

class handler(BaseHTTPRequestHandler):
    """Serverless function handler for Vercel."""

    def do_GET(self):
        try:
            # Parse URL to get query parameters
            parsed_url = urlparse(self.path)
            query_params = parse_qs(parsed_url.query)

            # Get symbol from path (everything after /api/stock/)
            path_parts = parsed_url.path.split('/')
            symbol = path_parts[-1] if len(path_parts) > 0 else ''

            # Get parameters from query string
            interval = query_params.get('interval', ['1d'])[0]
            period = query_params.get('period', ['1mo'])[0]

            if not symbol:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({
                    'error': True,
                    'message': 'Symbol parameter is required'
                }).encode())
                return

            print(f"Fetching {symbol} with interval={interval}, period={period}")

            # Fetch data using yfinance
            ticker = yf.Ticker(symbol)
            df = ticker.history(period=period, interval=interval)

            if df.empty:
                self.send_response(404)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({
                    'error': True,
                    'message': f'No data found for {symbol}'
                }).encode())
                return

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

            response = {
                'success': True,
                'symbol': symbol,
                'interval': interval,
                'period': period,
                'data': data,
                'count': len(data)
            }

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        except Exception as e:
            print(f"Error fetching stock data: {str(e)}")
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({
                'error': True,
                'message': str(e)
            }).encode())

    def do_OPTIONS(self):
        """Handle CORS preflight requests."""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
