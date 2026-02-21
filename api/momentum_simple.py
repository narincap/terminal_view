from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Simple test response
            response = {
                'success': True,
                'message': 'Momentum screener endpoint works!',
                'stocks': [
                    {
                        'symbol': 'TEST',
                        'name': 'Test Stock',
                        'pattern_score': 85.5,
                        'potential_return': 120.0,
                        'final_score': 95.0
                    }
                ]
            }

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({
                'success': False,
                'error': str(e)
            }).encode())
