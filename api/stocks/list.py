"""
Vercel serverless function to fetch complete stock list.
Endpoint: /api/stocks/list
Returns: JSON array of stocks with metadata (symbol, name, exchange, sector, industry)
"""

from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    """Serverless function handler for Vercel."""

    def do_GET(self):
        try:
            # Complete stock database with IDX focus - ~150 major stocks
            stocks = [
                # Indonesia - Banking (14 stocks)
                {"symbol": "BBCA.JK", "name": "Bank Central Asia", "exchange": "IDX", "sector": "Financial Services", "industry": "Banks"},
                {"symbol": "BMRI.JK", "name": "Bank Mandiri", "exchange": "IDX", "sector": "Financial Services", "industry": "Banks"},
                {"symbol": "BBRI.JK", "name": "Bank Rakyat Indonesia", "exchange": "IDX", "sector": "Financial Services", "industry": "Banks"},
                {"symbol": "BBNI.JK", "name": "Bank Negara Indonesia", "exchange": "IDX", "sector": "Financial Services", "industry": "Banks"},
                {"symbol": "BRIS.JK", "name": "Bank BRI Syariah", "exchange": "IDX", "sector": "Financial Services", "industry": "Banks"},
                {"symbol": "MEGA.JK", "name": "Bank Mega", "exchange": "IDX", "sector": "Financial Services", "industry": "Banks"},
                {"symbol": "BNII.JK", "name": "Bank Maybank Indonesia", "exchange": "IDX", "sector": "Financial Services", "industry": "Banks"},
                {"symbol": "NISP.JK", "name": "Bank OCBC NISP", "exchange": "IDX", "sector": "Financial Services", "industry": "Banks"},
                {"symbol": "PNBN.JK", "name": "Bank Pan Indonesia", "exchange": "IDX", "sector": "Financial Services", "industry": "Banks"},
                {"symbol": "BNGA.JK", "name": "Bank CIMB Niaga", "exchange": "IDX", "sector": "Financial Services", "industry": "Banks"},
                {"symbol": "BDMN.JK", "name": "Bank Danamon", "exchange": "IDX", "sector": "Financial Services", "industry": "Banks"},
                {"symbol": "BJTM.JK", "name": "Bank Jatim", "exchange": "IDX", "sector": "Financial Services", "industry": "Banks"},
                {"symbol": "BJBR.JK", "name": "BPD Jabar Banten", "exchange": "IDX", "sector": "Financial Services", "industry": "Banks"},
                {"symbol": "BACA.JK", "name": "Bank Capital", "exchange": "IDX", "sector": "Financial Services", "industry": "Banks"},

                # Indonesia - Telecom & Technology (7 stocks)
                {"symbol": "TLKM.JK", "name": "Telkom Indonesia", "exchange": "IDX", "sector": "Communication", "industry": "Telecom"},
                {"symbol": "EXCL.JK", "name": "XL Axiata", "exchange": "IDX", "sector": "Communication", "industry": "Telecom"},
                {"symbol": "ISAT.JK", "name": "Indosat Ooredoo", "exchange": "IDX", "sector": "Communication", "industry": "Telecom"},
                {"symbol": "GOTO.JK", "name": "GoTo Gojek Tokopedia", "exchange": "IDX", "sector": "Technology", "industry": "Internet"},
                {"symbol": "EMTK.JK", "name": "Elang Mahkota Teknologi", "exchange": "IDX", "sector": "Communication", "industry": "Media"},
                {"symbol": "MTEL.JK", "name": "Dayamitra Telekomunikasi", "exchange": "IDX", "sector": "Communication", "industry": "Telecom"},
                {"symbol": "FREN.JK", "name": "Smartfren Telecom", "exchange": "IDX", "sector": "Communication", "industry": "Telecom"},

                # Indonesia - Consumer Goods (13 stocks)
                {"symbol": "UNVR.JK", "name": "Unilever Indonesia", "exchange": "IDX", "sector": "Consumer Defensive", "industry": "Personal Products"},
                {"symbol": "INDF.JK", "name": "Indofood Sukses Makmur", "exchange": "IDX", "sector": "Consumer Defensive", "industry": "Packaged Foods"},
                {"symbol": "ICBP.JK", "name": "Indofood CBP", "exchange": "IDX", "sector": "Consumer Defensive", "industry": "Packaged Foods"},
                {"symbol": "KLBF.JK", "name": "Kalbe Farma", "exchange": "IDX", "sector": "Healthcare", "industry": "Pharmaceuticals"},
                {"symbol": "MYOR.JK", "name": "Mayora Indah", "exchange": "IDX", "sector": "Consumer Defensive", "industry": "Packaged Foods"},
                {"symbol": "ULTJ.JK", "name": "Ultra Jaya Milk", "exchange": "IDX", "sector": "Consumer Defensive", "industry": "Beverages"},
                {"symbol": "GGRM.JK", "name": "Gudang Garam", "exchange": "IDX", "sector": "Consumer Defensive", "industry": "Tobacco"},
                {"symbol": "HMSP.JK", "name": "HM Sampoerna", "exchange": "IDX", "sector": "Consumer Defensive", "industry": "Tobacco"},
                {"symbol": "WIIM.JK", "name": "Wismilak Inti Makmur", "exchange": "IDX", "sector": "Consumer Defensive", "industry": "Tobacco"},
                {"symbol": "DLTA.JK", "name": "Delta Djakarta", "exchange": "IDX", "sector": "Consumer Defensive", "industry": "Beverages"},
                {"symbol": "ROTI.JK", "name": "Nippon Indosari", "exchange": "IDX", "sector": "Consumer Defensive", "industry": "Packaged Foods"},
                {"symbol": "ADES.JK", "name": "Akasha Wira", "exchange": "IDX", "sector": "Consumer Defensive", "industry": "Beverages"},
                {"symbol": "CAMP.JK", "name": "Campina Ice Cream", "exchange": "IDX", "sector": "Consumer Defensive", "industry": "Packaged Foods"},

                # Indonesia - Automotive (6 stocks)
                {"symbol": "ASII.JK", "name": "Astra International", "exchange": "IDX", "sector": "Consumer Cyclical", "industry": "Auto Dealers"},
                {"symbol": "UNTR.JK", "name": "United Tractors", "exchange": "IDX", "sector": "Industrials", "industry": "Heavy Machinery"},
                {"symbol": "AUTO.JK", "name": "Astra Otoparts", "exchange": "IDX", "sector": "Consumer Cyclical", "industry": "Auto Parts"},
                {"symbol": "GJTL.JK", "name": "Gajah Tunggal", "exchange": "IDX", "sector": "Consumer Cyclical", "industry": "Auto Parts"},
                {"symbol": "IMAS.JK", "name": "Indomobil Sukses", "exchange": "IDX", "sector": "Consumer Cyclical", "industry": "Auto"},
                {"symbol": "SMSM.JK", "name": "Selamat Sempurna", "exchange": "IDX", "sector": "Consumer Cyclical", "industry": "Auto Parts"},

                # Indonesia - Mining & Energy (11 stocks)
                {"symbol": "ANTM.JK", "name": "Aneka Tambang", "exchange": "IDX", "sector": "Materials", "industry": "Mining"},
                {"symbol": "PTBA.JK", "name": "Bukit Asam", "exchange": "IDX", "sector": "Energy", "industry": "Coal"},
                {"symbol": "ADRO.JK", "name": "Adaro Energy", "exchange": "IDX", "sector": "Energy", "industry": "Coal"},
                {"symbol": "ITMG.JK", "name": "Indo Tambangraya", "exchange": "IDX", "sector": "Energy", "industry": "Coal"},
                {"symbol": "INDY.JK", "name": "Indika Energy", "exchange": "IDX", "sector": "Energy", "industry": "Coal"},
                {"symbol": "HRUM.JK", "name": "Harum Energy", "exchange": "IDX", "sector": "Energy", "industry": "Coal"},
                {"symbol": "PTRO.JK", "name": "Petrosea", "exchange": "IDX", "sector": "Energy", "industry": "Oil & Gas Services"},
                {"symbol": "MDKA.JK", "name": "Merdeka Copper Gold", "exchange": "IDX", "sector": "Materials", "industry": "Copper"},
                {"symbol": "TINS.JK", "name": "Timah", "exchange": "IDX", "sector": "Materials", "industry": "Mining"},
                {"symbol": "INCO.JK", "name": "Vale Indonesia", "exchange": "IDX", "sector": "Materials", "industry": "Nickel"},
                {"symbol": "DOID.JK", "name": "Delta Dunia Makmur", "exchange": "IDX", "sector": "Energy", "industry": "Oil & Gas Services"},

                # Indonesia - Property (9 stocks)
                {"symbol": "BSDE.JK", "name": "Bumi Serpong Damai", "exchange": "IDX", "sector": "Real Estate", "industry": "Development"},
                {"symbol": "PWON.JK", "name": "Pakuwon Jati", "exchange": "IDX", "sector": "Real Estate", "industry": "Development"},
                {"symbol": "SMRA.JK", "name": "Summarecon Agung", "exchange": "IDX", "sector": "Real Estate", "industry": "Development"},
                {"symbol": "CTRA.JK", "name": "Ciputra Development", "exchange": "IDX", "sector": "Real Estate", "industry": "Development"},
                {"symbol": "APLN.JK", "name": "Agung Podomoro Land", "exchange": "IDX", "sector": "Real Estate", "industry": "Development"},
                {"symbol": "LPKR.JK", "name": "Lippo Karawaci", "exchange": "IDX", "sector": "Real Estate", "industry": "Development"},
                {"symbol": "ASRI.JK", "name": "Alam Sutera Realty", "exchange": "IDX", "sector": "Real Estate", "industry": "Development"},
                {"symbol": "DUTI.JK", "name": "Duta Pertiwi", "exchange": "IDX", "sector": "Real Estate", "industry": "Development"},
                {"symbol": "PLIN.JK", "name": "Plaza Indonesia", "exchange": "IDX", "sector": "Real Estate", "industry": "Services"},

                # Indonesia - Construction (8 stocks)
                {"symbol": "SMGR.JK", "name": "Semen Indonesia", "exchange": "IDX", "sector": "Materials", "industry": "Cement"},
                {"symbol": "INTP.JK", "name": "Indocement", "exchange": "IDX", "sector": "Materials", "industry": "Cement"},
                {"symbol": "WTON.JK", "name": "Wijaya Karya Beton", "exchange": "IDX", "sector": "Materials", "industry": "Cement"},
                {"symbol": "WIKA.JK", "name": "Wijaya Karya", "exchange": "IDX", "sector": "Industrials", "industry": "Construction"},
                {"symbol": "WSKT.JK", "name": "Waskita Karya", "exchange": "IDX", "sector": "Industrials", "industry": "Construction"},
                {"symbol": "PTPP.JK", "name": "PP Persero", "exchange": "IDX", "sector": "Industrials", "industry": "Construction"},
                {"symbol": "ADHI.JK", "name": "Adhi Karya", "exchange": "IDX", "sector": "Industrials", "industry": "Construction"},
                {"symbol": "TOTL.JK", "name": "Total Bangun Persada", "exchange": "IDX", "sector": "Industrials", "industry": "Construction"},

                # Indonesia - Retail (6 stocks)
                {"symbol": "ACES.JK", "name": "Ace Hardware", "exchange": "IDX", "sector": "Consumer Cyclical", "industry": "Retail"},
                {"symbol": "ERAA.JK", "name": "Erajaya Swasembada", "exchange": "IDX", "sector": "Consumer Cyclical", "industry": "Retail"},
                {"symbol": "MAPI.JK", "name": "Mitra Adiperkasa", "exchange": "IDX", "sector": "Consumer Cyclical", "industry": "Department Stores"},
                {"symbol": "LPPF.JK", "name": "Matahari Department", "exchange": "IDX", "sector": "Consumer Cyclical", "industry": "Department Stores"},
                {"symbol": "RANC.JK", "name": "Sumber Alfaria (Alfamart)", "exchange": "IDX", "sector": "Consumer Defensive", "industry": "Grocery"},
                {"symbol": "AMRT.JK", "name": "Sumber Alfaria Trijaya", "exchange": "IDX", "sector": "Consumer Defensive", "industry": "Grocery"},

                # Indonesia - Pharma (5 stocks)
                {"symbol": "KAEF.JK", "name": "Kimia Farma", "exchange": "IDX", "sector": "Healthcare", "industry": "Pharmaceuticals"},
                {"symbol": "INAF.JK", "name": "Indofarma", "exchange": "IDX", "sector": "Healthcare", "industry": "Pharmaceuticals"},
                {"symbol": "DVLA.JK", "name": "Darya-Varia", "exchange": "IDX", "sector": "Healthcare", "industry": "Pharmaceuticals"},
                {"symbol": "PYFA.JK", "name": "Pyridam Farma", "exchange": "IDX", "sector": "Healthcare", "industry": "Pharmaceuticals"},
                {"symbol": "SIDO.JK", "name": "Sido Muncul", "exchange": "IDX", "sector": "Healthcare", "industry": "Pharmaceuticals"},

                # Indonesia - Transportation & Others (6 stocks)
                {"symbol": "BIRD.JK", "name": "Blue Bird", "exchange": "IDX", "sector": "Industrials", "industry": "Transportation"},
                {"symbol": "JSMR.JK", "name": "Jasa Marga", "exchange": "IDX", "sector": "Industrials", "industry": "Infrastructure"},
                {"symbol": "TPIA.JK", "name": "Chandra Asri", "exchange": "IDX", "sector": "Materials", "industry": "Chemicals"},
                {"symbol": "SCMA.JK", "name": "Surya Citra Media", "exchange": "IDX", "sector": "Communication", "industry": "Media"},
                {"symbol": "MNCN.JK", "name": "Media Nusantara", "exchange": "IDX", "sector": "Communication", "industry": "Media"},
                {"symbol": "VIVA.JK", "name": "Visi Media Asia", "exchange": "IDX", "sector": "Communication", "industry": "Media"},

                # US - Technology (17 stocks)
                {"symbol": "AAPL", "name": "Apple Inc", "exchange": "NASDAQ", "sector": "Technology", "industry": "Consumer Electronics"},
                {"symbol": "MSFT", "name": "Microsoft", "exchange": "NASDAQ", "sector": "Technology", "industry": "Software"},
                {"symbol": "GOOGL", "name": "Alphabet Class A", "exchange": "NASDAQ", "sector": "Communication", "industry": "Internet"},
                {"symbol": "AMZN", "name": "Amazon.com", "exchange": "NASDAQ", "sector": "Consumer Cyclical", "industry": "Internet Retail"},
                {"symbol": "NVDA", "name": "NVIDIA", "exchange": "NASDAQ", "sector": "Technology", "industry": "Semiconductors"},
                {"symbol": "META", "name": "Meta Platforms", "exchange": "NASDAQ", "sector": "Communication", "industry": "Internet"},
                {"symbol": "TSLA", "name": "Tesla", "exchange": "NASDAQ", "sector": "Consumer Cyclical", "industry": "Auto"},
                {"symbol": "NFLX", "name": "Netflix", "exchange": "NASDAQ", "sector": "Communication", "industry": "Entertainment"},
                {"symbol": "AMD", "name": "Advanced Micro Devices", "exchange": "NASDAQ", "sector": "Technology", "industry": "Semiconductors"},
                {"symbol": "INTC", "name": "Intel", "exchange": "NASDAQ", "sector": "Technology", "industry": "Semiconductors"},
                {"symbol": "ORCL", "name": "Oracle", "exchange": "NYSE", "sector": "Technology", "industry": "Software"},
                {"symbol": "CRM", "name": "Salesforce", "exchange": "NYSE", "sector": "Technology", "industry": "Software"},
                {"symbol": "ADBE", "name": "Adobe", "exchange": "NASDAQ", "sector": "Technology", "industry": "Software"},
                {"symbol": "CSCO", "name": "Cisco Systems", "exchange": "NASDAQ", "sector": "Technology", "industry": "Networking"},
                {"symbol": "AVGO", "name": "Broadcom", "exchange": "NASDAQ", "sector": "Technology", "industry": "Semiconductors"},
                {"symbol": "QCOM", "name": "QUALCOMM", "exchange": "NASDAQ", "sector": "Technology", "industry": "Semiconductors"},
                {"symbol": "TXN", "name": "Texas Instruments", "exchange": "NASDAQ", "sector": "Technology", "industry": "Semiconductors"},

                # US - Finance (8 stocks)
                {"symbol": "JPM", "name": "JPMorgan Chase", "exchange": "NYSE", "sector": "Financial Services", "industry": "Banks"},
                {"symbol": "BAC", "name": "Bank of America", "exchange": "NYSE", "sector": "Financial Services", "industry": "Banks"},
                {"symbol": "WFC", "name": "Wells Fargo", "exchange": "NYSE", "sector": "Financial Services", "industry": "Banks"},
                {"symbol": "V", "name": "Visa", "exchange": "NYSE", "sector": "Financial Services", "industry": "Credit Services"},
                {"symbol": "MA", "name": "Mastercard", "exchange": "NYSE", "sector": "Financial Services", "industry": "Credit Services"},
                {"symbol": "GS", "name": "Goldman Sachs", "exchange": "NYSE", "sector": "Financial Services", "industry": "Investment Banking"},
                {"symbol": "MS", "name": "Morgan Stanley", "exchange": "NYSE", "sector": "Financial Services", "industry": "Investment Banking"},
                {"symbol": "AXP", "name": "American Express", "exchange": "NYSE", "sector": "Financial Services", "industry": "Credit Services"},

                # US - Consumer (9 stocks)
                {"symbol": "WMT", "name": "Walmart", "exchange": "NYSE", "sector": "Consumer Defensive", "industry": "Discount Stores"},
                {"symbol": "HD", "name": "Home Depot", "exchange": "NYSE", "sector": "Consumer Cyclical", "industry": "Home Improvement"},
                {"symbol": "MCD", "name": "McDonald's", "exchange": "NYSE", "sector": "Consumer Cyclical", "industry": "Restaurants"},
                {"symbol": "NKE", "name": "Nike", "exchange": "NYSE", "sector": "Consumer Cyclical", "industry": "Apparel"},
                {"symbol": "SBUX", "name": "Starbucks", "exchange": "NASDAQ", "sector": "Consumer Cyclical", "industry": "Restaurants"},
                {"symbol": "KO", "name": "Coca-Cola", "exchange": "NYSE", "sector": "Consumer Defensive", "industry": "Beverages"},
                {"symbol": "PEP", "name": "PepsiCo", "exchange": "NASDAQ", "sector": "Consumer Defensive", "industry": "Beverages"},
                {"symbol": "COST", "name": "Costco", "exchange": "NASDAQ", "sector": "Consumer Defensive", "industry": "Discount Stores"},
                {"symbol": "TGT", "name": "Target", "exchange": "NYSE", "sector": "Consumer Defensive", "industry": "Discount Stores"},

                # US - Healthcare (6 stocks)
                {"symbol": "JNJ", "name": "Johnson & Johnson", "exchange": "NYSE", "sector": "Healthcare", "industry": "Pharmaceuticals"},
                {"symbol": "UNH", "name": "UnitedHealth", "exchange": "NYSE", "sector": "Healthcare", "industry": "Insurance"},
                {"symbol": "PFE", "name": "Pfizer", "exchange": "NYSE", "sector": "Healthcare", "industry": "Pharmaceuticals"},
                {"symbol": "ABBV", "name": "AbbVie", "exchange": "NYSE", "sector": "Healthcare", "industry": "Pharmaceuticals"},
                {"symbol": "TMO", "name": "Thermo Fisher", "exchange": "NYSE", "sector": "Healthcare", "industry": "Equipment"},
                {"symbol": "LLY", "name": "Eli Lilly", "exchange": "NYSE", "sector": "Healthcare", "industry": "Pharmaceuticals"},

                # US - Energy (2 stocks)
                {"symbol": "XOM", "name": "Exxon Mobil", "exchange": "NYSE", "sector": "Energy", "industry": "Oil & Gas"},
                {"symbol": "CVX", "name": "Chevron", "exchange": "NYSE", "sector": "Energy", "industry": "Oil & Gas"},

                # UK (6 stocks)
                {"symbol": "BP.L", "name": "BP plc", "exchange": "LSE", "sector": "Energy", "industry": "Oil & Gas"},
                {"symbol": "SHEL.L", "name": "Shell plc", "exchange": "LSE", "sector": "Energy", "industry": "Oil & Gas"},
                {"symbol": "HSBA.L", "name": "HSBC Holdings", "exchange": "LSE", "sector": "Financial Services", "industry": "Banks"},
                {"symbol": "ULVR.L", "name": "Unilever", "exchange": "LSE", "sector": "Consumer Defensive", "industry": "Personal Products"},
                {"symbol": "AZN.L", "name": "AstraZeneca", "exchange": "LSE", "sector": "Healthcare", "industry": "Pharmaceuticals"},
                {"symbol": "GSK.L", "name": "GSK", "exchange": "LSE", "sector": "Healthcare", "industry": "Pharmaceuticals"},

                # China/HK (5 stocks)
                {"symbol": "BABA", "name": "Alibaba", "exchange": "NYSE", "sector": "Consumer Cyclical", "industry": "Internet Retail"},
                {"symbol": "0700.HK", "name": "Tencent", "exchange": "HKEX", "sector": "Communication", "industry": "Internet"},
                {"symbol": "9988.HK", "name": "Alibaba HK", "exchange": "HKEX", "sector": "Consumer Cyclical", "industry": "Internet Retail"},
                {"symbol": "0941.HK", "name": "China Mobile", "exchange": "HKEX", "sector": "Communication", "industry": "Telecom"},
                {"symbol": "1299.HK", "name": "AIA Group", "exchange": "HKEX", "sector": "Financial Services", "industry": "Insurance"},

                # Japan (5 stocks)
                {"symbol": "7203.T", "name": "Toyota Motor", "exchange": "TSE", "sector": "Consumer Cyclical", "industry": "Auto"},
                {"symbol": "6758.T", "name": "Sony Group", "exchange": "TSE", "sector": "Technology", "industry": "Electronics"},
                {"symbol": "9984.T", "name": "SoftBank", "exchange": "TSE", "sector": "Communication", "industry": "Telecom"},
                {"symbol": "6861.T", "name": "Keyence", "exchange": "TSE", "sector": "Technology", "industry": "Instruments"},
                {"symbol": "7974.T", "name": "Nintendo", "exchange": "TSE", "sector": "Communication", "industry": "Gaming"},

                # Singapore (3 stocks)
                {"symbol": "D05.SI", "name": "DBS Group", "exchange": "SGX", "sector": "Financial Services", "industry": "Banks"},
                {"symbol": "O39.SI", "name": "OCBC Bank", "exchange": "SGX", "sector": "Financial Services", "industry": "Banks"},
                {"symbol": "U11.SI", "name": "UOB", "exchange": "SGX", "sector": "Financial Services", "industry": "Banks"},

                # Malaysia (3 stocks)
                {"symbol": "1155.KL", "name": "Maybank", "exchange": "KLSE", "sector": "Financial Services", "industry": "Banks"},
                {"symbol": "5183.KL", "name": "Public Bank", "exchange": "KLSE", "sector": "Financial Services", "industry": "Banks"},
                {"symbol": "6012.KL", "name": "Maxis", "exchange": "KLSE", "sector": "Communication", "industry": "Telecom"},

                # Thailand (2 stocks)
                {"symbol": "ADVANC.BK", "name": "Advanced Info Service", "exchange": "SET", "sector": "Communication", "industry": "Telecom"},
                {"symbol": "PTT.BK", "name": "PTT Public", "exchange": "SET", "sector": "Energy", "industry": "Oil & Gas"},
            ]

            response = {
                "success": True,
                "count": len(stocks),
                "stocks": stocks
            }

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Cache-Control', 'public, max-age=86400')
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
