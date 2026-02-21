#!/usr/bin/env python3
"""
Get ALL tickers from multiple sources
Target: 15,000-30,000+ stocks worldwide
"""

import yfinance as yf
import pandas as pd
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

def get_nasdaq_all():
    """Get ALL NASDAQ stocks from official NASDAQ FTP"""
    print("📊 Downloading ALL NASDAQ stocks from official FTP...")
    try:
        url = 'ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt'
        df = pd.read_csv(url, sep='|')

        # Filter out test issues and keep only normal stocks
        df = df[df['Test Issue'] == 'N']
        df = df[df['Symbol'].str.len() <= 5]  # Remove weird symbols

        symbols = df['Symbol'].tolist()
        # Remove the last row which is just file info
        symbols = [s for s in symbols if s != 'File Creation Time']

        print(f"✅ Got {len(symbols)} NASDAQ stocks")
        return symbols
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

def get_nyse_all():
    """Get ALL NYSE, AMEX, ARCA stocks from official NASDAQ FTP"""
    print("📊 Downloading ALL NYSE/AMEX/ARCA stocks from official FTP...")
    try:
        url = 'ftp://ftp.nasdaqtrader.com/SymbolDirectory/otherlisted.txt'
        df = pd.read_csv(url, sep='|')

        # Filter
        df = df[df['Test Issue'] == 'N']

        symbols = df['ACT Symbol'].tolist()
        symbols = [s for s in symbols if s != 'File Creation Time' and len(s) <= 5]

        print(f"✅ Got {len(symbols)} NYSE/AMEX/ARCA stocks")
        return symbols
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

def get_all_idx_stocks():
    """Get ALL IDX stocks - comprehensive list"""
    print("📊 Getting comprehensive IDX stock list...")

    # We already have 745 validated, let's add more known patterns
    idx_symbols = []

    # Load from current database
    try:
        with open('api/stocks/list.py', 'r') as f:
            import re
            matches = re.findall(r'"symbol":\s*"([A-Z0-9]+\.JK)"', f.read())
            idx_symbols.extend(matches)
    except:
        pass

    # Add common patterns that might be missing
    # IDX uses 4-letter codes
    common_prefixes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # Generate potential symbols (4-letter codes)
    for p1 in common_prefixes:
        for p2 in common_prefixes[:10]:  # Limit to avoid explosion
            for suffix in ['A', 'B', 'C', 'I', 'L', 'M', 'N', 'R', 'S', 'T']:
                symbol = f"{p1}{p2}{suffix}J.JK"
                idx_symbols.append(symbol)

    idx_symbols = list(set(idx_symbols))
    print(f"✅ Got {len(idx_symbols)} potential IDX symbols")
    return idx_symbols

def get_international_stocks():
    """Get international stocks from major exchanges"""
    print("📊 Adding international stocks...")
    intl = []

    # Hong Kong - top 500
    for i in range(1, 500):
        intl.append(f"{i:04d}.HK")

    # Japan TSE - major companies
    for i in range(1000, 2000):
        intl.append(f"{i}.T")
    for i in range(3000, 4000):
        intl.append(f"{i}.T")
    for i in range(6000, 7500):
        intl.append(f"{i}.T")
    for i in range(9000, 10000):
        intl.append(f"{i}.T")

    # Singapore
    sgx_codes = ['D05', 'O39', 'U11', 'C6L', 'C52', 'S58', 'BN4', 'Z74', 'V03',
                 'Y92', 'C07', 'F34', 'C38U', 'BS6', 'C09']
    intl.extend([f"{code}.SI" for code in sgx_codes])

    # UK FTSE
    uk_tops = ['BP', 'SHEL', 'HSBA', 'AZN', 'ULVR', 'GSK', 'DGE', 'RIO', 'BARC',
               'LLOY', 'VOD', 'BT-A', 'GLEN', 'AAL', 'NG', 'PRU', 'LSEG', 'REL']
    intl.extend([f"{code}.L" for code in uk_tops])

    # Germany
    de_stocks = ['SAP', 'SIE.DE', 'ALV.DE', 'DTE.DE', 'VOW3.DE', 'DAI.DE', 'BMW.DE',
                 'BAYN.DE', 'MBG.DE', 'DB1.DE', 'ADS.DE', 'BAS.DE']
    intl.extend(de_stocks)

    # France
    fr_stocks = ['MC.PA', 'OR.PA', 'SAN.PA', 'AIR.PA', 'BNP.PA', 'TTE.PA', 'SU.PA',
                 'CA.PA', 'RMS.PA', 'BN.PA']
    intl.extend(fr_stocks)

    print(f"✅ Got {len(intl)} international symbols")
    return intl

def get_crypto_and_indices():
    """Get crypto and indices"""
    print("📊 Adding crypto, indices, commodities...")

    crypto = [
        'BTC-USD', 'ETH-USD', 'BNB-USD', 'XRP-USD', 'ADA-USD', 'DOGE-USD',
        'SOL-USD', 'DOT-USD', 'MATIC-USD', 'AVAX-USD', 'LINK-USD', 'UNI-USD',
        'ATOM-USD', 'LTC-USD', 'BCH-USD', 'XLM-USD', 'ALGO-USD', 'VET-USD',
        'ICP-USD', 'FIL-USD', 'TRX-USD', 'ETC-USD', 'XMR-USD'
    ]

    indices = [
        '^GSPC', '^DJI', '^IXIC', '^RUT', '^FTSE', '^GDAXI', '^FCHI',
        '^N225', '^HSI', '^JKSE', '^STI', '^AXJO', '^KS11', '^TWII',
        '^NSEI', '^BSESN', '^SSEC'
    ]

    commodities = [
        'GC=F', 'SI=F', 'CL=F', 'NG=F', 'HG=F', 'PL=F', 'PA=F'
    ]

    all_items = crypto + indices + commodities
    print(f"✅ Got {len(all_items)} crypto/indices/commodities")
    return all_items

def validate_symbol_batch(symbols, max_workers=20):
    """Validate symbols in batch with rate limiting"""
    valid_stocks = []
    failed = 0
    total = len(symbols)

    print(f"\n🔄 Validating {total:,} symbols...")
    print(f"Using {max_workers} workers with rate limiting")
    print("=" * 70)

    def validate_one(symbol):
        try:
            # Add small delay for rate limiting
            time.sleep(0.05)  # 20 requests/second max

            ticker = yf.Ticker(symbol)
            info = ticker.info

            if info and 'symbol' in info:
                # Determine exchange
                exchange = info.get('exchange', '')

                if '.JK' in symbol:
                    exchange = 'IDX'
                elif '.HK' in symbol:
                    exchange = 'HKEX'
                elif '.T' in symbol:
                    exchange = 'TSE'
                elif '.SI' in symbol:
                    exchange = 'SGX'
                elif '.L' in symbol:
                    exchange = 'LSE'
                elif '.DE' in symbol:
                    exchange = 'XETRA'
                elif '.PA' in symbol:
                    exchange = 'EPA'
                elif '-USD' in symbol:
                    exchange = 'CRYPTO'
                elif symbol.startswith('^'):
                    exchange = 'INDEX'
                elif '=F' in symbol:
                    exchange = 'FUTURES'
                else:
                    # US stock
                    if not exchange:
                        exchange = 'NASDAQ'

                return {
                    'symbol': symbol,
                    'name': (info.get('longName') or info.get('shortName') or symbol).replace('"', "'"),
                    'exchange': exchange,
                    'sector': info.get('sector', ''),
                    'industry': info.get('industry', '')
                }
        except:
            pass
        return None

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(validate_one, sym): sym for sym in symbols}

        for future in as_completed(futures):
            try:
                result = future.result()
                if result:
                    valid_stocks.append(result)
                    if len(valid_stocks) % 500 == 0:
                        elapsed = time.time() - start_time
                        rate = len(valid_stocks) / elapsed if elapsed > 0 else 0
                        remaining = total - len(valid_stocks) - failed
                        eta = remaining / rate if rate > 0 else 0

                        print(f"✓ {len(valid_stocks):5,} valid | {failed:4,} failed | "
                              f"{rate:.1f}/s | ETA: {eta/60:.0f}m | {result['symbol']}")
                else:
                    failed += 1
            except:
                failed += 1

    elapsed = time.time() - start_time
    print("\n" + "=" * 70)
    print(f"✅ Validation complete in {elapsed/60:.1f} minutes")
    print(f"✓ Valid: {len(valid_stocks):,}")
    print(f"✗ Failed: {failed:,}")
    print(f"📊 Success rate: {len(valid_stocks)/(len(valid_stocks)+failed)*100:.1f}%")

    return valid_stocks

def main():
    print("=" * 70)
    print("🌍 FETCHING ALL AVAILABLE TICKERS - COMPLETE EDITION")
    print("=" * 70)
    print()

    all_symbols = []

    # Get all sources
    all_symbols.extend(get_nasdaq_all())
    all_symbols.extend(get_nyse_all())
    all_symbols.extend(get_all_idx_stocks())
    all_symbols.extend(get_international_stocks())
    all_symbols.extend(get_crypto_and_indices())

    # Remove duplicates
    all_symbols = list(set(all_symbols))

    print()
    print("=" * 70)
    print(f"📊 TOTAL SYMBOLS COLLECTED: {len(all_symbols):,}")
    print("=" * 70)

    # Validate all
    stocks = validate_symbol_batch(all_symbols, max_workers=15)  # Slower to avoid rate limits

    # Save
    stocks_sorted = sorted(stocks, key=lambda x: (x['exchange'], x['symbol']))
    data = {'success': True, 'count': len(stocks_sorted), 'stocks': stocks_sorted}

    with open('all_stocks_COMPLETE.json', 'w') as f:
        json.dump(data, f, indent=2)

    # Size analysis
    json_str = json.dumps(data)
    import gzip, brotli
    gzipped = gzip.compress(json_str.encode('utf-8'))
    brotli_compressed = brotli.compress(json_str.encode('utf-8'), quality=11)

    print()
    print("=" * 70)
    print("📦 FILE SIZE ANALYSIS")
    print("=" * 70)
    print(f"Uncompressed: {len(json_str):,} bytes ({len(json_str)//1024:,} KB)")
    print(f"Gzipped: {len(gzipped):,} bytes ({len(gzipped)//1024:,} KB)")
    print(f"Brotli: {len(brotli_compressed):,} bytes ({len(brotli_compressed)//1024:,} KB)")

    if len(brotli_compressed) > 4_500_000:
        print("⚠️ WARNING: Exceeds Vercel 4.5MB limit!")
        print(f"   Current: {len(brotli_compressed)//1024//1024:.1f}MB")
        print("   Need to reduce or paginate")
    elif len(brotli_compressed) > 2_000_000:
        print(f"⚠️ Large file: {len(brotli_compressed)//1024//1024:.1f}MB")
    else:
        print("✅ Perfect for Vercel!")

    # Breakdown
    print()
    print("=" * 70)
    print("📊 BREAKDOWN BY EXCHANGE")
    print("=" * 70)

    exchanges = {}
    for stock in stocks:
        ex = stock['exchange']
        exchanges[ex] = exchanges.get(ex, 0) + 1

    for exchange, count in sorted(exchanges.items(), key=lambda x: -x[1]):
        print(f"{exchange:15} {count:6,} stocks")

    print()
    print(f"💾 Saved to: all_stocks_COMPLETE.json")
    print("=" * 70)
    print()
    print(f"🎉 GOT {len(stocks):,} STOCKS FROM AROUND THE WORLD!")
    print("=" * 70)

if __name__ == '__main__':
    main()
