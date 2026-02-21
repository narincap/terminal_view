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
from scipy.optimize import curve_fit
from scipy.stats import linregress
import pandas as pd
from datetime import datetime, timedelta
import traceback

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Get top stocks to analyze (for now, analyze a curated list)
            # In production, this would analyze more stocks in batches
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
            for i, result in enumerate(top_results):
                result['rank'] = i + 1

            response = {
                'success': True,
                'count': len(top_results),
                'analyzed': len(stocks_to_analyze),
                'timestamp': datetime.now().isoformat(),
                'stocks': top_results
            }

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Cache-Control', 'public, max-age=3600')  # Cache for 1 hour
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        except Exception as e:
            print(f"Error in screener: {e}")
            traceback.print_exc()

            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            error_response = json.dumps({
                'success': False,
                'error': str(e),
                'message': 'Failed to run momentum screener'
            })
            self.wfile.write(error_response.encode())

    def get_stock_universe(self):
        """Get list of stocks to analyze"""
        # For initial version, analyze popular stocks from major markets
        # This will be expanded to use the full database

        stocks = [
            # US Tech
            {'symbol': 'NVDA', 'name': 'NVIDIA Corporation', 'exchange': 'NASDAQ'},
            {'symbol': 'AMD', 'name': 'Advanced Micro Devices', 'exchange': 'NASDAQ'},
            {'symbol': 'TSLA', 'name': 'Tesla Inc', 'exchange': 'NASDAQ'},
            {'symbol': 'AAPL', 'name': 'Apple Inc', 'exchange': 'NASDAQ'},
            {'symbol': 'MSFT', 'name': 'Microsoft Corporation', 'exchange': 'NASDAQ'},
            {'symbol': 'GOOGL', 'name': 'Alphabet Inc', 'exchange': 'NASDAQ'},
            {'symbol': 'META', 'name': 'Meta Platforms', 'exchange': 'NASDAQ'},
            {'symbol': 'AMZN', 'name': 'Amazon.com Inc', 'exchange': 'NASDAQ'},

            # Indonesian stocks
            {'symbol': 'BBCA.JK', 'name': 'Bank Central Asia', 'exchange': 'IDX'},
            {'symbol': 'BBRI.JK', 'name': 'Bank Rakyat Indonesia', 'exchange': 'IDX'},
            {'symbol': 'BMRI.JK', 'name': 'Bank Mandiri', 'exchange': 'IDX'},
            {'symbol': 'TLKM.JK', 'name': 'Telkom Indonesia', 'exchange': 'IDX'},
            {'symbol': 'ASII.JK', 'name': 'Astra International', 'exchange': 'IDX'},
            {'symbol': 'GOTO.JK', 'name': 'GoTo Gojek Tokopedia', 'exchange': 'IDX'},
            {'symbol': 'VISI.JK', 'name': 'Satu Visi Putra Tbk', 'exchange': 'IDX'},

            # More sectors
            {'symbol': 'LLY', 'name': 'Eli Lilly and Company', 'exchange': 'NYSE'},
            {'symbol': 'JPM', 'name': 'JPMorgan Chase', 'exchange': 'NYSE'},
            {'symbol': 'V', 'name': 'Visa Inc', 'exchange': 'NYSE'},
            {'symbol': 'MA', 'name': 'Mastercard Inc', 'exchange': 'NYSE'},
        ]

        return stocks

    def analyze_stock(self, symbol):
        """Analyze a single stock for exponential pattern and return potential"""

        # Fetch 1 year of data
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period='1y', interval='1d')

        if len(hist) < 60:  # Need at least 60 days
            return None

        # Get current price
        current_price = hist['Close'].iloc[-1]

        # Analyze multiple timeframes
        timeframes = {
            '1M': 21,   # ~21 trading days
            '2M': 42,
            '3M': 63,
            '6M': 126,
            '1Y': 252
        }

        pattern_scores = {}

        for tf_name, days in timeframes.items():
            if len(hist) >= days:
                data = hist['Close'].iloc[-days:].values
                score = self.calculate_exponential_score(data)
                pattern_scores[tf_name] = score

        # Average pattern quality
        avg_pattern = np.mean(list(pattern_scores.values())) if pattern_scores else 0

        # Calculate potential return
        potential_return = self.calculate_potential_return(hist, pattern_scores)

        # Final score: 30% pattern + 70% potential return
        final_score = (avg_pattern * 0.3) + (potential_return * 0.7)

        # Get mini chart data (last 6 months)
        chart_data = hist['Close'].iloc[-126:].tolist()

        return {
            'symbol': symbol,
            'price': round(current_price, 2),
            'pattern_score': round(avg_pattern, 1),
            'potential_return': round(potential_return, 1),
            'final_score': round(final_score, 2),
            'timeframe_scores': {k: round(v, 1) for k, v in pattern_scores.items()},
            'chart_data': chart_data,
            'projected_price': round(current_price * (1 + potential_return/100), 2)
        }

    def calculate_exponential_score(self, prices):
        """Calculate how well the price fits an exponential curve (0-100)"""

        if len(prices) < 10:
            return 0

        x = np.arange(len(prices))
        y = prices

        # Remove any NaN or inf values
        mask = np.isfinite(y)
        x = x[mask]
        y = y[mask]

        if len(x) < 10:
            return 0

        try:
            # Exponential function: a * e^(b*x)
            def exp_func(x, a, b):
                return a * np.exp(b * x)

            # Fit exponential curve
            popt_exp, _ = curve_fit(exp_func, x, y, p0=[y[0], 0.01], maxfev=5000)
            y_exp_fit = exp_func(x, *popt_exp)

            # Calculate R² for exponential fit
            ss_res_exp = np.sum((y - y_exp_fit) ** 2)
            ss_tot = np.sum((y - np.mean(y)) ** 2)
            r2_exp = 1 - (ss_res_exp / ss_tot) if ss_tot > 0 else 0

            # Linear fit for comparison
            slope, intercept, _, _, _ = linregress(x, y)
            y_lin_fit = slope * x + intercept
            ss_res_lin = np.sum((y - y_lin_fit) ** 2)
            r2_lin = 1 - (ss_res_lin / ss_tot) if ss_tot > 0 else 0

            # Score based on:
            # 1. Exponential R² quality (0-100)
            # 2. Exponential fits better than linear
            # 3. Positive growth (b > 0)

            score = 0

            if r2_exp > 0.7:  # Good exponential fit
                score += r2_exp * 70  # Up to 70 points for fit quality

            if r2_exp > r2_lin and popt_exp[1] > 0:  # Exponential better than linear AND growing
                score += 30  # 30 bonus points

            return min(100, max(0, score))

        except Exception as e:
            # If curve fitting fails, return 0
            return 0

    def calculate_potential_return(self, hist, pattern_scores):
        """Calculate potential return percentage (0-500+)"""

        if len(hist) < 63:
            return 0

        # Get recent performance
        price_3m_ago = hist['Close'].iloc[-63]
        current_price = hist['Close'].iloc[-1]
        recent_gain = ((current_price - price_3m_ago) / price_3m_ago) * 100

        # Get distance from 1-year low
        year_low = hist['Close'].min()
        distance_from_low = ((current_price - year_low) / year_low) * 100

        # Calculate velocity (monthly gain rate)
        monthly_gains = []
        for i in range(1, 7):  # Last 6 months
            days = i * 21
            if len(hist) >= days + 21:
                month_ago_price = hist['Close'].iloc[-(days + 21)]
                month_price = hist['Close'].iloc[-days] if days > 0 else current_price
                if month_ago_price > 0:
                    gain = ((month_price - month_ago_price) / month_ago_price) * 100
                    monthly_gains.append(gain)

        avg_monthly_gain = np.mean(monthly_gains) if monthly_gains else 0

        # Acceleration (is it speeding up?)
        acceleration = 0
        if len(monthly_gains) >= 3:
            recent_avg = np.mean(monthly_gains[:3])
            older_avg = np.mean(monthly_gains[3:])
            acceleration = recent_avg - older_avg

        # Average pattern quality across timeframes
        avg_pattern = np.mean(list(pattern_scores.values())) if pattern_scores else 0

        # Calculate potential return
        # Formula: Base on recent momentum + acceleration + pattern quality

        potential = 0

        # If showing strong exponential pattern and positive momentum
        if avg_pattern > 60 and avg_monthly_gain > 0:
            # Project 6 months forward
            projected_months = 6

            # Conservative: Current monthly rate
            conservative = avg_monthly_gain * projected_months

            # With acceleration
            if acceleration > 0:
                accelerated = conservative * (1 + acceleration/100)
            else:
                accelerated = conservative

            # Adjust based on how early we are (more potential if just started)
            if distance_from_low < 200:  # Less than 3x from low = early
                early_bonus = 1.5
            elif distance_from_low < 400:  # 3-5x from low = mid
                early_bonus = 1.2
            else:  # Already up a lot
                early_bonus = 0.8

            potential = accelerated * early_bonus

        # Cap potential return at 500%
        return min(500, max(0, potential))

    def do_OPTIONS(self):
        """Handle CORS preflight"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
