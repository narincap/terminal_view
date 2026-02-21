#!/usr/bin/env python3
"""
Build COMPLETE stock database from official ticker lists
NO Yahoo Finance validation needed - validate on-demand when loading charts!
"""

import pandas as pd
import json
import brotli

def get_nasdaq_all():
    """Get ALL NASDAQ stocks from official FTP"""
    print("📊 Downloading ALL NASDAQ stocks...")
    try:
        url = 'ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt'
        df = pd.read_csv(url, sep='|')

        # Clean up
        df = df[df['Test Issue'] == 'N']  # No test issues
        df = df[df['Financial Status'] != 'D']  # Not deficient
        df = df[~df['Symbol'].str.contains('\$')]  # No special symbols

        stocks = []
        for _, row in df.iterrows():
            if row['Symbol'] == 'File Creation Time':
                continue
            stocks.append({
                'symbol': row['Symbol'],
                'name': row['Security Name'],
                'exchange': 'NASDAQ',
                'sector': '',  # NASDAQ doesn't provide this
                'industry': ''
            })

        print(f"✅ Got {len(stocks)} NASDAQ stocks")
        return stocks
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

def get_nyse_all():
    """Get ALL NYSE/AMEX/ARCA stocks"""
    print("📊 Downloading ALL NYSE/AMEX/ARCA stocks...")
    try:
        url = 'ftp://ftp.nasdaqtrader.com/SymbolDirectory/otherlisted.txt'
        df = pd.read_csv(url, sep='|')

        df = df[df['Test Issue'] == 'N']
        df = df[~df['ACT Symbol'].str.contains('\$')]

        stocks = []
        for _, row in df.iterrows():
            if row['ACT Symbol'] == 'File Creation Time':
                continue

            # Determine exchange
            exchange = row['Exchange']
            if exchange == 'N':
                exchange_name = 'NYSE'
            elif exchange == 'A':
                exchange_name = 'AMEX'
            elif exchange == 'P':
                exchange_name = 'ARCA'
            elif exchange == 'Z':
                exchange_name = 'BATS'
            else:
                exchange_name = 'NYSE'

            stocks.append({
                'symbol': row['ACT Symbol'],
                'name': row['Security Name'],
                'exchange': exchange_name,
                'sector': '',
                'industry': ''
            })

        print(f"✅ Got {len(stocks)} NYSE/AMEX/ARCA stocks")
        return stocks
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

def get_idx_stocks():
    """Get IDX stocks from current database"""
    print("📊 Loading IDX stocks from current database...")
    try:
        with open('api/stocks/list.py', 'r') as f:
            import re
            content = f.read()
            matches = re.findall(
                r'\["([^"]+)",\s*"([^"]+)",\s*"([^"]*)",\s*"([^"]*)"\]',
                content
            )

            stocks = []
            for match in matches:
                # Only get IDX stocks (those with .JK)
                if '.JK' in match[0]:
                    stocks.append({
                        'symbol': match[0],
                        'name': match[1],
                        'exchange': 'IDX',
                        'sector': match[2],
                        'industry': match[3]
                    })

        print(f"✅ Got {len(stocks)} IDX stocks")
        return stocks
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

def get_international_and_crypto():
    """Get international stocks and crypto"""
    print("📊 Adding international stocks, crypto, indices...")

    stocks = []

    # Major Hong Kong stocks
    hk_major = [
        ('0700.HK', 'Tencent Holdings'),
        ('9988.HK', 'Alibaba Group'),
        ('0005.HK', 'HSBC Holdings'),
        ('0941.HK', 'China Mobile'),
        ('1299.HK', 'AIA Group'),
        ('0388.HK', 'Hong Kong Exchanges'),
        ('1398.HK', 'ICBC'),
        ('2318.HK', 'Ping An Insurance'),
        ('3690.HK', 'Meituan'),
    ]
    for symbol, name in hk_major:
        stocks.append({'symbol': symbol, 'name': name, 'exchange': 'HKEX', 'sector': '', 'industry': ''})

    # Cryptocurrencies
    cryptos = [
        ('BTC-USD', 'Bitcoin'), ('ETH-USD', 'Ethereum'), ('BNB-USD', 'Binance Coin'),
        ('XRP-USD', 'Ripple'), ('ADA-USD', 'Cardano'), ('DOGE-USD', 'Dogecoin'),
        ('SOL-USD', 'Solana'), ('DOT-USD', 'Polkadot'), ('MATIC-USD', 'Polygon'),
        ('AVAX-USD', 'Avalanche'), ('LINK-USD', 'Chainlink'), ('UNI-USD', 'Uniswap'),
    ]
    for symbol, name in cryptos:
        stocks.append({'symbol': symbol, 'name': name, 'exchange': 'CRYPTO', 'sector': '', 'industry': ''})

    # Major indices
    indices = [
        ('^GSPC', 'S&P 500'), ('^DJI', 'Dow Jones'), ('^IXIC', 'NASDAQ Composite'),
        ('^RUT', 'Russell 2000'), ('^FTSE', 'FTSE 100'), ('^GDAXI', 'DAX'),
        ('^JKSE', 'Jakarta Composite'), ('^HSI', 'Hang Seng'), ('^N225', 'Nikkei 225'),
    ]
    for symbol, name in indices:
        stocks.append({'symbol': symbol, 'name': name, 'exchange': 'INDEX', 'sector': '', 'industry': ''})

    print(f"✅ Got {len(stocks)} international/crypto/indices")
    return stocks

def build_database():
    """Build complete database"""
    print("=" * 70)
    print("🌍 BUILDING COMPLETE GLOBAL STOCK DATABASE")
    print("=" * 70)
    print()

    all_stocks = []

    # Get from all sources
    all_stocks.extend(get_nasdaq_all())
    all_stocks.extend(get_nyse_all())
    all_stocks.extend(get_idx_stocks())
    all_stocks.extend(get_international_and_crypto())

    # Remove duplicates by symbol
    seen = set()
    unique_stocks = []
    for stock in all_stocks:
        if stock['symbol'] not in seen:
            seen.add(stock['symbol'])
            unique_stocks.append(stock)

    print()
    print("=" * 70)
    print(f"📊 TOTAL STOCKS: {len(unique_stocks):,}")
    print("=" * 70)

    # Analyze size with compression
    data = {'success': True, 'count': len(unique_stocks), 'stocks': unique_stocks}

    json_str = json.dumps(data, separators=(',', ':'))
    json_bytes = json_str.encode('utf-8')

    import gzip
    gzipped = gzip.compress(json_bytes, compresslevel=9)
    brotli_compressed = brotli.compress(json_bytes, quality=11)

    print(f"\n📦 SIZE ANALYSIS:")
    print(f"   Uncompressed: {len(json_bytes):,} bytes ({len(json_bytes)//1024:,} KB)")
    print(f"   Gzipped: {len(gzipped):,} bytes ({len(gzipped)//1024:,} KB)")
    print(f"   Brotli: {len(brotli_compressed):,} bytes ({len(brotli_compressed)//1024:,} KB)")
    print(f"   Compression ratio: {len(json_bytes)/len(brotli_compressed):.1f}x")

    if len(brotli_compressed) > 4_500_000:
        print(f"\n⚠️  WARNING: {len(brotli_compressed)//1024//1024:.1f}MB exceeds Vercel 4.5MB limit!")
        print("   Consider reducing stock count or implementing pagination")
    elif len(brotli_compressed) > 1_000_000:
        print(f"\n⚠️  Large: {len(brotli_compressed)//1024}KB - may affect page load")
    else:
        print(f"\n✅ Perfect size for Vercel!")

    # Breakdown by exchange
    print(f"\n📊 BREAKDOWN BY EXCHANGE:")
    exchanges = {}
    for stock in unique_stocks:
        ex = stock['exchange']
        exchanges[ex] = exchanges.get(ex, 0) + 1

    for exchange, count in sorted(exchanges.items(), key=lambda x: -x[1]):
        print(f"   {exchange:15} {count:6,} stocks")

    # Save
    with open('complete_stock_database.json', 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\n💾 Saved to: complete_stock_database.json")
    print("=" * 70)
    print(f"🎉 DATABASE COMPLETE WITH {len(unique_stocks):,} STOCKS!")
    print("=" * 70)

    return unique_stocks

if __name__ == '__main__':
    stocks = build_database()
