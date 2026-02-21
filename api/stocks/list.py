"""
Vercel serverless function to serve stock database.
Returns stock database JSON directly.

🌍 GLOBAL DATABASE: 25,188 stocks from around the world
"""

from http.server import BaseHTTPRequestHandler
import json
import os
import sys

class handler(BaseHTTPRequestHandler):
    """Serverless function handler for Vercel."""

    def do_GET(self):
        try:
            # Try multiple paths to find the JSON file
            possible_paths = [
                '/var/task/public/stocks-database.json',  # Vercel standard
                'public/stocks-database.json',  # Relative
                '../../public/stocks-database.json',  # From api/stocks/
                '/stocks-database.json',  # Root
            ]
            
            stock_data = None
            used_path = None
            
            for path in possible_paths:
                if os.path.exists(path):
                    with open(path, 'r') as f:
                        stock_data = f.read()
                    used_path = path
                    print(f"✅ Found file at: {path}")
                    break
            
            if stock_data is None:
                # Log debug info
                cwd = os.getcwd()
                files = os.listdir(cwd) if os.path.exists(cwd) else []
                raise FileNotFoundError(f"Stock database not found. CWD: {cwd}, Files: {files[:10]}")
            
            # Send JSON response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Cache-Control', 'public, max-age=86400')
            self.end_headers()
            self.wfile.write(stock_data.encode('utf-8'))

        except Exception as e:
            print(f"❌ Error: {str(e)}")
            import traceback
            traceback.print_exc()
            
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            error_response = json.dumps({
                'success': False,
                'error': str(e),
                'message': f'Failed to load stock database: {str(e)}'
            })
            self.wfile.write(error_response.encode())

    def do_OPTIONS(self):
        """Handle CORS preflight."""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
