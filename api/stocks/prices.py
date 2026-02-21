"""
Vercel serverless function to fetch current prices for multiple stocks.
Endpoint: /api/stocks/prices?symbols=AAPL,MSFT,GOOGL
Returns: JSON object with current prices
"""

from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import yfinance as yf
import json

class handler(BaseHTTPRequestHandler):
    """Serverless function handler for Vercel."""

    def do_GET(self):
        try:
            # Parse query parameters
            parsed_url = urlparse(self.path)
            query_params = parse_qs(parsed_url.query)
            
            # Get symbols list (comma-separated)
            symbols_param = query_params.get('symbols', [''])[0]
            if not symbols_param:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({
                    'error': True,
                    'message': 'symbols parameter is required (comma-separated list)'
                }).encode())
                return

            # Split symbols and limit to 10
            symbols = [s.strip().upper() for s in symbols_param.split(',')][:10]
            
            print(f"Fetching prices for: {symbols}")
            
            # Fetch current prices using yfinance
            prices = {}
            for symbol in symbols:
                try:
                    ticker = yf.Ticker(symbol)
                    # Get latest price from info
                    info = ticker.info
                    
                    # Try different price fields
                    current_price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')
                    
                    if current_price:
                        prices[symbol] = {
                            'price': float(current_price),
                            'currency': info.get('currency', 'USD'),
                            'marketCap': info.get('marketCap'),
                            'volume': info.get('volume')
                        }
                    else:
                        prices[symbol] = {'error': 'Price not available'}
                        
                except Exception as e:
                    print(f"Error fetching {symbol}: {str(e)}")
                    prices[symbol] = {'error': str(e)}

            response = {
                'success': True,
                'prices': prices,
                'test_deployment': 'v2_feb21_15_30'
            }

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Cache-Control', 'public, max-age=60')  # Cache for 1 minute
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        except Exception as e:
            print(f"Error: {str(e)}")
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({
                'error': True,
                'message': str(e)
            }).encode())

    def do_OPTIONS(self):
        """Handle CORS preflight."""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
