"""
Momentum Screener API
Finds stocks in early exponential breakout phase with high return potential

Endpoint: /api/screener/momentum
Returns: Top ranked stocks based on exponential pattern + potential return
"""

from http.server import BaseHTTPRequestHandler
import json
import yfinance as yf
import numpy as np
import traceback

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Get top stocks to analyze (curated list of liquid stocks)
            stocks_to_analyze = self.get_stock_universe()

            print(f"Analyzing {len(stocks_to_analyze)} stocks...")

            # Analyze each stock
            results = []
            for i, stock_info in enumerate(stocks_to_analyze):
                try:
                    if i % 10 == 0:
                        print(f"Progress: {i}/{len(stocks_to_analyze)}")

                    score = self.analyze_stock(stock_info['symbol'])
                    if score:
                        score['name'] = stock_info['name']
                        score['exchange'] = stock_info['exchange']
                        results.append(score)
                except Exception as e:
                    print(f"Error analyzing {stock_info['symbol']}: {e}")
                    continue

            # Sort by final score (descending)
            results.sort(key=lambda x: x['final_score'], reverse=True)

            # Take top 100
            top_results = results[:100]

            # Add rank
            for i, stock in enumerate(top_results):
                stock['rank'] = i + 1

            response = {
                'success': True,
                'stocks': top_results,
                'count': len(top_results),
                'analyzed': len(stocks_to_analyze)
            }

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        except Exception as e:
            print(f"Fatal error: {traceback.format_exc()}")
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({
                'success': False,
                'error': str(e),
                'traceback': traceback.format_exc()
            }).encode())

    def get_stock_universe(self):
        """Get list of liquid stocks to analyze"""
        return [
            {'symbol': 'AAPL', 'name': 'Apple Inc.', 'exchange': 'NASDAQ'},
            {'symbol': 'MSFT', 'name': 'Microsoft Corporation', 'exchange': 'NASDAQ'},
            {'symbol': 'GOOGL', 'name': 'Alphabet Inc.', 'exchange': 'NASDAQ'},
            {'symbol': 'AMZN', 'name': 'Amazon.com Inc.', 'exchange': 'NASDAQ'},
            {'symbol': 'NVDA', 'name': 'NVIDIA Corporation', 'exchange': 'NASDAQ'},
            {'symbol': 'META', 'name': 'Meta Platforms Inc.', 'exchange': 'NASDAQ'},
            {'symbol': 'TSLA', 'name': 'Tesla Inc.', 'exchange': 'NASDAQ'},
            {'symbol': 'BRK-B', 'name': 'Berkshire Hathaway', 'exchange': 'NYSE'},
            {'symbol': 'V', 'name': 'Visa Inc.', 'exchange': 'NYSE'},
            {'symbol': 'JNJ', 'name': 'Johnson & Johnson', 'exchange': 'NYSE'},
            {'symbol': 'WMT', 'name': 'Walmart Inc.', 'exchange': 'NYSE'},
            {'symbol': 'JPM', 'name': 'JPMorgan Chase', 'exchange': 'NYSE'},
            {'symbol': 'MA', 'name': 'Mastercard Inc.', 'exchange': 'NYSE'},
            {'symbol': 'PG', 'name': 'Procter & Gamble', 'exchange': 'NYSE'},
            {'symbol': 'UNH', 'name': 'UnitedHealth Group', 'exchange': 'NYSE'},
            {'symbol': 'HD', 'name': 'Home Depot', 'exchange': 'NYSE'},
            {'symbol': 'DIS', 'name': 'Walt Disney Company', 'exchange': 'NYSE'},
            {'symbol': 'BAC', 'name': 'Bank of America', 'exchange': 'NYSE'},
            {'symbol': 'ADBE', 'name': 'Adobe Inc.', 'exchange': 'NASDAQ'},
            {'symbol': 'CRM', 'name': 'Salesforce Inc.', 'exchange': 'NYSE'},
            {'symbol': 'NFLX', 'name': 'Netflix Inc.', 'exchange': 'NASDAQ'},
            {'symbol': 'CSCO', 'name': 'Cisco Systems', 'exchange': 'NASDAQ'},
            {'symbol': 'INTC', 'name': 'Intel Corporation', 'exchange': 'NASDAQ'},
            {'symbol': 'PEP', 'name': 'PepsiCo Inc.', 'exchange': 'NASDAQ'},
            {'symbol': 'AMD', 'name': 'Advanced Micro Devices', 'exchange': 'NASDAQ'},
        ]

    def calculate_exponential_score(self, prices):
        """Calculate exponential growth score (0-100) using simple math"""
        if len(prices) < 20:
            return 0

        try:
            # Calculate percentage gains over time
            gains = []
            for i in range(5, len(prices), 5):
                if prices[i-5] > 0:
                    gain = ((prices[i] - prices[i-5]) / prices[i-5]) * 100
                    gains.append(gain)

            if not gains or len(gains) < 2:
                return 0

            # Exponential pattern: gains should be accelerating
            avg_early = np.mean(gains[:len(gains)//2])
            avg_late = np.mean(gains[len(gains)//2:])

            # Check if recent gains are higher (acceleration)
            acceleration = avg_late - avg_early

            # Check consistency (all gains should be positive)
            positive_count = sum(1 for g in gains if g > 0)
            consistency = (positive_count / len(gains)) * 100

            # Calculate recent slope
            recent_prices = prices[-20:]
            if len(recent_prices) > 1:
                slope = (recent_prices[-1] - recent_prices[0]) / len(recent_prices)
                slope_score = min(100, max(0, slope * 10))
            else:
                slope_score = 0

            # Final exponential score
            score = (consistency * 0.4) + (min(100, max(0, acceleration * 5)) * 0.3) + (slope_score * 0.3)

            return min(100, max(0, score))

        except Exception as e:
            print(f"Error calculating exponential score: {e}")
            return 0

    def calculate_potential_return(self, hist, pattern_scores):
        """Calculate potential return percentage (0-500+)"""
        try:
            if hist.empty or len(hist) < 60:
                return 0

            prices = hist['Close'].values
            current_price = prices[-1]

            # Find 52-week low
            low_52w = np.min(prices)
            distance_from_low = ((current_price - low_52w) / low_52w) * 100

            # Calculate recent momentum (3 months)
            if len(prices) >= 63:
                price_3m_ago = prices[-63]
                recent_gain = ((current_price - price_3m_ago) / price_3m_ago) * 100
            else:
                recent_gain = 0

            # Calculate monthly velocity
            monthly_gains = []
            for months_back in range(1, min(7, len(prices)//21)):
                lookback = months_back * 21
                if lookback < len(prices):
                    old_price = prices[-lookback]
                    if old_price > 0:
                        gain = ((current_price - old_price) / old_price) * 100
                        monthly_gains.append(gain / months_back)

            avg_monthly_gain = np.mean(monthly_gains) if monthly_gains else 0

            # Project forward 6 months
            potential = avg_monthly_gain * 6

            # Bonus for early stage (closer to 52w low = more upside potential)
            if distance_from_low < 200:
                potential *= 1.5

            # Bonus for acceleration
            if recent_gain > avg_monthly_gain:
                potential *= 1.2

            # Average with pattern scores
            avg_pattern = np.mean(list(pattern_scores.values())) if pattern_scores else 0
            potential = (potential * 0.7) + (avg_pattern * 0.3)

            return min(500, max(0, potential))

        except Exception as e:
            print(f"Error calculating potential return: {e}")
            return 0

    def analyze_stock(self, symbol):
        """Analyze a single stock"""
        try:
            # Fetch 1 year of data
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period='1y')

            if hist.empty or len(hist) < 60:
                return None

            # Analyze multiple timeframes
            timeframes = {
                '1M': 21,
                '2M': 42,
                '3M': 63,
                '6M': 126,
                '1Y': min(252, len(hist))
            }

            pattern_scores = {}
            for tf_name, days in timeframes.items():
                if days <= len(hist):
                    data = hist['Close'].iloc[-days:].values
                    score = self.calculate_exponential_score(data)
                    pattern_scores[tf_name] = score

            if not pattern_scores:
                return None

            # Calculate average pattern score
            avg_pattern = np.mean(list(pattern_scores.values()))

            # Calculate potential return
            potential_return = self.calculate_potential_return(hist, pattern_scores)

            # Final score: 30% pattern quality + 70% return potential
            final_score = (avg_pattern * 0.3) + (potential_return * 0.7)

            # Only include stocks with decent scores
            if final_score < 20:
                return None

            return {
                'symbol': symbol,
                'pattern_score': round(avg_pattern, 2),
                'potential_return': round(potential_return, 2),
                'final_score': round(final_score, 2),
                'timeframe_scores': {k: round(v, 2) for k, v in pattern_scores.items()},
                'current_price': round(float(hist['Close'].iloc[-1]), 2)
            }

        except Exception as e:
            print(f"Error analyzing {symbol}: {e}")
            return None

    def do_OPTIONS(self):
        """Handle CORS preflight"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
