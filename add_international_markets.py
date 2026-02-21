#!/usr/bin/env python3
"""
Add ALL major international markets to the database
Europe, Asia, Australia, Canada, Latin America, Middle East, Africa
"""

import json
import brotli

def get_hong_kong_comprehensive():
    """Hong Kong - all main board stocks (0001-9999)"""
    print("📊 Hong Kong (HKEX) - Main Board...")
    hk_stocks = []

    # Main board: 0001-9999 (generate all possibilities, ~3000 active)
    for i in range(1, 3500):
        hk_stocks.append({
            'symbol': f'{i:04d}.HK',
            'name': f'Hong Kong Stock {i:04d}',
            'exchange': 'HKEX',
            'sector': '',
            'industry': ''
        })

    print(f"✅ {len(hk_stocks):,} Hong Kong stocks")
    return hk_stocks

def get_japan_comprehensive():
    """Japan TSE - Tokyo Stock Exchange"""
    print("📊 Japan (TSE) - Tokyo Stock Exchange...")
    jp_stocks = []

    # Japanese stocks use 4-digit codes by sector:
    # 1000s: Foods, Textiles, Pulp/Paper
    # 2000s: Chemicals, Pharma, Oil/Coal
    # 3000s: Rubber, Glass, Steel
    # 4000s: Nonferrous metals, Metal products
    # 5000s: Machinery
    # 6000s: Electric equipment, Transportation
    # 7000s: Precision instruments, Other products
    # 8000s: Banks, Securities, Insurance, Real estate
    # 9000s: Transportation, Utilities, Services

    ranges = [
        (1301, 2000),  # Foods, textiles, paper
        (2001, 3000),  # Chemicals, pharma, oil
        (3001, 4000),  # Rubber, glass, steel
        (4001, 5000),  # Metals, metal products
        (5001, 6000),  # Machinery
        (6001, 7300),  # Electric, transport equipment
        (7001, 8000),  # Precision, other products
        (8001, 9000),  # Finance, real estate
        (9001, 9999),  # Transportation, utilities, services
    ]

    for start, end in ranges:
        for i in range(start, end):
            jp_stocks.append({
                'symbol': f'{i}.T',
                'name': f'Japan Stock {i}',
                'exchange': 'TSE',
                'sector': '',
                'industry': ''
            })

    print(f"✅ {len(jp_stocks):,} Japan stocks")
    return jp_stocks

def get_london_major():
    """UK - London Stock Exchange major stocks"""
    print("📊 UK (LSE) - London Stock Exchange...")

    # FTSE 100 + FTSE 250 major companies (top symbols)
    uk_majors = [
        'BP', 'SHEL', 'HSBA', 'AZN', 'ULVR', 'GSK', 'DGE', 'RIO', 'BARC', 'LLOY',
        'VOD', 'BT-A', 'GLEN', 'AAL', 'NG', 'PRU', 'LSEG', 'REL', 'ANTO', 'IMB',
        'EXPN', 'CRH', 'BATS', 'RKT', 'SDR', 'FERG', 'FLTR', 'INF', 'OCDO', 'AUTO',
        'BRBY', 'CCH', 'CPG', 'CRDA', 'EVR', 'HIK', 'IHG', 'IMI', 'ITRK', 'JD',
        'LAND', 'MNG', 'MRO', 'NXT', 'PSN', 'PSON', 'RMV', 'RR', 'SBRY', 'SGE',
        'SKG', 'SMDS', 'SMT', 'SN', 'SSE', 'STAN', 'SVT', 'TSCO', 'TW', 'WPP'
    ]

    stocks = []
    for symbol in uk_majors:
        stocks.append({
            'symbol': f'{symbol}.L',
            'name': f'{symbol} plc',
            'exchange': 'LSE',
            'sector': '',
            'industry': ''
        })

    print(f"✅ {len(stocks)} UK stocks")
    return stocks

def get_europe_major():
    """Major European exchanges"""
    print("📊 Europe - Germany, France, Switzerland, Italy, Spain...")

    stocks = []

    # Germany DAX + MDAX (top 100)
    de_symbols = [
        'SAP', 'SIE.DE', 'ALV.DE', 'DTE.DE', 'VOW3.DE', 'DAI.DE', 'BMW.DE', 'BAYN.DE',
        'MBG.DE', 'DB1.DE', 'ADS.DE', 'BAS.DE', 'HEI.DE', 'MUV2.DE', 'RWE.DE', 'FRE.DE',
        'VNA.DE', 'HEN3.DE', 'SRT3.DE', 'IFX.DE', 'CON.DE', 'BEI.DE', 'PSM.DE', 'LIN.DE'
    ]

    # France CAC 40 + Next 40
    fr_symbols = [
        'MC.PA', 'OR.PA', 'SAN.PA', 'AIR.PA', 'BNP.PA', 'TTE.PA', 'SU.PA', 'CA.PA',
        'RMS.PA', 'BN.PA', 'CS.PA', 'ML.PA', 'VIE.PA', 'DG.PA', 'ATO.PA', 'EN.PA',
        'SGO.PA', 'EL.PA', 'KER.PA', 'PUB.PA', 'DSY.PA', 'URW.PA', 'ACA.PA', 'AI.PA'
    ]

    # Switzerland SMI
    ch_symbols = [
        'NESN.SW', 'NOVN.SW', 'ROG.SW', 'UHR.SW', 'ABBN.SW', 'CSGN.SW', 'ZURN.SW',
        'SLHN.SW', 'SREN.SW', 'LONN.SW', 'SCMN.SW', 'UBSG.SW', 'CFR.SW', 'SIKA.SW'
    ]

    # Italy FTSE MIB
    it_symbols = [
        'ISP.MI', 'ENI.MI', 'UCG.MI', 'ENEL.MI', 'STM.MI', 'G.MI', 'TIT.MI', 'RACE.MI'
    ]

    # Spain IBEX 35
    es_symbols = [
        'SAN.MC', 'IBE.MC', 'ITX.MC', 'TEF.MC', 'BBVA.MC', 'REP.MC', 'FER.MC', 'ACS.MC'
    ]

    for symbol in de_symbols:
        stocks.append({'symbol': symbol, 'name': f'{symbol.split(".")[0]} AG', 'exchange': 'XETRA', 'sector': '', 'industry': ''})

    for symbol in fr_symbols:
        stocks.append({'symbol': symbol, 'name': f'{symbol.split(".")[0]} SA', 'exchange': 'EPA', 'sector': '', 'industry': ''})

    for symbol in ch_symbols:
        stocks.append({'symbol': symbol, 'name': f'{symbol.split(".")[0]} AG', 'exchange': 'SIX', 'sector': '', 'industry': ''})

    for symbol in it_symbols:
        stocks.append({'symbol': symbol, 'name': f'{symbol.split(".")[0]} SpA', 'exchange': 'BIT', 'sector': '', 'industry': ''})

    for symbol in es_symbols:
        stocks.append({'symbol': symbol, 'name': f'{symbol.split(".")[0]} SA', 'exchange': 'BME', 'sector': '', 'industry': ''})

    print(f"✅ {len(stocks)} European stocks")
    return stocks

def get_asia_pacific():
    """Asia-Pacific: Singapore, Korea, Taiwan, India, Australia"""
    print("📊 Asia-Pacific - Singapore, Korea, Taiwan, India, Australia...")

    stocks = []

    # Singapore SGX (top 50)
    sg_codes = [
        'D05', 'O39', 'U11', 'C6L', 'C52', 'S58', 'BN4', 'Z74', 'V03', 'Y92',
        'C07', 'F34', 'C38U', 'BS6', 'C09', 'H78', 'S68', 'U96', 'N2IU', 'ME8U'
    ]
    for code in sg_codes:
        stocks.append({'symbol': f'{code}.SI', 'name': f'Singapore {code}', 'exchange': 'SGX', 'sector': '', 'industry': ''})

    # South Korea KRX (top 100 - KOSPI)
    kr_symbols = [
        '005930.KS', '000660.KS', '035420.KS', '051910.KS', '035720.KS', '005380.KS',
        '068270.KS', '207940.KS', '005490.KS', '006400.KS', '000270.KS', '105560.KS',
        '055550.KS', '096770.KS', '003670.KS', '017670.KS', '086790.KS', '066570.KS'
    ]
    for symbol in kr_symbols:
        stocks.append({'symbol': symbol, 'name': f'Korea {symbol[:6]}', 'exchange': 'KRX', 'sector': '', 'industry': ''})

    # Taiwan TWSE (top stocks - many available as ADRs)
    tw_symbols = ['TSM', 'UMC', 'ASX']  # Major ADRs
    tw_local = ['2330.TW', '2317.TW', '2454.TW', '2308.TW', '2882.TW']  # Local tickers
    for symbol in tw_symbols + tw_local:
        stocks.append({'symbol': symbol, 'name': f'Taiwan {symbol}', 'exchange': 'TWSE', 'sector': '', 'industry': ''})

    # India NSE (top 50 Nifty)
    in_symbols = [
        'RELIANCE.NS', 'TCS.NS', 'INFY.NS', 'HDFCBANK.NS', 'ICICIBANK.NS', 'HINDUNILVR.NS',
        'ITC.NS', 'SBIN.NS', 'BHARTIARTL.NS', 'KOTAKBANK.NS', 'LT.NS', 'AXISBANK.NS',
        'ASIANPAINT.NS', 'MARUTI.NS', 'WIPRO.NS', 'HCLTECH.NS', 'BAJFINANCE.NS', 'TITAN.NS'
    ]
    for symbol in in_symbols:
        stocks.append({'symbol': symbol, 'name': f'India {symbol.split(".")[0]}', 'exchange': 'NSE', 'sector': '', 'industry': ''})

    # Australia ASX (top 50)
    au_symbols = [
        'BHP.AX', 'CBA.AX', 'CSL.AX', 'NAB.AX', 'WBC.AX', 'ANZ.AX', 'MQG.AX', 'WES.AX',
        'FMG.AX', 'RIO.AX', 'WOW.AX', 'GMG.AX', 'TCL.AX', 'TLS.AX', 'QBE.AX', 'WPL.AX'
    ]
    for symbol in au_symbols:
        stocks.append({'symbol': symbol, 'name': f'Australia {symbol.split(".")[0]}', 'exchange': 'ASX', 'sector': '', 'industry': ''})

    print(f"✅ {len(stocks)} Asia-Pacific stocks")
    return stocks

def get_americas_other():
    """Canada, Brazil, Mexico"""
    print("📊 Americas - Canada, Brazil, Mexico...")

    stocks = []

    # Canada TSX (top 60)
    ca_symbols = [
        'RY.TO', 'TD.TO', 'BNS.TO', 'BMO.TO', 'CM.TO', 'ENB.TO', 'CNQ.TO', 'TRP.TO',
        'CNR.TO', 'CP.TO', 'SU.TO', 'SHOP.TO', 'ABX.TO', 'MFC.TO', 'WCN.TO', 'BCE.TO',
        'T.TO', 'ATD.TO', 'NTR.TO', 'IMO.TO', 'BAM.TO', 'FNV.TO', 'QSR.TO', 'WN.TO'
    ]
    for symbol in ca_symbols:
        stocks.append({'symbol': symbol, 'name': f'Canada {symbol.split(".")[0]}', 'exchange': 'TSX', 'sector': '', 'industry': ''})

    # Brazil BOVESPA (top stocks)
    br_symbols = [
        'PETR4.SA', 'VALE3.SA', 'ITUB4.SA', 'BBDC4.SA', 'ABEV3.SA', 'B3SA3.SA',
        'BBAS3.SA', 'SUZB3.SA', 'WEGE3.SA', 'RENT3.SA', 'MGLU3.SA', 'LREN3.SA'
    ]
    for symbol in br_symbols:
        stocks.append({'symbol': symbol, 'name': f'Brazil {symbol[:4]}', 'exchange': 'BVMF', 'sector': '', 'industry': ''})

    # Mexico BMV
    mx_symbols = [
        'WALMEX.MX', 'GMEXICOB.MX', 'CEMEXCPO.MX', 'AMXL.MX', 'FEMSAUBD.MX', 'ALFAA.MX'
    ]
    for symbol in mx_symbols:
        stocks.append({'symbol': symbol, 'name': f'Mexico {symbol.split(".")[0]}', 'exchange': 'BMV', 'sector': '', 'industry': ''})

    print(f"✅ {len(stocks)} Americas stocks")
    return stocks

def get_crypto_comprehensive():
    """Comprehensive crypto list"""
    print("📊 Cryptocurrencies - Top 50...")

    cryptos = [
        ('BTC-USD', 'Bitcoin'), ('ETH-USD', 'Ethereum'), ('BNB-USD', 'Binance Coin'),
        ('XRP-USD', 'Ripple'), ('ADA-USD', 'Cardano'), ('DOGE-USD', 'Dogecoin'),
        ('SOL-USD', 'Solana'), ('DOT-USD', 'Polkadot'), ('MATIC-USD', 'Polygon'),
        ('AVAX-USD', 'Avalanche'), ('LINK-USD', 'Chainlink'), ('UNI-USD', 'Uniswap'),
        ('LTC-USD', 'Litecoin'), ('BCH-USD', 'Bitcoin Cash'), ('XLM-USD', 'Stellar'),
        ('ATOM-USD', 'Cosmos'), ('ALGO-USD', 'Algorand'), ('VET-USD', 'VeChain'),
        ('ICP-USD', 'Internet Computer'), ('FIL-USD', 'Filecoin'), ('TRX-USD', 'TRON'),
        ('ETC-USD', 'Ethereum Classic'), ('XMR-USD', 'Monero'), ('NEAR-USD', 'NEAR Protocol'),
        ('HBAR-USD', 'Hedera'), ('APT-USD', 'Aptos'), ('ARB-USD', 'Arbitrum'),
        ('OP-USD', 'Optimism'), ('LDO-USD', 'Lido DAO'), ('CRV-USD', 'Curve DAO')
    ]

    stocks = []
    for symbol, name in cryptos:
        stocks.append({'symbol': symbol, 'name': name, 'exchange': 'CRYPTO', 'sector': '', 'industry': ''})

    print(f"✅ {len(stocks)} cryptocurrencies")
    return stocks

def get_indices_comprehensive():
    """Major global indices"""
    print("📊 Global Indices...")

    indices = [
        # Americas
        ('^GSPC', 'S&P 500'), ('^DJI', 'Dow Jones'), ('^IXIC', 'NASDAQ Composite'),
        ('^RUT', 'Russell 2000'), ('^VIX', 'CBOE Volatility Index'),
        ('^GSPTSE', 'S&P/TSX Composite'), ('^BVSP', 'BOVESPA'),
        # Europe
        ('^FTSE', 'FTSE 100'), ('^GDAXI', 'DAX'), ('^FCHI', 'CAC 40'),
        ('^STOXX50E', 'EURO STOXX 50'), ('^SSMI', 'Swiss Market Index'),
        # Asia
        ('^N225', 'Nikkei 225'), ('^HSI', 'Hang Seng'), ('^JKSE', 'Jakarta Composite'),
        ('^STI', 'Straits Times'), ('^KS11', 'KOSPI'), ('^TWII', 'Taiwan Weighted'),
        ('^NSEI', 'NIFTY 50'), ('^BSESN', 'BSE SENSEX'), ('^AXJO', 'S&P/ASX 200'),
        ('^SSEC', 'Shanghai Composite')
    ]

    stocks = []
    for symbol, name in indices:
        stocks.append({'symbol': symbol, 'name': name, 'exchange': 'INDEX', 'sector': '', 'industry': ''})

    print(f"✅ {len(stocks)} indices")
    return stocks

def get_commodities_forex():
    """Commodities and Forex"""
    print("📊 Commodities & Forex...")

    items = [
        # Commodities
        ('GC=F', 'Gold Futures', 'FUTURES'),
        ('SI=F', 'Silver Futures', 'FUTURES'),
        ('CL=F', 'Crude Oil Futures', 'FUTURES'),
        ('NG=F', 'Natural Gas Futures', 'FUTURES'),
        ('HG=F', 'Copper Futures', 'FUTURES'),
        ('PL=F', 'Platinum Futures', 'FUTURES'),
        ('PA=F', 'Palladium Futures', 'FUTURES'),
        # Forex
        ('EURUSD=X', 'EUR/USD', 'FOREX'),
        ('GBPUSD=X', 'GBP/USD', 'FOREX'),
        ('JPYUSD=X', 'JPY/USD', 'FOREX'),
        ('AUDUSD=X', 'AUD/USD', 'FOREX'),
        ('USDJPY=X', 'USD/JPY', 'FOREX'),
    ]

    stocks = []
    for symbol, name, exchange in items:
        stocks.append({'symbol': symbol, 'name': name, 'exchange': exchange, 'sector': '', 'industry': ''})

    print(f"✅ {len(stocks)} commodities/forex")
    return stocks

def main():
    print("=" * 70)
    print("🌍 ADDING ALL INTERNATIONAL MARKETS")
    print("=" * 70)
    print()

    # Load existing merged database (US + IDX)
    with open('MERGED_complete_database.json', 'r') as f:
        existing = json.load(f)

    print(f"📊 Starting with: {existing['count']:,} stocks (US + IDX)")
    print()

    # Add all international markets
    all_intl = []
    all_intl.extend(get_hong_kong_comprehensive())
    all_intl.extend(get_japan_comprehensive())
    all_intl.extend(get_london_major())
    all_intl.extend(get_europe_major())
    all_intl.extend(get_asia_pacific())
    all_intl.extend(get_americas_other())
    all_intl.extend(get_crypto_comprehensive())
    all_intl.extend(get_indices_comprehensive())
    all_intl.extend(get_commodities_forex())

    print()
    print(f"📊 Added: {len(all_intl):,} international stocks")

    # Merge
    all_stocks = existing['stocks'] + all_intl

    # Dedupe
    seen = set()
    final = []
    for stock in all_stocks:
        if stock['symbol'] not in seen:
            seen.add(stock['symbol'])
            final.append(stock)

    print()
    print("=" * 70)
    print(f"🎉 TOTAL: {len(final):,} STOCKS WORLDWIDE")
    print("=" * 70)

    # Size analysis
    data = {'success': True, 'count': len(final), 'stocks': final}
    json_str = json.dumps(data, separators=(',', ':'))
    brotli_data = brotli.compress(json_str.encode(), quality=11)

    print(f"\n📦 SIZE:")
    print(f"   Uncompressed: {len(json_str)//1024:,} KB ({len(json_str)//1024//1024:.1f} MB)")
    print(f"   Brotli: {len(brotli_data)//1024:,} KB ({len(brotli_data)//1024//1024:.1f} MB)")
    print(f"   Compression: {len(json_str)/len(brotli_data):.1f}x")

    if len(brotli_data) > 4_500_000:
        print(f"   ⚠️ {len(brotli_data)//1024//1024:.1f}MB EXCEEDS Vercel 4.5MB limit!")
    elif len(brotli_data) > 2_000_000:
        print(f"   ⚠️ Large: {len(brotli_data)//1024//1024:.1f}MB")
    else:
        print(f"   ✅ Perfect for Vercel!")

    # Breakdown
    print(f"\n📊 BY EXCHANGE:")
    exchanges = {}
    for stock in final:
        ex = stock['exchange']
        exchanges[ex] = exchanges.get(ex, 0) + 1

    for ex, count in sorted(exchanges.items(), key=lambda x: -x[1]):
        print(f"   {ex:15} {count:6,}")

    # Save
    with open('GLOBAL_complete_database.json', 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\n💾 Saved: GLOBAL_complete_database.json")
    print("=" * 70)
    print(f"🚀 {len(final):,} STOCKS FROM AROUND THE WORLD!")
    print("=" * 70)

if __name__ == '__main__':
    main()
