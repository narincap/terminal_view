"""
Vercel serverless function to serve stock database.
Returns stock database JSON directly.

🌍 ULTIMATE GLOBAL DATABASE: 63,553 stocks from 33 exchanges worldwide
"""

from http.server import BaseHTTPRequestHandler
import json
import os

class handler(BaseHTTPRequestHandler):
    """Serverless function handler for Vercel."""

    def do_GET(self):
        try:
            # Read the static JSON file
            # Vercel puts files in /var/task/public during deployment
            json_path = os.path.join(os.path.dirname(__file__), '..', '..', 'public', 'stocks-database.json')
            
            with open(json_path, 'r') as f:
                stock_data = f.read()
            
            # Send JSON response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Cache-Control', 'public, max-age=86400')
            self.send_header('Content-Length', str(len(stock_data)))
            self.end_headers()
            self.wfile.write(stock_data.encode('utf-8'))

        except Exception as e:
            print(f"Error: {str(e)}")
            import traceback
            traceback.print_exc()
            
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            error_response = json.dumps({
                'success': False,
                'error': str(e),
                'message': 'Failed to load stock database'
            })
            self.wfile.write(error_response.encode())

    def do_OPTIONS(self):
        """Handle CORS preflight."""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
