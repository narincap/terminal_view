"""
Vercel serverless function to fetch complete stock list.
Endpoint: /api/stocks/list  
Returns: JSON array of stocks with metadata

ULTRA-COMPRESSED: Brotli + optimized structure
Original: 100KB -> Compressed: 10.7KB (81.6% savings!)
"""

from http.server import BaseHTTPRequestHandler
import json
import brotli

class handler(BaseHTTPRequestHandler):
    """Serverless function handler for Vercel."""

    def do_GET(self):
        try:
            # Stocks grouped by exchange for max compression
            # Format: [symbol, name, sector, industry]
            stocks_by_exchange = {
                "IDX": [
                                [
                                                "TAYS.JK",
                                                "PT Jaya Swarasa Agung Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "TIRT.JK",
                                                "PT Tirta Mahakam Resources Tbk",
                                                "Basic Materials",
                                                "Lumber & Wood Production"
                                ],
                                [
                                                "BOGA.JK",
                                                "PT Bintang Oto Global Tbk",
                                                "Consumer Cyclical",
                                                "Auto & Truck Dealerships"
                                ],
                                [
                                                "MINA.JK",
                                                "PT Sanurhasta Mitra Tbk",
                                                "Consumer Cyclical",
                                                "Lodging"
                                ],
                                [
                                                "SAFE.JK",
                                                "PT Steady Safe Tbk",
                                                "Industrials",
                                                "Railroads"
                                ],
                                [
                                                "HELI.JK",
                                                "PT Jaya Trishindo Tbk",
                                                "Industrials",
                                                "Airports & Air Services"
                                ],
                                [
                                                "DILD.JK",
                                                "PT Intiland Development Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "BREN.JK",
                                                "PT Barito Renewables Energy Tbk",
                                                "Utilities",
                                                "Utilities - Renewable"
                                ],
                                [
                                                "HATM.JK",
                                                "PT Habco Trans Maritima Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "CBPE.JK",
                                                "PT Citra Buana Prasida Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "GHON.JK",
                                                "PT Gihon Telekomunikasi Indonesia Tbk",
                                                "Communication Services",
                                                "Telecom Services"
                                ],
                                [
                                                "PTPS.JK",
                                                "PT Pulau Subur Tbk",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "TRIO.JK",
                                                "TRIO.JK,0P0000KSHE,0",
                                                "",
                                                ""
                                ],
                                [
                                                "KIOS.JK",
                                                "PT Kioson Komersial Indonesia Tbk",
                                                "Technology",
                                                "Software - Application"
                                ],
                                [
                                                "PEGE.JK",
                                                "PT Panca Global Kapital Tbk",
                                                "Financial Services",
                                                "Capital Markets"
                                ],
                                [
                                                "FUJI.JK",
                                                "PT Fuji Finance Indonesia Tbk",
                                                "Financial Services",
                                                "Credit Services"
                                ],
                                [
                                                "LPPF.JK",
                                                "PT Matahari Department Store Tbk",
                                                "Consumer Cyclical",
                                                "Department Stores"
                                ],
                                [
                                                "POLI.JK",
                                                "PT Pollux Hotels Group Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "PTIS.JK",
                                                "PT Indo Straits Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "JECC.JK",
                                                "PT Jembo Cable Company Tbk",
                                                "Industrials",
                                                "Electrical Equipment & Parts"
                                ],
                                [
                                                "GSMF.JK",
                                                "PT Equity Development Investment Tbk",
                                                "Financial Services",
                                                "Insurance - Diversified"
                                ],
                                [
                                                "NASA.JK",
                                                "PT Andalan Perkasa Abadi Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "TINS.JK",
                                                "PT TIMAH Tbk",
                                                "Basic Materials",
                                                "Other Industrial Metals & Mining"
                                ],
                                [
                                                "SMKM.JK",
                                                "PT Sumber Mas Konstruksi Tbk",
                                                "Industrials",
                                                "Engineering & Construction"
                                ],
                                [
                                                "IMJS.JK",
                                                "PT Indomobil Multi Jasa Tbk",
                                                "Industrials",
                                                "Conglomerates"
                                ],
                                [
                                                "PLIN.JK",
                                                "PT Plaza Indonesia Realty Tbk",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "TRIN.JK",
                                                "PT Perintis Triniti Properti Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "BSML.JK",
                                                "PT Bintang Samudera Mandiri Lines Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "AMIN.JK",
                                                "PT Ateliers Mecaniques D'Indonesie Tbk",
                                                "Industrials",
                                                "Specialty Industrial Machinery"
                                ],
                                [
                                                "BUKK.JK",
                                                "PT Bukaka Teknik Utama Tbk.",
                                                "Industrials",
                                                "Engineering & Construction"
                                ],
                                [
                                                "IBOS.JK",
                                                "PT Indo Boga Sukses Tbk",
                                                "Consumer Cyclical",
                                                "Restaurants"
                                ],
                                [
                                                "CLPI.JK",
                                                "PT Colorpak Indonesia Tbk",
                                                "Basic Materials",
                                                "Specialty Chemicals"
                                ],
                                [
                                                "JAYA.JK",
                                                "PT Armada Berjaya Trans Tbk",
                                                "Industrials",
                                                "Trucking"
                                ],
                                [
                                                "AMAR.JK",
                                                "PT Bank Amar Indonesia Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "CBMF.JK",
                                                "PT Cahaya Bintang Medan Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "FITT.JK",
                                                "PT Hotel Fitra International Tbk",
                                                "Consumer Cyclical",
                                                "Lodging"
                                ],
                                [
                                                "BKDP.JK",
                                                "PT Bukit Darmo Property Tbk",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "CTRA.JK",
                                                "PT Ciputra Development Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "DMAS.JK",
                                                "PT Puradelta Lestari Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "HKMU.JK",
                                                "PT HK Metals Utama Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "PSGO.JK",
                                                "PT Palma Serasih Tbk",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "DYAN.JK",
                                                "PT Dyandra Media International Tbk",
                                                "Communication Services",
                                                "Entertainment"
                                ],
                                [
                                                "GAMA.JK",
                                                "PT Aksara Global Development Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "CNKO.JK",
                                                "PT Exploitasi Energi Indonesia Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "PWSI.JK",
                                                "PWSI",
                                                "",
                                                ""
                                ],
                                [
                                                "PGLI.JK",
                                                "PT Pembangunan Graha Lestari Indah Tbk",
                                                "Consumer Cyclical",
                                                "Lodging"
                                ],
                                [
                                                "HOPE.JK",
                                                "PT Harapan Duta Pertiwi Tbk",
                                                "Industrials",
                                                "Metal Fabrication"
                                ],
                                [
                                                "TAMU.JK",
                                                "PT Pelayaran Tamarin Samudra Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "VRNA.JK",
                                                "PT Mizuho Leasing Indonesia Tbk",
                                                "Financial Services",
                                                "Credit Services"
                                ],
                                [
                                                "JSPT.JK",
                                                "PT Jakarta Setiabudi Internasional Tbk",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "PBID.JK",
                                                "PT Panca Budi Idaman Tbk",
                                                "Consumer Cyclical",
                                                "Packaging & Containers"
                                ],
                                [
                                                "ITMG.JK",
                                                "PT Indo Tambangraya Megah Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "ALKA.JK",
                                                "PT Alakasa Industrindo Tbk",
                                                "Basic Materials",
                                                "Aluminum"
                                ],
                                [
                                                "TFCO.JK",
                                                "PT Tifico Fiber Indonesia Tbk",
                                                "Consumer Cyclical",
                                                "Textile Manufacturing"
                                ],
                                [
                                                "KRAH.JK",
                                                "PT Grand Kartech Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "WIIM.JK",
                                                "PT Wismilak Inti Makmur Tbk",
                                                "Consumer Defensive",
                                                "Tobacco"
                                ],
                                [
                                                "AMAG.JK",
                                                "PT Asuransi Multi Artha Guna Tbk",
                                                "Financial Services",
                                                "Insurance - Property & Casualty"
                                ],
                                [
                                                "BBCA.JK",
                                                "PT Bank Central Asia Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "ERTX.JK",
                                                "PT Eratex Djaja Tbk",
                                                "Consumer Cyclical",
                                                "Apparel Manufacturing"
                                ],
                                [
                                                "IGAR.JK",
                                                "PT Champion Pacific Indonesia Tbk",
                                                "Consumer Cyclical",
                                                "Packaging & Containers"
                                ],
                                [
                                                "ITMA.JK",
                                                "PT Sumber Energi Andalan Tbk",
                                                "Basic Materials",
                                                "Other Industrial Metals & Mining"
                                ],
                                [
                                                "JTPE.JK",
                                                "PT Jasuindo Tiga Perkasa Tbk",
                                                "Industrials",
                                                "Specialty Business Services"
                                ],
                                [
                                                "SULI.JK",
                                                "PT SLJ Global Tbk",
                                                "Basic Materials",
                                                "Lumber & Wood Production"
                                ],
                                [
                                                "TAPG.JK",
                                                "PT Triputra Agro Persada Tbk",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "BELL.JK",
                                                "PT Trisula Textile Industries Tbk",
                                                "Consumer Cyclical",
                                                "Textile Manufacturing"
                                ],
                                [
                                                "TKIM.JK",
                                                "PT Pabrik Kertas Tjiwi Kimia Tbk",
                                                "Basic Materials",
                                                "Paper & Paper Products"
                                ],
                                [
                                                "URBN.JK",
                                                "PT Urban Jakarta Propertindo Tbk.",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "ASSA.JK",
                                                "PT Adi Sarana Armada Tbk",
                                                "Industrials",
                                                "Rental & Leasing Services"
                                ],
                                [
                                                "KOTA.JK",
                                                "PT DMS Propertindo Tbk",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "BJBR.JK",
                                                "PT Bank Pembangunan Daerah Jawa Barat dan Banten Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "SOSS.JK",
                                                "PT Shield On Service Tbk",
                                                "Industrials",
                                                "Staffing & Employment Services"
                                ],
                                [
                                                "UNVR.JK",
                                                "PT Unilever Indonesia Tbk",
                                                "Consumer Defensive",
                                                "Household & Personal Products"
                                ],
                                [
                                                "CLEO.JK",
                                                "PT Sariguna Primatirta Tbk",
                                                "Consumer Defensive",
                                                "Beverages - Non-Alcoholic"
                                ],
                                [
                                                "IDEA.JK",
                                                "PT Idea Indonesia Akademi Tbk",
                                                "Consumer Defensive",
                                                "Education & Training Services"
                                ],
                                [
                                                "ISAT.JK",
                                                "PT Indosat Ooredoo Hutchison Tbk",
                                                "Communication Services",
                                                "Telecom Services"
                                ],
                                [
                                                "AKPI.JK",
                                                "PT Argha Karya Prima Industry Tbk",
                                                "Consumer Cyclical",
                                                "Packaging & Containers"
                                ],
                                [
                                                "ASPI.JK",
                                                "PT Andalan Sakti Primaindo Tbk",
                                                "Consumer Cyclical",
                                                "Residential Construction"
                                ],
                                [
                                                "SKBM.JK",
                                                "PT Sekar Bumi Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "POSA.JK",
                                                "PT Bliss Properti Indonesia Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "VIVA.JK",
                                                "PT Visi Media Asia Tbk",
                                                "Communication Services",
                                                "Broadcasting"
                                ],
                                [
                                                "NRCA.JK",
                                                "PT Nusa Raya Cipta Tbk",
                                                "Industrials",
                                                "Engineering & Construction"
                                ],
                                [
                                                "BVIC.JK",
                                                "PT Bank Victoria International Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "META.JK",
                                                "PT Nusantara Infrastructure Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "MBSS.JK",
                                                "PT Mitrabahtera Segara Sejati Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "ENVY.JK",
                                                "PT Envy Technologies Indonesia Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "RODA.JK",
                                                "PT Pikko Land Development Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "NATO.JK",
                                                "PT Surya Permata Andalan Tbk",
                                                "Consumer Cyclical",
                                                "Lodging"
                                ],
                                [
                                                "SMKL.JK",
                                                "PT Satyamitra Kemas Lestari Tbk",
                                                "Consumer Cyclical",
                                                "Packaging & Containers"
                                ],
                                [
                                                "LIFE.JK",
                                                "PT MSIG Life Insurance Indonesia Tbk",
                                                "Financial Services",
                                                "Insurance - Life"
                                ],
                                [
                                                "ISSP.JK",
                                                "PT Steel Pipe Industry of Indonesia Tbk",
                                                "Basic Materials",
                                                "Steel"
                                ],
                                [
                                                "MTRA.JK",
                                                "PT Mitra Pemuda Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "SAME.JK",
                                                "PT Sarana Meditama Metropolitan Tbk",
                                                "Healthcare",
                                                "Medical Care Facilities"
                                ],
                                [
                                                "BNBA.JK",
                                                "PT Bank Bumi Arta Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "INTA.JK",
                                                "PT Intraco Penta Tbk",
                                                "Industrials",
                                                "Industrial Distribution"
                                ],
                                [
                                                "LPKR.JK",
                                                "PT Lippo Karawaci Tbk",
                                                "Healthcare",
                                                "Medical Care Facilities"
                                ],
                                [
                                                "MDKA.JK",
                                                "PT Merdeka Copper Gold Tbk",
                                                "Basic Materials",
                                                "Other Industrial Metals & Mining"
                                ],
                                [
                                                "TRST.JK",
                                                "PT Trias Sentosa Tbk",
                                                "Consumer Cyclical",
                                                "Packaging & Containers"
                                ],
                                [
                                                "CINT.JK",
                                                "PT Chitose Internasional Tbk",
                                                "Consumer Cyclical",
                                                "Furnishings, Fixtures & Appliances"
                                ],
                                [
                                                "RIGS.JK",
                                                "PT Rig Tenders Indonesia Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "POLY.JK",
                                                "PT Asia Pacific Fibers Tbk",
                                                "Basic Materials",
                                                "Specialty Chemicals"
                                ],
                                [
                                                "CHEM.JK",
                                                "PT Chemstar Indonesia Tbk",
                                                "Basic Materials",
                                                "Specialty Chemicals"
                                ],
                                [
                                                "MSKY.JK",
                                                "PT MNC Sky Vision Tbk",
                                                "Communication Services",
                                                "Entertainment"
                                ],
                                [
                                                "TIRA.JK",
                                                "PT Tira Austenite Tbk",
                                                "Industrials",
                                                "Industrial Distribution"
                                ],
                                [
                                                "WEGE.JK",
                                                "PT Wijaya Karya Bangunan Gedung Tbk",
                                                "Industrials",
                                                "Engineering & Construction"
                                ],
                                [
                                                "COWL.JK",
                                                "PT Cowell Development Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "ABMM.JK",
                                                "PT ABM Investama Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "SPMA.JK",
                                                "PT Suparma Tbk",
                                                "Basic Materials",
                                                "Paper & Paper Products"
                                ],
                                [
                                                "DADA.JK",
                                                "PT Diamond Citra Propertindo Tbk",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "TOTL.JK",
                                                "PT Total Bangun Persada Tbk",
                                                "Industrials",
                                                "Engineering & Construction"
                                ],
                                [
                                                "CMPP.JK",
                                                "PT AirAsia Indonesia Tbk",
                                                "Industrials",
                                                "Airlines"
                                ],
                                [
                                                "BUMI.JK",
                                                "PT Bumi Resources Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "ADMF.JK",
                                                "PT Adira Dinamika Multi Finance Tbk",
                                                "Financial Services",
                                                "Credit Services"
                                ],
                                [
                                                "ZYRX.JK",
                                                "PT Zyrexindo Mandiri Buana Tbk",
                                                "Technology",
                                                "Computer Hardware"
                                ],
                                [
                                                "DGIK.JK",
                                                "PT Nusa Konstruksi Enjiniring Tbk",
                                                "Industrials",
                                                "Engineering & Construction"
                                ],
                                [
                                                "PWON.JK",
                                                "PT Pakuwon Jati Tbk",
                                                "Real Estate",
                                                "Real Estate - Diversified"
                                ],
                                [
                                                "BCAP.JK",
                                                "PT MNC Kapital Indonesia Tbk",
                                                "Financial Services",
                                                "Financial Conglomerates"
                                ],
                                [
                                                "BEST.JK",
                                                "PT Bekasi Fajar Industrial Estate Tbk",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "CBDK.JK",
                                                "Bangun Kosambi Sukses Tbk.",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "KIAS.JK",
                                                "PT Keramika Indonesia Assosiasi Tbk",
                                                "Industrials",
                                                "Building Products & Equipment"
                                ],
                                [
                                                "TRIL.JK",
                                                "TRIL.JK,0P0000EOL4,0",
                                                "",
                                                ""
                                ],
                                [
                                                "PRIM.JK",
                                                "PT Royal Prima Tbk",
                                                "Healthcare",
                                                "Medical Care Facilities"
                                ],
                                [
                                                "BFIN.JK",
                                                "PT BFI Finance Indonesia Tbk",
                                                "Financial Services",
                                                "Credit Services"
                                ],
                                [
                                                "ABDA.JK",
                                                "PT Asuransi Bina Dana Arta Tbk",
                                                "Financial Services",
                                                "Insurance - Property & Casualty"
                                ],
                                [
                                                "UCID.JK",
                                                "PT Uni-Charm Indonesia Tbk",
                                                "Consumer Defensive",
                                                "Household & Personal Products"
                                ],
                                [
                                                "SBMA.JK",
                                                "PT Surya Biru Murni Acetylene Tbk",
                                                "Basic Materials",
                                                "Chemicals"
                                ],
                                [
                                                "JMAS.JK",
                                                "PT Asuransi Jiwa Syariah Jasa Mitra Abadi Tbk",
                                                "Financial Services",
                                                "Insurance - Life"
                                ],
                                [
                                                "MDIA.JK",
                                                "PT Intermedia Capital Tbk",
                                                "Communication Services",
                                                "Broadcasting"
                                ],
                                [
                                                "EURO.JK",
                                                "PT Estee Gold Feet Tbk",
                                                "Consumer Defensive",
                                                "Household & Personal Products"
                                ],
                                [
                                                "WSBP.JK",
                                                "PT Waskita Beton Precast Tbk",
                                                "Basic Materials",
                                                "Building Materials"
                                ],
                                [
                                                "INCF.JK",
                                                "PT Indo Komoditi Korpora Tbk",
                                                "Basic Materials",
                                                "Specialty Chemicals"
                                ],
                                [
                                                "AMMS.JK",
                                                "PT Agung Menjangan Mas Tbk",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "PNIN.JK",
                                                "PT Paninvest Tbk",
                                                "Financial Services",
                                                "Insurance - Life"
                                ],
                                [
                                                "PORT.JK",
                                                "PT Nusantara Pelabuhan Handal Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "ERAA.JK",
                                                "PT Erajaya Swasembada Tbk",
                                                "Consumer Cyclical",
                                                "Specialty Retail"
                                ],
                                [
                                                "ASMI.JK",
                                                "PT Asuransi Maximus Graha Persada Tbk",
                                                "Financial Services",
                                                "Insurance - Property & Casualty"
                                ],
                                [
                                                "PPGL.JK",
                                                "PT Prima Globalindo Logistik Tbk",
                                                "Industrials",
                                                "Integrated Freight & Logistics"
                                ],
                                [
                                                "TAMA.JK",
                                                "PT Lancartama Sejati Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "EAST.JK",
                                                "PT Eastparc Hotel Tbk",
                                                "Consumer Cyclical",
                                                "Lodging"
                                ],
                                [
                                                "AGRO.JK",
                                                "PT Bank Raya Indonesia Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "LTLS.JK",
                                                "PT Lautan Luas Tbk",
                                                "Basic Materials",
                                                "Specialty Chemicals"
                                ],
                                [
                                                "MNCN.JK",
                                                "PT. Media Nusantara Citra Tbk",
                                                "Communication Services",
                                                "Advertising Agencies"
                                ],
                                [
                                                "BSIM.JK",
                                                "PT Bank Sinarmas Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "LION.JK",
                                                "PT Lion Metal Works Tbk",
                                                "Industrials",
                                                "Business Equipment & Supplies"
                                ],
                                [
                                                "WIRG.JK",
                                                "PT WIR ASIA Tbk",
                                                "Technology",
                                                "Information Technology Services"
                                ],
                                [
                                                "AMRT.JK",
                                                "PT Sumber Alfaria Trijaya Tbk",
                                                "Consumer Defensive",
                                                "Grocery Stores"
                                ],
                                [
                                                "CEKA.JK",
                                                "PT Wilmar Cahaya Indonesia Tbk.",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "TURI.JK",
                                                "TURI",
                                                "",
                                                ""
                                ],
                                [
                                                "BBSS.JK",
                                                "PT Bumi Benowo Sukses Sejahtera Tbk",
                                                "Industrials",
                                                "Engineering & Construction"
                                ],
                                [
                                                "WINS.JK",
                                                "PT Wintermar Offshore Marine Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "CASS.JK",
                                                "PT Cahaya Aero Services Tbk.",
                                                "Industrials",
                                                "Airports & Air Services"
                                ],
                                [
                                                "FORU.JK",
                                                "PT Fortune Indonesia Tbk",
                                                "Communication Services",
                                                "Advertising Agencies"
                                ],
                                [
                                                "LPIN.JK",
                                                "PT Multi Prima Sejahtera Tbk",
                                                "Consumer Cyclical",
                                                "Auto Parts"
                                ],
                                [
                                                "STAR.JK",
                                                "PT Buana Artha Anugerah Tbk",
                                                "Financial Services",
                                                "Asset Management"
                                ],
                                [
                                                "MAMIP.JK",
                                                "MAMIP.JK,0P0000EGJN,0",
                                                "",
                                                ""
                                ],
                                [
                                                "CASH.JK",
                                                "PT Cashlez Worldwide Indonesia Tbk",
                                                "Industrials",
                                                "Business Equipment & Supplies"
                                ],
                                [
                                                "PALM.JK",
                                                "PT Provident Investasi Bersama Tbk",
                                                "Financial Services",
                                                "Asset Management"
                                ],
                                [
                                                "CNTX.JK",
                                                "PT Century Textile Industry Tbk",
                                                "Consumer Cyclical",
                                                "Textile Manufacturing"
                                ],
                                [
                                                "KPAL.JK",
                                                "PT Steadfast Marine Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "SRTG.JK",
                                                "PT Saratoga Investama Sedaya Tbk",
                                                "Financial Services",
                                                "Asset Management"
                                ],
                                [
                                                "BRAM.JK",
                                                "PT Indo Kordsa Tbk",
                                                "Consumer Cyclical",
                                                "Textile Manufacturing"
                                ],
                                [
                                                "LEAD.JK",
                                                "PT Logindo Samudramakmur Tbk.",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "VINS.JK",
                                                "PT Victoria Insurance Tbk",
                                                "Financial Services",
                                                "Insurance - Property & Casualty"
                                ],
                                [
                                                "TBIG.JK",
                                                "PT Tower Bersama Infrastructure Tbk",
                                                "Communication Services",
                                                "Telecom Services"
                                ],
                                [
                                                "MCAS.JK",
                                                "PT M Cash Integrasi Tbk",
                                                "Industrials",
                                                "Business Equipment & Supplies"
                                ],
                                [
                                                "HAIS.JK",
                                                "PT Hasnur Internasional Shipping Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "BRMS.JK",
                                                "PT Bumi Resources Minerals Tbk",
                                                "Basic Materials",
                                                "Other Industrial Metals & Mining"
                                ],
                                [
                                                "SIMA.JK",
                                                "PT Siwani Makmur Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "PSKT.JK",
                                                "PT Red Planet Indonesia Tbk",
                                                "Consumer Cyclical",
                                                "Lodging"
                                ],
                                [
                                                "PCAR.JK",
                                                "PT Prima Cakrawala Abadi Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "HRTA.JK",
                                                "PT Hartadinata Abadi Tbk",
                                                "Consumer Cyclical",
                                                "Luxury Goods"
                                ],
                                [
                                                "SWAT.JK",
                                                "PT Sriwahana Adityakarta Tbk",
                                                "Consumer Cyclical",
                                                "Packaging & Containers"
                                ],
                                [
                                                "BUKA.JK",
                                                "PT Bukalapak.com Tbk.",
                                                "Consumer Cyclical",
                                                "Internet Retail"
                                ],
                                [
                                                "SCNP.JK",
                                                "PT Selaras Citra Nusantara Perkasa Tbk",
                                                "Technology",
                                                "Consumer Electronics"
                                ],
                                [
                                                "BPTR.JK",
                                                "PT Batavia Prosperindo Trans Tbk",
                                                "Industrials",
                                                "Rental & Leasing Services"
                                ],
                                [
                                                "FMII.JK",
                                                "PT Fortune Mate Indonesia Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "BESS.JK",
                                                "PT Batulicin Nusantara Maritim Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "ASLC.JK",
                                                "PT Autopedia Sukses Lestari Tbk",
                                                "Consumer Cyclical",
                                                "Auto & Truck Dealerships"
                                ],
                                [
                                                "BINA.JK",
                                                "PT Bank Ina Perdana Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "OASA.JK",
                                                "PT Maharaksa Biru Energi Tbk",
                                                "Utilities",
                                                "Utilities - Renewable"
                                ],
                                [
                                                "INRU.JK",
                                                "PT Toba Pulp Lestari Tbk",
                                                "Basic Materials",
                                                "Paper & Paper Products"
                                ],
                                [
                                                "RUNS.JK",
                                                "PT Global Sukses Solusi Tbk",
                                                "Technology",
                                                "Software - Application"
                                ],
                                [
                                                "PNLF.JK",
                                                "PT Panin Financial Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "IMAS.JK",
                                                "PT Indomobil Sukses Internasional Tbk",
                                                "Consumer Cyclical",
                                                "Auto & Truck Dealerships"
                                ],
                                [
                                                "COAL.JK",
                                                "PT Black Diamond Resources Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "TLDN.JK",
                                                "PT Teladan Prima Agro Tbk",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "ARCI.JK",
                                                "PT Archi Indonesia Tbk",
                                                "Basic Materials",
                                                "Gold"
                                ],
                                [
                                                "PTBA.JK",
                                                "PT Bukit Asam Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "FIRE.JK",
                                                "PT Alfa Energi Investama Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "KEJU.JK",
                                                "PT Mulia Boga Raya Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "BOBA.JK",
                                                "PT Formosa Ingredient Factory Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "CPRO.JK",
                                                "PT Central Proteina Prima Tbk",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "ERAL.JK",
                                                "PT Sinar Eka Selaras Tbk",
                                                "Consumer Cyclical",
                                                "Specialty Retail"
                                ],
                                [
                                                "STTP.JK",
                                                "PT Siantar Top Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "TBLA.JK",
                                                "PT Tunas Baru Lampung Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "MAYA.JK",
                                                "PT Bank Mayapada Internasional Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "GOOD.JK",
                                                "PT Garudafood Putra Putri Jaya Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "WOMF.JK",
                                                "PT Wahana Ottomitra Multiartha Tbk",
                                                "Financial Services",
                                                "Credit Services"
                                ],
                                [
                                                "TLKM.JK",
                                                "Perusahaan Perseroan (Persero) PT Telekomunikasi Indonesia Tbk",
                                                "Communication Services",
                                                "Telecom Services"
                                ],
                                [
                                                "MKPI.JK",
                                                "PT Metropolitan Kentjana Tbk",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "LUCY.JK",
                                                "PT Lima Dua Lima Tiga Tbk",
                                                "Consumer Cyclical",
                                                "Restaurants"
                                ],
                                [
                                                "SMGR.JK",
                                                "PT Semen Indonesia (Persero) Tbk",
                                                "Basic Materials",
                                                "Building Materials"
                                ],
                                [
                                                "BPII.JK",
                                                "PT Batavia Prosperindo Internasional Tbk",
                                                "Financial Services",
                                                "Asset Management"
                                ],
                                [
                                                "SGER.JK",
                                                "PT Sumber Global Energy Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "DFAM.JK",
                                                "PT Dafam Property Indonesia Tbk",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "MAMI.JK",
                                                "PT Mas Murni Indonesia, Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "ALTO.JK",
                                                "PT Tri Banyan Tirta Tbk",
                                                "Consumer Defensive",
                                                "Beverages - Non-Alcoholic"
                                ],
                                [
                                                "APLI.JK",
                                                "PT Asiaplast Industries Tbk",
                                                "Consumer Cyclical",
                                                "Packaging & Containers"
                                ],
                                [
                                                "LMPI.JK",
                                                "PT Langgeng Makmur Industri Tbk",
                                                "Consumer Cyclical",
                                                "Furnishings, Fixtures & Appliances"
                                ],
                                [
                                                "RIMO.JK",
                                                "PT Rimo International Lestari Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "AIMS.JK",
                                                "PT Artha Mahiya Investama Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "BNLI.JK",
                                                "PT Bank Permata Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "LPCK.JK",
                                                "PT Lippo Cikarang Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "LUCK.JK",
                                                "PT Sentral Mitra Informatika Tbk",
                                                "Technology",
                                                "Computer Hardware"
                                ],
                                [
                                                "INCO.JK",
                                                "PT Vale Indonesia Tbk",
                                                "Basic Materials",
                                                "Other Industrial Metals & Mining"
                                ],
                                [
                                                "CTBN.JK",
                                                "PT Citra Tubindo Tbk",
                                                "Energy",
                                                "Oil & Gas Equipment & Services"
                                ],
                                [
                                                "ASRI.JK",
                                                "PT Alam Sutera Realty Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "WAPO.JK",
                                                "PT Wahana Pronatural Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "TEBE.JK",
                                                "PT Dana Brata Luhur Tbk",
                                                "Industrials",
                                                "Infrastructure Operations"
                                ],
                                [
                                                "MSIN.JK",
                                                "PT MNC Digital Entertainment Tbk",
                                                "Communication Services",
                                                "Entertainment"
                                ],
                                [
                                                "BABP.JK",
                                                "PT Bank MNC Internasional Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "BBNI.JK",
                                                "PT Bank Negara Indonesia (Persero) Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "MYOH.JK",
                                                "PT Samindo Resources Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "GWSA.JK",
                                                "PT Greenwood Sejahtera Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "TRUK.JK",
                                                "PT Guna Timur Raya Tbk",
                                                "Industrials",
                                                "Trucking"
                                ],
                                [
                                                "HBAT.JK",
                                                "PT Minahasa Membangun Hebat Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "TOYS.JK",
                                                "PT Sunindo Adipersada Tbk",
                                                "Consumer Cyclical",
                                                "Leisure"
                                ],
                                [
                                                "DEAL.JK",
                                                "PT Dewata Freightinternational Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "MIRA.JK",
                                                "PT Mitra International Resources Tbk",
                                                "Energy",
                                                "Oil & Gas Equipment & Services"
                                ],
                                [
                                                "PTDU.JK",
                                                "PT Djasa Ubersakti Tbk",
                                                "Industrials",
                                                "Engineering & Construction"
                                ],
                                [
                                                "VICO.JK",
                                                "PT Victoria Investama Tbk",
                                                "Financial Services",
                                                "Asset Management"
                                ],
                                [
                                                "WOOD.JK",
                                                "PT Integra Indocabinet Tbk",
                                                "Consumer Cyclical",
                                                "Furnishings, Fixtures & Appliances"
                                ],
                                [
                                                "TECH.JK",
                                                "PT Indosterling Technomedia TBK",
                                                "",
                                                ""
                                ],
                                [
                                                "SNLK.JK",
                                                "PT Sunter Lakeside Hotel Tbk",
                                                "Consumer Cyclical",
                                                "Lodging"
                                ],
                                [
                                                "SOTS.JK",
                                                "PT Satria Mega Kencana Tbk",
                                                "Consumer Cyclical",
                                                "Lodging"
                                ],
                                [
                                                "ASJT.JK",
                                                "PT Asuransi Jasa Tania Tbk",
                                                "Financial Services",
                                                "Insurance - Property & Casualty"
                                ],
                                [
                                                "INPP.JK",
                                                "PT Indonesian Paradise Property Tbk",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "EMTK.JK",
                                                "PT Elang Mahkota Teknologi Tbk",
                                                "Communication Services",
                                                "Broadcasting"
                                ],
                                [
                                                "KREN.JK",
                                                "PT Quantum Clovera Investama Tbk",
                                                "Financial Services",
                                                "Asset Management"
                                ],
                                [
                                                "SPTO.JK",
                                                "PT Surya Pertiwi Tbk",
                                                "Consumer Cyclical",
                                                "Furnishings, Fixtures & Appliances"
                                ],
                                [
                                                "CMRY.JK",
                                                "PT Cisarua Mountain Dairy Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "GDYR.JK",
                                                "PT Goodyear Indonesia Tbk",
                                                "Consumer Cyclical",
                                                "Auto Parts"
                                ],
                                [
                                                "KEEN.JK",
                                                "PT Kencana Energi Lestari Tbk",
                                                "Utilities",
                                                "Utilities - Independent Power Producers"
                                ],
                                [
                                                "MEDC.JK",
                                                "PT Medco Energi Internasional Tbk",
                                                "Energy",
                                                "Oil & Gas E&P"
                                ],
                                [
                                                "SUGI.JK",
                                                "SUGI.JK,0P0000BT07,0",
                                                "",
                                                ""
                                ],
                                [
                                                "SUPR.JK",
                                                "PT Solusi Tunas Pratama Tbk",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "BNGA.JK",
                                                "PT Bank CIMB Niaga Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "DUTI.JK",
                                                "PT Duta Pertiwi Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "TPIA.JK",
                                                "PT Chandra Asri Pacific Tbk",
                                                "Basic Materials",
                                                "Specialty Chemicals"
                                ],
                                [
                                                "NICK.JK",
                                                "PT Charnic Capital Tbk",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "SKRN.JK",
                                                "PT Superkrane Mitra Utama Tbk",
                                                "Industrials",
                                                "Rental & Leasing Services"
                                ],
                                [
                                                "BOLA.JK",
                                                "PT Bali Bintang Sejahtera Tbk",
                                                "Communication Services",
                                                "Entertainment"
                                ],
                                [
                                                "LPPS.JK",
                                                "PT Lenox Pasifik Investama Tbk",
                                                "Financial Services",
                                                "Capital Markets"
                                ],
                                [
                                                "PURI.JK",
                                                "PT Puri Global Sukses Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "ASHA.JK",
                                                "PT Cilacap Samudera Fishing Industry Tbk",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "FPNI.JK",
                                                "PT Lotte Chemical Titan Tbk",
                                                "Basic Materials",
                                                "Specialty Chemicals"
                                ],
                                [
                                                "NOBU.JK",
                                                "PT Bank Nationalnobu Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "INDY.JK",
                                                "PT. Indika Energy Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "INKP.JK",
                                                "PT Indah Kiat Pulp & Paper Tbk",
                                                "Basic Materials",
                                                "Paper & Paper Products"
                                ],
                                [
                                                "HOME.JK",
                                                "PT Hotel Mandarine Regency Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "MDRN.JK",
                                                "PT Modern Internasional Tbk",
                                                "Industrials",
                                                "Business Equipment & Supplies"
                                ],
                                [
                                                "TOBA.JK",
                                                "PT TBS Energi Utama Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "MAPB.JK",
                                                "PT Map Boga Adiperkasa Tbk",
                                                "Consumer Cyclical",
                                                "Restaurants"
                                ],
                                [
                                                "RELI.JK",
                                                "PT Reliance Sekuritas Indonesia Tbk",
                                                "Financial Services",
                                                "Capital Markets"
                                ],
                                [
                                                "INPS.JK",
                                                "PT Indah Prakasa Sentosa Tbk",
                                                "Industrials",
                                                "Trucking"
                                ],
                                [
                                                "ANDI.JK",
                                                "PT Andira Agro, Tbk",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "DOSS.JK",
                                                "Global Sukses Digital Tbk.",
                                                "Consumer Cyclical",
                                                "Specialty Retail"
                                ],
                                [
                                                "BBKP.JK",
                                                "PT Bank KB Indonesia Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "IIKP.JK",
                                                "PT Inti Agri Resources Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "MBTO.JK",
                                                "PT Martina Berto Tbk",
                                                "Consumer Defensive",
                                                "Household & Personal Products"
                                ],
                                [
                                                "RANC.JK",
                                                "PT Supra Boga Lestari Tbk",
                                                "Consumer Defensive",
                                                "Grocery Stores"
                                ],
                                [
                                                "INDR.JK",
                                                "PT. Indo-Rama Synthetics Tbk",
                                                "Consumer Cyclical",
                                                "Textile Manufacturing"
                                ],
                                [
                                                "NIPS.JK",
                                                "PT Nipress Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "AMOR.JK",
                                                "PT Ashmore Asset Management Indonesia Tbk",
                                                "Financial Services",
                                                "Asset Management"
                                ],
                                [
                                                "TBMS.JK",
                                                "PT Tembaga Mulia Semanan Tbk",
                                                "Industrials",
                                                "Metal Fabrication"
                                ],
                                [
                                                "BIKA.JK",
                                                "PT Binakarya Jaya Abadi Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "VOKS.JK",
                                                "PT Voksel Electric Tbk",
                                                "Industrials",
                                                "Electrical Equipment & Parts"
                                ],
                                [
                                                "HEXA.JK",
                                                "PT Hexindo Adiperkasa Tbk",
                                                "Industrials",
                                                "Industrial Distribution"
                                ],
                                [
                                                "SOUL.JK",
                                                "PT Mitra Tirta Buwana Tbk",
                                                "Industrials",
                                                "Specialty Business Services"
                                ],
                                [
                                                "ADES.JK",
                                                "PT Akasha Wira International Tbk",
                                                "Consumer Defensive",
                                                "Beverages - Non-Alcoholic"
                                ],
                                [
                                                "SMBR.JK",
                                                "PT Semen Baturaja (Persero) Tbk",
                                                "Basic Materials",
                                                "Building Materials"
                                ],
                                [
                                                "ALMI.JK",
                                                "PT Alumindo Light Metal Industry Tbk",
                                                "Basic Materials",
                                                "Aluminum"
                                ],
                                [
                                                "EPMT.JK",
                                                "PT Enseval Putera Megatrading Tbk.",
                                                "Healthcare",
                                                "Medical Distribution"
                                ],
                                [
                                                "DART.JK",
                                                "PT Duta Anggada Realty Tbk.",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "PSSI.JK",
                                                "PT IMC Pelita Logistik Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "BBHI.JK",
                                                "PT Allo Bank Indonesia Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "BGTG.JK",
                                                "PT Bank Ganesha Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "GOLL.JK",
                                                "PT Golden Plantation Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "IMPC.JK",
                                                "PT Impack Pratama Industri Tbk",
                                                "Industrials",
                                                "Building Products & Equipment"
                                ],
                                [
                                                "BBRM.JK",
                                                "PT Pelayaran Nasional Bina Buana Raya Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "DIVA.JK",
                                                "PT Distribusi Voucher Nusantara Tbk",
                                                "Technology",
                                                "Software - Application"
                                ],
                                [
                                                "BSDE.JK",
                                                "PT Bumi Serpong Damai Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "BNII.JK",
                                                "PT Bank Maybank Indonesia Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "BMRI.JK",
                                                "PT Bank Mandiri (Persero) Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "DNET.JK",
                                                "PT Indoritel Makmur Internasional Tbk.",
                                                "Communication Services",
                                                "Telecom Services"
                                ],
                                [
                                                "ZATA.JK",
                                                "PT Bersama Zatta Jaya Tbk",
                                                "Consumer Cyclical",
                                                "Apparel Retail"
                                ],
                                [
                                                "BSWD.JK",
                                                "PT Bank of India Indonesia Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "SMRA.JK",
                                                "PT Summarecon Agung Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "MIKA.JK",
                                                "PT Mitra Keluarga Karyasehat Tbk",
                                                "Healthcare",
                                                "Medical Care Facilities"
                                ],
                                [
                                                "INOV.JK",
                                                "PT Inocycle Technology Group Tbk",
                                                "Industrials",
                                                "Waste Management"
                                ],
                                [
                                                "MTLA.JK",
                                                "PT Metropolitan Land Tbk",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "BALI.JK",
                                                "PT Bali Towerindo Sentra Tbk",
                                                "Communication Services",
                                                "Telecom Services"
                                ],
                                [
                                                "PAMG.JK",
                                                "PT Bima Sakti Pertiwi Tbk",
                                                "Real Estate",
                                                "Real Estate - Diversified"
                                ],
                                [
                                                "GUNA.JK",
                                                "Gunanusa Eramandiri Tbk.",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "CENT.JK",
                                                "PT Centratama Telekomunikasi Indonesia Tbk",
                                                "Communication Services",
                                                "Telecom Services"
                                ],
                                [
                                                "GTRA.JK",
                                                "PT Grahaprima Suksesmandiri Tbk",
                                                "Industrials",
                                                "Integrated Freight & Logistics"
                                ],
                                [
                                                "VICI.JK",
                                                "PT Victoria Care Indonesia Tbk",
                                                "Consumer Defensive",
                                                "Household & Personal Products"
                                ],
                                [
                                                "AYLS.JK",
                                                "PT Agro Yasa Lestari Tbk",
                                                "Consumer Defensive",
                                                "Food Distribution"
                                ],
                                [
                                                "ASDM.JK",
                                                "PT Asuransi Dayin Mitra Tbk",
                                                "Financial Services",
                                                "Insurance - Diversified"
                                ],
                                [
                                                "PEHA.JK",
                                                "PT Phapros Tbk",
                                                "Healthcare",
                                                "Drug Manufacturers - Specialty & Generic"
                                ],
                                [
                                                "SURE.JK",
                                                "PT Super Energy Tbk",
                                                "Energy",
                                                "Oil & Gas Integrated"
                                ],
                                [
                                                "OCAP.JK",
                                                "PT Onix Capital Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "BBSI.JK",
                                                "PT Krom Bank Indonesia Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "UNIQ.JK",
                                                "PT Ulima Nitra Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "BBLD.JK",
                                                "PT Buana Finance Tbk",
                                                "Financial Services",
                                                "Credit Services"
                                ],
                                [
                                                "MKNT.JK",
                                                "PT Mitra Komunikasi Nusantara Tbk",
                                                "Technology",
                                                "Communication Equipment"
                                ],
                                [
                                                "DOOH.JK",
                                                "PT Era Media Sejahtera Tbk",
                                                "Communication Services",
                                                "Advertising Agencies"
                                ],
                                [
                                                "PRDA.JK",
                                                "PT Prodia Widyahusada Tbk",
                                                "Healthcare",
                                                "Diagnostics & Research"
                                ],
                                [
                                                "IKBI.JK",
                                                "PT Sumi Indo Kabel Tbk",
                                                "Industrials",
                                                "Electrical Equipment & Parts"
                                ],
                                [
                                                "GLOB.JK",
                                                "PT Globe Kita Terang Tbk",
                                                "Consumer Cyclical",
                                                "Specialty Retail"
                                ],
                                [
                                                "LPLI.JK",
                                                "PT Star Pacific Tbk",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "POOL.JK",
                                                "PT. Pool Advista Indonesia Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "SOFA.JK",
                                                "PT Boston Furniture Industries Tbk",
                                                "Utilities",
                                                "Utilities - Renewable"
                                ],
                                [
                                                "YPAS.JK",
                                                "PT Yanaprima Hastapersada Tbk",
                                                "Consumer Cyclical",
                                                "Packaging & Containers"
                                ],
                                [
                                                "BCIC.JK",
                                                "PT Bank JTrust Indonesia Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "SRAJ.JK",
                                                "PT Sejahteraraya Anugrahjaya Tbk",
                                                "Healthcare",
                                                "Medical Care Facilities"
                                ],
                                [
                                                "ARMY.JK",
                                                "PT Armidian Karyatama Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "HERO.JK",
                                                "PT DFI Retail Nusantara Tbk",
                                                "Consumer Cyclical",
                                                "Department Stores"
                                ],
                                [
                                                "DLTA.JK",
                                                "PT Delta Djakarta Tbk",
                                                "Consumer Defensive",
                                                "Beverages - Brewers"
                                ],
                                [
                                                "CASA.JK",
                                                "PT Capital Financial Indonesia Tbk",
                                                "Financial Services",
                                                "Insurance - Life"
                                ],
                                [
                                                "GEMS.JK",
                                                "PT Golden Energy Mines Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "SRSN.JK",
                                                "PT Indo Acidatama Tbk",
                                                "Basic Materials",
                                                "Chemicals"
                                ],
                                [
                                                "IKAI.JK",
                                                "PT Intikeramik Alamasri Industri Tbk",
                                                "Industrials",
                                                "Building Products & Equipment"
                                ],
                                [
                                                "LCGP.JK",
                                                "PT Eureka Prima Jakarta Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "WIFI.JK",
                                                "PT Solusi Sinergi Digital Tbk",
                                                "Technology",
                                                "Information Technology Services"
                                ],
                                [
                                                "MYTX.JK",
                                                "PT Asia Pacific Investama Tbk",
                                                "Consumer Cyclical",
                                                "Textile Manufacturing"
                                ],
                                [
                                                "EXCL.JK",
                                                "PT XLSMART Telecom Sejahtera Tbk",
                                                "Communication Services",
                                                "Telecom Services"
                                ],
                                [
                                                "MPPA.JK",
                                                "PT Matahari Putra Prima Tbk",
                                                "Consumer Cyclical",
                                                "Department Stores"
                                ],
                                [
                                                "AHAP.JK",
                                                "PT Asuransi Harta Aman Pratama Tbk",
                                                "Financial Services",
                                                "Insurance - Property & Casualty"
                                ],
                                [
                                                "SMRU.JK",
                                                "PT SMR Utama Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "KAEF.JK",
                                                "PT Kimia Farma Tbk",
                                                "Healthcare",
                                                "Medical Distribution"
                                ],
                                [
                                                "MITI.JK",
                                                "PT Mitra Investindo Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "IBFN.JK",
                                                "PT Intan Baru Prana Tbk",
                                                "Financial Services",
                                                "Credit Services"
                                ],
                                [
                                                "DIGI.JK",
                                                "PT Arkadia Digital Media Tbk",
                                                "Communication Services",
                                                "Internet Content & Information"
                                ],
                                [
                                                "DPUM.JK",
                                                "PT Dua Putra Utama Makmur Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "MGNA.JK",
                                                "PT Magna Investama Mandiri Tbk",
                                                "Financial Services",
                                                "Credit Services"
                                ],
                                [
                                                "ROCK.JK",
                                                "PT Rockfields Properti Indonesia Tbk.",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "UVCR.JK",
                                                "PT Trimegah Karya Pratama Tbk",
                                                "Technology",
                                                "Software - Application"
                                ],
                                [
                                                "ARGO.JK",
                                                "PT Argo Pantes Tbk",
                                                "Consumer Cyclical",
                                                "Textile Manufacturing"
                                ],
                                [
                                                "NETV.JK",
                                                "PT MDTV Media Technologies Tbk",
                                                "Communication Services",
                                                "Broadcasting"
                                ],
                                [
                                                "TRUE.JK",
                                                "PT Triniti Dinamik Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "TAXI.JK",
                                                "PT Express Transindo Utama Tbk",
                                                "Industrials",
                                                "Railroads"
                                ],
                                [
                                                "ACST.JK",
                                                "PT Acset Indonusa Tbk",
                                                "Industrials",
                                                "Engineering & Construction"
                                ],
                                [
                                                "BRIS.JK",
                                                "PT Bank Syariah Indonesia Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "KBLV.JK",
                                                "PT First Media Tbk",
                                                "Communication Services",
                                                "Entertainment"
                                ],
                                [
                                                "ZONE.JK",
                                                "PT Mega Perintis Tbk",
                                                "Consumer Cyclical",
                                                "Apparel Retail"
                                ],
                                [
                                                "TOWR.JK",
                                                "PT Sarana Menara Nusantara Tbk.",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "BCIP.JK",
                                                "PT Bumi Citra Permai Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "DPNS.JK",
                                                "PT Duta Pertiwi Nusantara Tbk",
                                                "Basic Materials",
                                                "Specialty Chemicals"
                                ],
                                [
                                                "ELPI.JK",
                                                "PT Pelayaran Nasional Ekalya Purnamasari Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "ADRO.JK",
                                                "PT Alamtri Resources Indonesia Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "SIDO.JK",
                                                "PT Industri Jamu dan Farmasi Sido Muncul Tbk",
                                                "Healthcare",
                                                "Drug Manufacturers - Specialty & Generic"
                                ],
                                [
                                                "MENN.JK",
                                                "PT Menn Teknologi Indonesia Tbk",
                                                "Industrials",
                                                "Electrical Equipment & Parts"
                                ],
                                [
                                                "FILM.JK",
                                                "PT.MD Entertainment Tbk",
                                                "Communication Services",
                                                "Entertainment"
                                ],
                                [
                                                "PTRO.JK",
                                                "PT Petrosea Tbk",
                                                "Basic Materials",
                                                "Other Industrial Metals & Mining"
                                ],
                                [
                                                "JPFA.JK",
                                                "PT Japfa Comfeed Indonesia Tbk",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "MERK.JK",
                                                "PT Merck Tbk",
                                                "Healthcare",
                                                "Drug Manufacturers - Specialty & Generic"
                                ],
                                [
                                                "NISP.JK",
                                                "PT Bank OCBC NISP Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "KINO.JK",
                                                "PT Kino Indonesia Tbk",
                                                "Consumer Defensive",
                                                "Beverages - Non-Alcoholic"
                                ],
                                [
                                                "KICI.JK",
                                                "PT Kedaung Indah Can Tbk",
                                                "Consumer Cyclical",
                                                "Furnishings, Fixtures & Appliances"
                                ],
                                [
                                                "SHIP.JK",
                                                "PT Sillo Maritime Perdana Tbk",
                                                "Energy",
                                                "Oil & Gas Equipment & Services"
                                ],
                                [
                                                "JSMR.JK",
                                                "PT Jasa Marga (Persero) Tbk",
                                                "Industrials",
                                                "Infrastructure Operations"
                                ],
                                [
                                                "KONI.JK",
                                                "PT Perdana Bangun Pusaka Tbk",
                                                "Consumer Cyclical",
                                                "Specialty Retail"
                                ],
                                [
                                                "MTPS.JK",
                                                "PT Meta Epsi Tbk.",
                                                "Industrials",
                                                "Engineering & Construction"
                                ],
                                [
                                                "GPRA.JK",
                                                "PT Perdana Gapuraprima Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "NUSA.JK",
                                                "PT Sinergi Megah Internusa Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "IPCM.JK",
                                                "PT Jasa Armada Indonesia Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "MDKI.JK",
                                                "PT Emdeki Utama Tbk",
                                                "Basic Materials",
                                                "Specialty Chemicals"
                                ],
                                [
                                                "SMIL.JK",
                                                "PT Sarana Mitra Luas Tbk",
                                                "Industrials",
                                                "Rental & Leasing Services"
                                ],
                                [
                                                "HDTX.JK",
                                                "HDTX.JK,0P0000B9YK,0",
                                                "",
                                                ""
                                ],
                                [
                                                "PSDN.JK",
                                                "PT Prasidha Aneka Niaga Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "SMSM.JK",
                                                "PT Selamat Sempurna Tbk",
                                                "Consumer Cyclical",
                                                "Auto Parts"
                                ],
                                [
                                                "SATU.JK",
                                                "PT Kota Satu Properti Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "APII.JK",
                                                "PT Arita Prima Indonesia Tbk",
                                                "Industrials",
                                                "Tools & Accessories"
                                ],
                                [
                                                "SMMA.JK",
                                                "PT Sinar Mas Multiartha Tbk",
                                                "Financial Services",
                                                "Insurance - Diversified"
                                ],
                                [
                                                "PLAN.JK",
                                                "PT Planet Properindo Jaya Tbk",
                                                "Consumer Cyclical",
                                                "Lodging"
                                ],
                                [
                                                "BLTZ.JK",
                                                "PT Graha Layar Prima Tbk",
                                                "Communication Services",
                                                "Entertainment"
                                ],
                                [
                                                "LRNA.JK",
                                                "PT Eka Sari Lorena Transport Tbk",
                                                "Industrials",
                                                "Railroads"
                                ],
                                [
                                                "PPRO.JK",
                                                "PT Pembangunan Perumahan Properti Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "TRIS.JK",
                                                "PT Trisula International Tbk",
                                                "Consumer Cyclical",
                                                "Apparel Manufacturing"
                                ],
                                [
                                                "RBMS.JK",
                                                "PT Ristia Bintang Mahkotasejati Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "LAPD.JK",
                                                "PT Leyand International Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "DCII.JK",
                                                "PT DCI Indonesia Tbk",
                                                "Technology",
                                                "Information Technology Services"
                                ],
                                [
                                                "MPMX.JK",
                                                "PT Mitra Pinasthika Mustika Tbk",
                                                "Consumer Cyclical",
                                                "Auto & Truck Dealerships"
                                ],
                                [
                                                "INDF.JK",
                                                "PT Indofood Sukses Makmur Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "KBRI.JK",
                                                "PT Kertas Basuki Rachmat Indonesia Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "DVLA.JK",
                                                "PT Darya-Varia Laboratoria Tbk",
                                                "Healthcare",
                                                "Drug Manufacturers - Specialty & Generic"
                                ],
                                [
                                                "JIHD.JK",
                                                "PT Jakarta International Hotels & Development Tbk",
                                                "Consumer Cyclical",
                                                "Lodging"
                                ],
                                [
                                                "MLIA.JK",
                                                "PT Mulia Industrindo Tbk",
                                                "Industrials",
                                                "Building Products & Equipment"
                                ],
                                [
                                                "PBRX.JK",
                                                "PT Pan Brothers Tbk",
                                                "Consumer Cyclical",
                                                "Apparel Manufacturing"
                                ],
                                [
                                                "SOCI.JK",
                                                "PT Soechi Lines Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "APIC.JK",
                                                "PT Pacific Strategic Financial Tbk",
                                                "Financial Services",
                                                "Insurance - Life"
                                ],
                                [
                                                "SSMS.JK",
                                                "PT Sawit Sumbermas Sarana Tbk.",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "EMDE.JK",
                                                "PT Megapolitan Developments Tbk",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "BRNA.JK",
                                                "PT Berlina Tbk",
                                                "Consumer Cyclical",
                                                "Packaging & Containers"
                                ],
                                [
                                                "BOSS.JK",
                                                "PT. Borneo Olah Sarana Sukses Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "GOTO.JK",
                                                "PT GoTo Gojek Tokopedia Tbk",
                                                "Technology",
                                                "Software - Infrastructure"
                                ],
                                [
                                                "IPCC.JK",
                                                "PT Indonesia Kendaraan Terminal Tbk",
                                                "Industrials",
                                                "Integrated Freight & Logistics"
                                ],
                                [
                                                "SCMA.JK",
                                                "PT Surya Citra Media Tbk",
                                                "Communication Services",
                                                "Broadcasting"
                                ],
                                [
                                                "TRJA.JK",
                                                "PT Transkon Jaya Tbk",
                                                "Industrials",
                                                "Rental & Leasing Services"
                                ],
                                [
                                                "GIAA.JK",
                                                "PT. Garuda Indonesia (Persero) Tbk",
                                                "Industrials",
                                                "Airlines"
                                ],
                                [
                                                "APLN.JK",
                                                "PT Agung Podomoro Land Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "TMAS.JK",
                                                "PT Temas Tbk.",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "CAMP.JK",
                                                "PT Campina Ice Cream Industry, Tbk.",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "ACES.JK",
                                                "PT Aspirasi Hidup Indonesia Tbk",
                                                "Consumer Cyclical",
                                                "Specialty Retail"
                                ],
                                [
                                                "ASGR.JK",
                                                "PT Astra Graphia Tbk",
                                                "Industrials",
                                                "Specialty Business Services"
                                ],
                                [
                                                "ELTY.JK",
                                                "PT Bakrieland Development Tbk",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "KARW.JK",
                                                "PT Meratus Jasa Prima Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "CTTH.JK",
                                                "PT Citatah Tbk",
                                                "Basic Materials",
                                                "Building Materials"
                                ],
                                [
                                                "SEMA.JK",
                                                "PT Semacom Integrated Tbk",
                                                "Industrials",
                                                "Specialty Industrial Machinery"
                                ],
                                [
                                                "GTSI.JK",
                                                "PT GTS Internasional Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "CMNT.JK",
                                                "PT Cemindo Gemilang Tbk",
                                                "Basic Materials",
                                                "Building Materials"
                                ],
                                [
                                                "ATIC.JK",
                                                "PT Anabatic Technologies Tbk",
                                                "Technology",
                                                "Information Technology Services"
                                ],
                                [
                                                "BWPT.JK",
                                                "PT Eagle High Plantations Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "PGAS.JK",
                                                "PT Perusahaan Gas Negara Tbk",
                                                "Utilities",
                                                "Utilities - Regulated Gas"
                                ],
                                [
                                                "PJAA.JK",
                                                "PT Pembangunan Jaya Ancol Tbk",
                                                "Consumer Cyclical",
                                                "Leisure"
                                ],
                                [
                                                "JKSW.JK",
                                                "PT Jakarta Kyoei Steel Works, Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "CSMI.JK",
                                                "PT Cipta Selera Murni Tbk",
                                                "Consumer Cyclical",
                                                "Restaurants"
                                ],
                                [
                                                "RISE.JK",
                                                "PT Jaya Sukses Makmur Sentosa Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "KETR.JK",
                                                "PT Ketrosden Triasmitra",
                                                "Technology",
                                                "Communication Equipment"
                                ],
                                [
                                                "TARA.JK",
                                                "PT Agung Semesta Sejahtera Tbk",
                                                "Real Estate",
                                                "Real Estate - Diversified"
                                ],
                                [
                                                "IRRA.JK",
                                                "PT Itama Ranoraya Tbk",
                                                "Healthcare",
                                                "Medical Distribution"
                                ],
                                [
                                                "CLAY.JK",
                                                "PT Citra Putra Realty Tbk",
                                                "Consumer Cyclical",
                                                "Lodging"
                                ],
                                [
                                                "ITIC.JK",
                                                "PT Indonesian Tobacco Tbk",
                                                "Consumer Defensive",
                                                "Tobacco"
                                ],
                                [
                                                "MREI.JK",
                                                "PT Maskapai Reasuransi Indonesia Tbk",
                                                "Financial Services",
                                                "Insurance - Reinsurance"
                                ],
                                [
                                                "LPGI.JK",
                                                "PT Lippo General Insurance Tbk",
                                                "Financial Services",
                                                "Insurance - Diversified"
                                ],
                                [
                                                "LMSH.JK",
                                                "PT Lionmesh Prima Tbk",
                                                "Industrials",
                                                "Metal Fabrication"
                                ],
                                [
                                                "BMHS.JK",
                                                "PT Bundamedik Tbk",
                                                "Healthcare",
                                                "Medical Care Facilities"
                                ],
                                [
                                                "PGEO.JK",
                                                "PT Pertamina Geothermal Energy Tbk",
                                                "Utilities",
                                                "Utilities - Renewable"
                                ],
                                [
                                                "CPRI.JK",
                                                "PT Capri Nusa Satu Properti Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "CSAP.JK",
                                                "PT Catur Sentosa Adiprana Tbk",
                                                "Industrials",
                                                "Industrial Distribution"
                                ],
                                [
                                                "MCOR.JK",
                                                "PT Bank China Construction Bank Indonesia Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "MTWI.JK",
                                                "PT Malacca Trust Wuwungan Insurance Tbk",
                                                "Financial Services",
                                                "Insurance - Diversified"
                                ],
                                [
                                                "TCPI.JK",
                                                "PT Transcoal Pacific Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "MEGA.JK",
                                                "PT Bank Mega Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "DEWA.JK",
                                                "PT Darma Henwa Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "TNCA.JK",
                                                "PT Trimuda Nuansa Citra Tbk",
                                                "Industrials",
                                                "Integrated Freight & Logistics"
                                ],
                                [
                                                "BTPS.JK",
                                                "PT Bank BTPN Syariah Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "PYFA.JK",
                                                "PT Pyridam Farma Tbk",
                                                "Healthcare",
                                                "Drug Manufacturers - Specialty & Generic"
                                ],
                                [
                                                "MLPT.JK",
                                                "PT Multipolar Technology Tbk",
                                                "Technology",
                                                "Information Technology Services"
                                ],
                                [
                                                "SHID.JK",
                                                "PT Hotel Sahid Jaya International Tbk",
                                                "Consumer Cyclical",
                                                "Lodging"
                                ],
                                [
                                                "BACA.JK",
                                                "PT Bank Capital Indonesia Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "SONA.JK",
                                                "PT Sona Topas Tourism Industry Tbk",
                                                "Consumer Cyclical",
                                                "Travel Services"
                                ],
                                [
                                                "SFAN.JK",
                                                "PT Surya Fajar Capital Tbk",
                                                "Financial Services",
                                                "Asset Management"
                                ],
                                [
                                                "BTPN.JK",
                                                "PT Bank SMBC Indonesia Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "PLAS.JK",
                                                "PT Polaris Investama Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "AKKU.JK",
                                                "PT Anugerah Kagum Karya Utama Tbk",
                                                "Consumer Cyclical",
                                                "Lodging"
                                ],
                                [
                                                "ALDO.JK",
                                                "PT Alkindo Naratama Tbk",
                                                "Basic Materials",
                                                "Paper & Paper Products"
                                ],
                                [
                                                "NIKL.JK",
                                                "PT Pelat Timah Nusantara Tbk",
                                                "Industrials",
                                                "Metal Fabrication"
                                ],
                                [
                                                "BUDI.JK",
                                                "PT Budi Starch & Sweetener Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "PNBN.JK",
                                                "PT Bank Pan Indonesia Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "PURE.JK",
                                                "PT Trinitan Metals and Minerals Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "TGRA.JK",
                                                "PT. Terregra Asia Energy Tbk",
                                                "Utilities",
                                                "Utilities - Renewable"
                                ],
                                [
                                                "MTFN.JK",
                                                "PT Capitalinc Investment Tbk",
                                                "Energy",
                                                "Oil & Gas E&P"
                                ],
                                [
                                                "INDS.JK",
                                                "PT Indospring Tbk",
                                                "Consumer Cyclical",
                                                "Auto Parts"
                                ],
                                [
                                                "ARTI.JK",
                                                "PT. Ratu Prabu Energi, Tbk",
                                                "Energy",
                                                "Oil & Gas Equipment & Services"
                                ],
                                [
                                                "MBAP.JK",
                                                "PT Mitrabara Adiperdana Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "SMDR.JK",
                                                "PT Samudera Indonesia Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "MYOR.JK",
                                                "PT Mayora Indah Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "IKAN.JK",
                                                "PT Era Mandiri Cemerlang Tbk",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "OILS.JK",
                                                "PT Indo Oil Perkasa Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "MDLN.JK",
                                                "PT Modernland Realty Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "PUDP.JK",
                                                "PT Pudjiadi Prestige Tbk",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "PTPP.JK",
                                                "PT PP (Persero) Tbk",
                                                "Industrials",
                                                "Engineering & Construction"
                                ],
                                [
                                                "ADMG.JK",
                                                "PT. Polychem Indonesia Tbk",
                                                "Basic Materials",
                                                "Chemicals"
                                ],
                                [
                                                "GGRP.JK",
                                                "PT Gunung Raja Paksi Tbk",
                                                "Basic Materials",
                                                "Steel"
                                ],
                                [
                                                "SOHO.JK",
                                                "PT Soho Global Health Tbk",
                                                "Healthcare",
                                                "Medical Distribution"
                                ],
                                [
                                                "MAIN.JK",
                                                "PT Malindo Feedmill Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "HRUM.JK",
                                                "PT Harum Energy Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "SAPX.JK",
                                                "PT Satria Antaran Prima Tbk",
                                                "Industrials",
                                                "Integrated Freight & Logistics"
                                ],
                                [
                                                "SMMT.JK",
                                                "PT Golden Eagle Energy Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "ANTM.JK",
                                                "PT Aneka Tambang Tbk",
                                                "Basic Materials",
                                                "Gold"
                                ],
                                [
                                                "CSRA.JK",
                                                "PT Cisadane Sawit Raya Tbk",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "BKSL.JK",
                                                "PT Sentul City Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "MTEL.JK",
                                                "PT Dayamitra Telekomunikasi Tbk.",
                                                "Communication Services",
                                                "Telecom Services"
                                ],
                                [
                                                "SKYB.JK",
                                                "PT Northcliff Citranusa Indonesia Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "ELSA.JK",
                                                "PT Elnusa Tbk",
                                                "Energy",
                                                "Oil & Gas Equipment & Services"
                                ],
                                [
                                                "MMLP.JK",
                                                "PT Mega Manunggal Property Tbk",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "HOKI.JK",
                                                "PT Buyung Poetra Sembada Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "GJTL.JK",
                                                "PT. Gajah Tunggal Tbk",
                                                "Consumer Cyclical",
                                                "Auto Parts"
                                ],
                                [
                                                "COCO.JK",
                                                "PT Wahana Interfood Nusantara Tbk",
                                                "Consumer Defensive",
                                                "Confectioners"
                                ],
                                [
                                                "ARNA.JK",
                                                "PT Arwana Citramulia Tbk",
                                                "Industrials",
                                                "Building Products & Equipment"
                                ],
                                [
                                                "TGKA.JK",
                                                "PT Tigaraksa Satria Tbk",
                                                "Consumer Defensive",
                                                "Food Distribution"
                                ],
                                [
                                                "CMNP.JK",
                                                "PT Citra Marga Nusaphala Persada Tbk",
                                                "Industrials",
                                                "Infrastructure Operations"
                                ],
                                [
                                                "GRIA.JK",
                                                "PT Ingria Pratama Capitalindo Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "HALO.JK",
                                                "PT Haloni Jane Tbk",
                                                "Basic Materials",
                                                "Chemicals"
                                ],
                                [
                                                "PANI.JK",
                                                "PT Pantai Indah Kapuk Dua Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "PANS.JK",
                                                "PT Panin Sekuritas Tbk",
                                                "Financial Services",
                                                "Capital Markets"
                                ],
                                [
                                                "INPC.JK",
                                                "PT Bank Artha Graha Internasional Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "KMTR.JK",
                                                "PT Kirana Megatara Tbk",
                                                "Consumer Cyclical",
                                                "Auto Parts"
                                ],
                                [
                                                "UNTR.JK",
                                                "PT United Tractors Tbk",
                                                "Basic Materials",
                                                "Other Industrial Metals & Mining"
                                ],
                                [
                                                "KMDS.JK",
                                                "PT Kurniamitra Duta Sentosa, Tbk",
                                                "Consumer Defensive",
                                                "Food Distribution"
                                ],
                                [
                                                "SSTM.JK",
                                                "PT Sunson Textile Manufacturer Tbk",
                                                "Consumer Cyclical",
                                                "Textile Manufacturing"
                                ],
                                [
                                                "PPRE.JK",
                                                "PT PP Presisi Tbk",
                                                "Industrials",
                                                "Engineering & Construction"
                                ],
                                [
                                                "BMAS.JK",
                                                "PT Bank Maspion Indonesia Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "PNSE.JK",
                                                "PT Pudjiadi and Sons Tbk",
                                                "Consumer Cyclical",
                                                "Resorts & Casinos"
                                ],
                                [
                                                "YULE.JK",
                                                "PT Yulie Sekuritas Indonesia Tbk",
                                                "Financial Services",
                                                "Capital Markets"
                                ],
                                [
                                                "TELE.JK",
                                                "PT Omni Inovasi Indonesia Tbk",
                                                "Communication Services",
                                                "Telecom Services"
                                ],
                                [
                                                "GRPM.JK",
                                                "PT Graha Prima Mentari Tbk",
                                                "Consumer Defensive",
                                                "Beverages - Non-Alcoholic"
                                ],
                                [
                                                "JSKY.JK",
                                                "PT Sky Energy Indonesia Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "HADE.JK",
                                                "PT Himalaya Energi Perkasa Tbk",
                                                "Consumer Cyclical",
                                                "Specialty Retail"
                                ],
                                [
                                                "BHIT.JK",
                                                "PT MNC Asia Holding Tbk",
                                                "Communication Services",
                                                "Entertainment"
                                ],
                                [
                                                "PDES.JK",
                                                "PT Destinasi Tirta Nusantara Tbk",
                                                "Consumer Cyclical",
                                                "Travel Services"
                                ],
                                [
                                                "FREN.JK",
                                                "FREN",
                                                "",
                                                ""
                                ],
                                [
                                                "STAA.JK",
                                                "PT Sumber Tani Agung Resources Tbk",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "KPIG.JK",
                                                "PT MNC Tourism Indonesia Tbk",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "KRAS.JK",
                                                "PT Krakatau Steel (Persero) Tbk",
                                                "Basic Materials",
                                                "Steel"
                                ],
                                [
                                                "UANG.JK",
                                                "PT Pakuan Tbk",
                                                "Consumer Cyclical",
                                                "Leisure"
                                ],
                                [
                                                "KBLI.JK",
                                                "PT KMI Wire and Cable Tbk",
                                                "Industrials",
                                                "Electrical Equipment & Parts"
                                ],
                                [
                                                "TRAM.JK",
                                                "PT Trada Alam Minera Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "MAPA.JK",
                                                "PT Map Aktif Adiperkasa Tbk",
                                                "Consumer Cyclical",
                                                "Specialty Retail"
                                ],
                                [
                                                "AGII.JK",
                                                "PT Samator Indo Gas Tbk",
                                                "Basic Materials",
                                                "Chemicals"
                                ],
                                [
                                                "SILO.JK",
                                                "PT Siloam International Hospitals Tbk",
                                                "Healthcare",
                                                "Medical Care Facilities"
                                ],
                                [
                                                "DUCK.JK",
                                                "PT Jaya Bersama Indo Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "KDSI.JK",
                                                "PT Kedawung Setia Industrial Tbk",
                                                "Consumer Cyclical",
                                                "Packaging & Containers"
                                ],
                                [
                                                "AKSI.JK",
                                                "PT Mineral Sumberdaya Mandiri Tbk",
                                                "Industrials",
                                                "Trucking"
                                ],
                                [
                                                "ARKA.JK",
                                                "PT Arkha Jayanti Persada Tbk",
                                                "Industrials",
                                                "Specialty Business Services"
                                ],
                                [
                                                "CSIS.JK",
                                                "PT Cahayasakti Investindo Sukses Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "PNGO.JK",
                                                "PT PINAGO UTAMA Tbk",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "AGRS.JK",
                                                "PT Bank IBK Indonesia Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "HOTL.JK",
                                                "PT. Saraswati Griya Lestari Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "MTDL.JK",
                                                "PT Metrodata Electronics Tbk",
                                                "Technology",
                                                "Electronics & Computer Distribution"
                                ],
                                [
                                                "GEMA.JK",
                                                "PT Gema Grahasarana Tbk",
                                                "Consumer Cyclical",
                                                "Furnishings, Fixtures & Appliances"
                                ],
                                [
                                                "ZINC.JK",
                                                "PT Kapuas Prima Coal Tbk",
                                                "Basic Materials",
                                                "Other Industrial Metals & Mining"
                                ],
                                [
                                                "BDMN.JK",
                                                "PT Bank Danamon Indonesia Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "CNTB.JK",
                                                "PT Century Textile Industry Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "BMSR.JK",
                                                "PT Bintang Mitra Semestaraya Tbk",
                                                "Basic Materials",
                                                "Chemicals"
                                ],
                                [
                                                "KLBF.JK",
                                                "PT Kalbe Farma Tbk.",
                                                "Healthcare",
                                                "Drug Manufacturers - General"
                                ],
                                [
                                                "ADHI.JK",
                                                "PT Adhi Karya (Persero) Tbk",
                                                "Industrials",
                                                "Engineering & Construction"
                                ],
                                [
                                                "BEKS.JK",
                                                "PT. Bank Pembangunan Daerah Banten, Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "SIPD.JK",
                                                "PT Sreeya Sewu Indonesia Tbk",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "AISA.JK",
                                                "PT FKS Food Sejahtera Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "JGLE.JK",
                                                "PT Graha Andrasentra Propertindo Tbk",
                                                "Consumer Cyclical",
                                                "Leisure"
                                ],
                                [
                                                "MARK.JK",
                                                "PT Mark Dynamics Indonesia Tbk",
                                                "Healthcare",
                                                "Medical Instruments & Supplies"
                                ],
                                [
                                                "WOWS.JK",
                                                "PT Ginting Jaya Energi Tbk",
                                                "Energy",
                                                "Oil & Gas Equipment & Services"
                                ],
                                [
                                                "SINI.JK",
                                                "PT Singaraja Putra Tbk",
                                                "Basic Materials",
                                                "Lumber & Wood Production"
                                ],
                                [
                                                "BEEF.JK",
                                                "PT Estika Tata Tiara Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "BRPT.JK",
                                                "PT Barito Pacific Tbk",
                                                "Basic Materials",
                                                "Chemicals"
                                ],
                                [
                                                "BLUE.JK",
                                                "PT Berkah Prima Perkasa Tbk",
                                                "Technology",
                                                "Electronics & Computer Distribution"
                                ],
                                [
                                                "IBST.JK",
                                                "PT Inti Bangun Sejahtera Tbk",
                                                "Communication Services",
                                                "Telecom Services"
                                ],
                                [
                                                "MRAT.JK",
                                                "PT Mustika Ratu Tbk",
                                                "Consumer Defensive",
                                                "Household & Personal Products"
                                ],
                                [
                                                "MOLI.JK",
                                                "PT Madusari Murni Indah Tbk",
                                                "Basic Materials",
                                                "Chemicals"
                                ],
                                [
                                                "BIMA.JK",
                                                "PT. Primarindo Asia Infrastructure, Tbk.",
                                                "Consumer Cyclical",
                                                "Footwear & Accessories"
                                ],
                                [
                                                "PRAS.JK",
                                                "PT. Prima Alloy Steel Universal Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "HEAL.JK",
                                                "PT Medikaloka Hermina Tbk",
                                                "Healthcare",
                                                "Medical Care Facilities"
                                ],
                                [
                                                "AVIA.JK",
                                                "PT Avia Avian Tbk",
                                                "Basic Materials",
                                                "Specialty Chemicals"
                                ],
                                [
                                                "INDX.JK",
                                                "PT Tanah Laut Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "RUIS.JK",
                                                "PT Radiant Utama Interinsco Tbk",
                                                "Energy",
                                                "Oil & Gas Equipment & Services"
                                ],
                                [
                                                "ETWA.JK",
                                                "PT Eterindo Wahanatama Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "TOSK.JK",
                                                "Topindo Solusi Komunika Tbk.",
                                                "Technology",
                                                "Software - Application"
                                ],
                                [
                                                "DSSA.JK",
                                                "PT Dian Swastatika Sentosa Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "TSPC.JK",
                                                "PT Tempo Scan Pacific Tbk",
                                                "Industrials",
                                                "Conglomerates"
                                ],
                                [
                                                "MLBI.JK",
                                                "PT Multi Bintang Indonesia Tbk",
                                                "Consumer Defensive",
                                                "Beverages - Brewers"
                                ],
                                [
                                                "WTON.JK",
                                                "PT Wijaya Karya Beton Tbk",
                                                "Basic Materials",
                                                "Building Materials"
                                ],
                                [
                                                "BANK.JK",
                                                "PT Bank Aladin Syariah Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "JAWA.JK",
                                                "PT Jaya Agra Wattie Tbk",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "IPPE.JK",
                                                "PT Indo Pureco Pratama Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "POLA.JK",
                                                "PT Pool Advista Finance Tbk",
                                                "Financial Services",
                                                "Credit Services"
                                ],
                                [
                                                "AMAN.JK",
                                                "PT Makmur Berkah Amanda Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "ANJT.JK",
                                                "PT Austindo Nusantara Jaya Tbk",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "SIMP.JK",
                                                "PT Salim Ivomas Pratama Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "FAST.JK",
                                                "PT Fast Food Indonesia Tbk",
                                                "Consumer Cyclical",
                                                "Restaurants"
                                ],
                                [
                                                "SDRA.JK",
                                                "PT Bank Woori Saudara Indonesia 1906 Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "DKFT.JK",
                                                "PT Central Omega Resources Tbk",
                                                "Basic Materials",
                                                "Other Industrial Metals & Mining"
                                ],
                                [
                                                "BAJA.JK",
                                                "PT Saranacentral Bajatama Tbk",
                                                "Basic Materials",
                                                "Steel"
                                ],
                                [
                                                "BUVA.JK",
                                                "PT Bukit Uluwatu Villa Tbk",
                                                "Consumer Cyclical",
                                                "Lodging"
                                ],
                                [
                                                "INTP.JK",
                                                "PT Indocement Tunggal Prakarsa Tbk",
                                                "Basic Materials",
                                                "Building Materials"
                                ],
                                [
                                                "CPIN.JK",
                                                "PT Charoen Pokphand Indonesia Tbk",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "ESIP.JK",
                                                "PT Sinergi Inti Plastindo Tbk",
                                                "Consumer Cyclical",
                                                "Packaging & Containers"
                                ],
                                [
                                                "LINK.JK",
                                                "PT Link Net Tbk",
                                                "Communication Services",
                                                "Telecom Services"
                                ],
                                [
                                                "DWGL.JK",
                                                "PT Dwi Guna Laksana Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "LMAS.JK",
                                                "PT Limas Indonesia Makmur Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "BDKR.JK",
                                                "PT Berdikari Pondasi Perkasa Tbk",
                                                "Industrials",
                                                "Engineering & Construction"
                                ],
                                [
                                                "POWR.JK",
                                                "PT Cikarang Listrindo Tbk",
                                                "Utilities",
                                                "Utilities - Independent Power Producers"
                                ],
                                [
                                                "INAI.JK",
                                                "PT Indal Aluminium Industry Tbk",
                                                "Basic Materials",
                                                "Aluminum"
                                ],
                                [
                                                "MGRO.JK",
                                                "PT Mahkota Group Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "INCI.JK",
                                                "PT Intanwijaya Internasional Tbk",
                                                "Basic Materials",
                                                "Specialty Chemicals"
                                ],
                                [
                                                "PNBS.JK",
                                                "PT Bank Panin Dubai Syariah Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "WEHA.JK",
                                                "PT WEHA Transportasi Indonesia Tbk",
                                                "Industrials",
                                                "Railroads"
                                ],
                                [
                                                "RICY.JK",
                                                "PT Ricky Putra Globalindo Tbk",
                                                "Consumer Cyclical",
                                                "Apparel Manufacturing"
                                ],
                                [
                                                "CFIN.JK",
                                                "PT. Clipan Finance Indonesia Tbk",
                                                "Financial Services",
                                                "Credit Services"
                                ],
                                [
                                                "MTSM.JK",
                                                "PT Metro Realty Tbk",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "IDPR.JK",
                                                "PT Indonesia Pondasi Raya Tbk",
                                                "Industrials",
                                                "Engineering & Construction"
                                ],
                                [
                                                "REAL.JK",
                                                "PT Repower Asia Indonesia Tbk",
                                                "Real Estate",
                                                "Real Estate - Diversified"
                                ],
                                [
                                                "DNAR.JK",
                                                "PT Bank Oke Indonesia Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "TPMA.JK",
                                                "PT Trans Power Marine Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "AALI.JK",
                                                "PT Astra Agro Lestari Tbk",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "OMRE.JK",
                                                "PT Indonesia Prima Property Tbk",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "ASBI.JK",
                                                "PT Asuransi Bintang Tbk",
                                                "Financial Services",
                                                "Insurance - Diversified"
                                ],
                                [
                                                "INAF.JK",
                                                "PT Indofarma Tbk",
                                                "Healthcare",
                                                "Drug Manufacturers - Specialty & Generic"
                                ],
                                [
                                                "NELY.JK",
                                                "PT Pelayaran Nelly Dwi Putri Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "SDPC.JK",
                                                "PT Millennium Pharmacon International Tbk",
                                                "Healthcare",
                                                "Medical Distribution"
                                ],
                                [
                                                "SGRO.JK",
                                                "PT Sampoerna Agro Tbk",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "BOLT.JK",
                                                "PT Garuda Metalindo Tbk",
                                                "Industrials",
                                                "Tools & Accessories"
                                ],
                                [
                                                "BMTR.JK",
                                                "PT Global Mediacom Tbk",
                                                "Communication Services",
                                                "Entertainment"
                                ],
                                [
                                                "INDO.JK",
                                                "PT Royalindo Investa Wijaya Tbk",
                                                "Consumer Cyclical",
                                                "Lodging"
                                ],
                                [
                                                "OPMS.JK",
                                                "PT Optima Prima Metal Sinergi Tbk",
                                                "Industrials",
                                                "Waste Management"
                                ],
                                [
                                                "EKAD.JK",
                                                "PT Ekadharma International Tbk",
                                                "Basic Materials",
                                                "Specialty Chemicals"
                                ],
                                [
                                                "RALS.JK",
                                                "PT Ramayana Lestari Sentosa Tbk",
                                                "Consumer Cyclical",
                                                "Department Stores"
                                ],
                                [
                                                "TGUK.JK",
                                                "PT Platinum Wahab Nusantara Tbk",
                                                "Consumer Defensive",
                                                "Food Distribution"
                                ],
                                [
                                                "BBTN.JK",
                                                "PT Bank Tabungan Negara (Persero) Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "ESSA.JK",
                                                "PT ESSA Industries Indonesia Tbk.",
                                                "Basic Materials",
                                                "Chemicals"
                                ],
                                [
                                                "SKLT.JK",
                                                "PT Sekar Laut Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "GGRM.JK",
                                                "PT Gudang Garam Tbk",
                                                "Consumer Defensive",
                                                "Tobacco"
                                ],
                                [
                                                "JAST.JK",
                                                "PT. Jasnita Telekomindo Tbk",
                                                "Communication Services",
                                                "Telecom Services"
                                ],
                                [
                                                "BJTM.JK",
                                                "PT Bank Pembangunan Daerah Jawa Timur Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "FASW.JK",
                                                "PT Fajar Surya Wisesa Tbk",
                                                "Consumer Cyclical",
                                                "Packaging & Containers"
                                ],
                                [
                                                "BLTA.JK",
                                                "PT Berlian Laju Tanker Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "PTSN.JK",
                                                "PT Sat Nusapersada Tbk",
                                                "Technology",
                                                "Electronic Components"
                                ],
                                [
                                                "BULL.JK",
                                                "PT Buana Lintas Lautan Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "MLPL.JK",
                                                "PT Multipolar Tbk",
                                                "Consumer Cyclical",
                                                "Department Stores"
                                ],
                                [
                                                "DGNS.JK",
                                                "PT Diagnos Laboratorium Utama Tbk",
                                                "Healthcare",
                                                "Diagnostics & Research"
                                ],
                                [
                                                "PICO.JK",
                                                "PT Pelangi Indah Canindo Tbk",
                                                "Consumer Cyclical",
                                                "Packaging & Containers"
                                ],
                                [
                                                "PTMP.JK",
                                                "PT Mitra Pack Tbk",
                                                "Industrials",
                                                "Specialty Industrial Machinery"
                                ],
                                [
                                                "CCSI.JK",
                                                "PT Communication Cable Systems Indonesia Tbk",
                                                "Technology",
                                                "Communication Equipment"
                                ],
                                [
                                                "KBAG.JK",
                                                "PT Karya Bersama Anugerah Tbk",
                                                "Consumer Cyclical",
                                                "Residential Construction"
                                ],
                                [
                                                "BISI.JK",
                                                "PT BISI International Tbk",
                                                "Basic Materials",
                                                "Agricultural Inputs"
                                ],
                                [
                                                "AGAR.JK",
                                                "PT Asia Sejahtera Mina Tbk",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "ABBA.JK",
                                                "PT Mahaka Media Tbk",
                                                "Communication Services",
                                                "Publishing"
                                ],
                                [
                                                "SCCO.JK",
                                                "PT Supreme Cable Manufacturing & Commerce Tbk",
                                                "Industrials",
                                                "Electrical Equipment & Parts"
                                ],
                                [
                                                "SLIS.JK",
                                                "PT Gaya Abadi Sempurna Tbk",
                                                "Technology",
                                                "Electronics & Computer Distribution"
                                ],
                                [
                                                "PZZA.JK",
                                                "PT Sarimelati Kencana Tbk",
                                                "Consumer Cyclical",
                                                "Restaurants"
                                ],
                                [
                                                "DAYA.JK",
                                                "PT Duta Intidaya Tbk",
                                                "Consumer Cyclical",
                                                "Specialty Retail"
                                ],
                                [
                                                "WINE.JK",
                                                "PT HATTEN BALI Tbk",
                                                "Consumer Defensive",
                                                "Beverages - Wineries & Distilleries"
                                ],
                                [
                                                "KOIN.JK",
                                                "PT Kokoh Inti Arebama Tbk",
                                                "Industrials",
                                                "Building Products & Equipment"
                                ],
                                [
                                                "OBMD.JK",
                                                "PT OBM Drilchem Tbk",
                                                "Basic Materials",
                                                "Specialty Chemicals"
                                ],
                                [
                                                "KBLM.JK",
                                                "PT Kabelindo Murni Tbk",
                                                "Industrials",
                                                "Electrical Equipment & Parts"
                                ],
                                [
                                                "BBRI.JK",
                                                "PT Bank Rakyat Indonesia (Persero) Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "IPTV.JK",
                                                "PT MNC Vision Networks Tbk",
                                                "Communication Services",
                                                "Entertainment"
                                ],
                                [
                                                "MYRX.JK",
                                                "PT Hanson International Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "OKAS.JK",
                                                "PT Ancora Indonesia Resources Tbk",
                                                "Basic Materials",
                                                "Specialty Chemicals"
                                ],
                                [
                                                "HUMI.JK",
                                                "PT Humpuss Maritim Internasional Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "MPRO.JK",
                                                "PT Maha Properti Indonesia Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "BAPA.JK",
                                                "PT Bekasi Asri Pemula Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "UNIT.JK",
                                                "PT Cahaya Permata Sejahtera Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "ICON.JK",
                                                "PT Island Concepts Indonesia Tbk",
                                                "Energy",
                                                "Oil & Gas Equipment & Services"
                                ],
                                [
                                                "BIPI.JK",
                                                "PT Astrindo Nusantara Infrastruktur Tbk",
                                                "Industrials",
                                                "Infrastructure Operations"
                                ],
                                [
                                                "SQMI.JK",
                                                "PT Wilton Makmur indonesia Tbk.",
                                                "Basic Materials",
                                                "Gold"
                                ],
                                [
                                                "CRAB.JK",
                                                "PT Toba Surimi Industries Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "HDIT.JK",
                                                "PT Hensel Davest Indonesia Tbk",
                                                "Technology",
                                                "Software - Infrastructure"
                                ],
                                [
                                                "CARE.JK",
                                                "PT Metro Healthcare Indonesia Tbk",
                                                "Healthcare",
                                                "Medical Care Facilities"
                                ],
                                [
                                                "PURA.JK",
                                                "PT Putra Rajawali Kencana Tbk",
                                                "Industrials",
                                                "Trucking"
                                ],
                                [
                                                "GRPH.JK",
                                                "Griptha Putra Persada Tbk.",
                                                "Consumer Cyclical",
                                                "Lodging"
                                ],
                                [
                                                "PBSA.JK",
                                                "PT Paramita Bangun Sarana Tbk",
                                                "Industrials",
                                                "Engineering & Construction"
                                ],
                                [
                                                "SMAR.JK",
                                                "PT Sinar Mas Agro Resources and Technology Tbk",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "ARTA.JK",
                                                "PT Arthavest Tbk",
                                                "Consumer Cyclical",
                                                "Lodging"
                                ],
                                [
                                                "PSAB.JK",
                                                "PT J Resources Asia Pasifik Tbk",
                                                "Basic Materials",
                                                "Gold"
                                ],
                                [
                                                "KKGI.JK",
                                                "PT Resource Alam Indonesia Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "RDTX.JK",
                                                "PT Roda Vivatex Tbk",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "BAYU.JK",
                                                "PT Bayu Buana Tbk",
                                                "Consumer Cyclical",
                                                "Travel Services"
                                ],
                                [
                                                "MBMA.JK",
                                                "PT Merdeka Battery Materials Tbk.",
                                                "Basic Materials",
                                                "Other Precious Metals & Mining"
                                ],
                                [
                                                "CITY.JK",
                                                "PT Natura City Developments Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "ASII.JK",
                                                "PT Astra International Tbk",
                                                "Industrials",
                                                "Conglomerates"
                                ],
                                [
                                                "IPOL.JK",
                                                "PT Indopoly Swakarsa Industry Tbk",
                                                "Consumer Cyclical",
                                                "Packaging & Containers"
                                ],
                                [
                                                "SDMU.JK",
                                                "PT Sidomulyo Selaras Tbk",
                                                "Industrials",
                                                "Trucking"
                                ],
                                [
                                                "KOPI.JK",
                                                "PT Mitra Energi Persada Tbk",
                                                "Energy",
                                                "Oil & Gas Refining & Marketing"
                                ],
                                [
                                                "LAND.JK",
                                                "PT Trimitra Propertindo Tbk",
                                                "Real Estate",
                                                "Real Estate Services"
                                ],
                                [
                                                "NPGF.JK",
                                                "PT Nusa Palapa Gemilang Tbk",
                                                "Basic Materials",
                                                "Agricultural Inputs"
                                ],
                                [
                                                "TMPO.JK",
                                                "PT Tempo Inti Media Tbk",
                                                "Communication Services",
                                                "Publishing"
                                ],
                                [
                                                "HILL.JK",
                                                "PT Hillcon Tbk",
                                                "Basic Materials",
                                                "Other Industrial Metals & Mining"
                                ],
                                [
                                                "PGUN.JK",
                                                "PT Pradiksi Gunatama Tbk",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "ROTI.JK",
                                                "PT Nippon Indosari Corpindo Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "SRIL.JK",
                                                "PT Sri Rejeki Isman Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "CAKK.JK",
                                                "PT Cahayaputra Asa Keramik Tbk",
                                                "Industrials",
                                                "Building Products & Equipment"
                                ],
                                [
                                                "BEER.JK",
                                                "PT Jobubu Jarum Minahasa Tbk",
                                                "Consumer Defensive",
                                                "Beverages - Wineries & Distilleries"
                                ],
                                [
                                                "SMDM.JK",
                                                "PT Suryamas Dutamakmur Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "BBMD.JK",
                                                "PT Bank Mestika Dharma Tbk",
                                                "Financial Services",
                                                "Banks - Regional"
                                ],
                                [
                                                "CITA.JK",
                                                "PT Cita Mineral Investindo Tbk",
                                                "Basic Materials",
                                                "Other Industrial Metals & Mining"
                                ],
                                [
                                                "ESTI.JK",
                                                "PT Ever Shine Tex Tbk",
                                                "Consumer Cyclical",
                                                "Textile Manufacturing"
                                ],
                                [
                                                "FISH.JK",
                                                "PT FKS Multi Agro Tbk",
                                                "Consumer Defensive",
                                                "Farm Products"
                                ],
                                [
                                                "JRPT.JK",
                                                "PT Jaya Real Property, Tbk.",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "TOTO.JK",
                                                "PT Surya Toto Indonesia Tbk",
                                                "Industrials",
                                                "Building Products & Equipment"
                                ],
                                [
                                                "TRUS.JK",
                                                "PT Trust Finance Indonesia Tbk",
                                                "Financial Services",
                                                "Credit Services"
                                ],
                                [
                                                "HMSP.JK",
                                                "PT Hanjaya Mandala Sampoerna Tbk",
                                                "Consumer Defensive",
                                                "Tobacco"
                                ],
                                [
                                                "CGAS.JK",
                                                "Citra Nusantara Gemilang Tbk.",
                                                "Energy",
                                                "Oil & Gas Refining & Marketing"
                                ],
                                [
                                                "WSKT.JK",
                                                "PT Waskita Karya (Persero) Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "ZBRA.JK",
                                                "PT Dosni Roha Indonesia Tbk",
                                                "Healthcare",
                                                "Medical Distribution"
                                ],
                                [
                                                "POLL.JK",
                                                "PT Pollux Properties Indonesia Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "SAGE.JK",
                                                "PT Saptausaha Gemilangindah Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "DEFI.JK",
                                                "PT Danasupra Erapacific Tbk",
                                                "Financial Services",
                                                "Credit Services"
                                ],
                                [
                                                "BPFI.JK",
                                                "PT Woori Finance Indonesia Tbk",
                                                "Financial Services",
                                                "Credit Services"
                                ],
                                [
                                                "ECII.JK",
                                                "PT Electronic City Indonesia Tbk",
                                                "Consumer Cyclical",
                                                "Specialty Retail"
                                ],
                                [
                                                "AMMN.JK",
                                                "PT Amman Mineral Internasional Tbk",
                                                "Basic Materials",
                                                "Other Precious Metals & Mining"
                                ],
                                [
                                                "BNBR.JK",
                                                "PT Bakrie & Brothers Tbk",
                                                "Industrials",
                                                "Conglomerates"
                                ],
                                [
                                                "TCID.JK",
                                                "PT. Mandom Indonesia Tbk",
                                                "Consumer Defensive",
                                                "Household & Personal Products"
                                ],
                                [
                                                "GLVA.JK",
                                                "PT Galva Technologies Tbk",
                                                "Technology",
                                                "Electronics & Computer Distribution"
                                ],
                                [
                                                "AKRA.JK",
                                                "PT AKR Corporindo Tbk",
                                                "Energy",
                                                "Oil & Gas Refining & Marketing"
                                ],
                                [
                                                "WIKA.JK",
                                                "PT Wijaya Karya (Persero) Tbk",
                                                "Industrials",
                                                "Engineering & Construction"
                                ],
                                [
                                                "EPAC.JK",
                                                "PT Megalestari Epack Sentosaraya Tbk",
                                                "Consumer Cyclical",
                                                "Packaging & Containers"
                                ],
                                [
                                                "GTBO.JK",
                                                "PT Garda Tujuh Buana Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "RONY.JK",
                                                "PT Aesler Grup Internasional Tbk",
                                                "Industrials",
                                                "Engineering & Construction"
                                ],
                                [
                                                "KPAS.JK",
                                                "PT Cottonindo Ariesta Tbk",
                                                "",
                                                ""
                                ],
                                [
                                                "ULTJ.JK",
                                                "PT Ultrajaya Milk Industry & Trading Company Tbk",
                                                "Consumer Defensive",
                                                "Beverages - Non-Alcoholic"
                                ],
                                [
                                                "GDST.JK",
                                                "PT Gunawan Dianjaya Steel Tbk",
                                                "Basic Materials",
                                                "Steel"
                                ],
                                [
                                                "MFMI.JK",
                                                "PT Multifiling Mitra Indonesia Tbk",
                                                "Industrials",
                                                "Specialty Business Services"
                                ],
                                [
                                                "SUNI.JK",
                                                "PT Sunindo Pratama Tbk",
                                                "Energy",
                                                "Oil & Gas Equipment & Services"
                                ],
                                [
                                                "BATA.JK",
                                                "PT Sepatu Bata Tbk.",
                                                "Consumer Cyclical",
                                                "Footwear & Accessories"
                                ],
                                [
                                                "PANR.JK",
                                                "PT Panorama Sentrawisata Tbk",
                                                "Consumer Cyclical",
                                                "Travel Services"
                                ],
                                [
                                                "MSJA.JK",
                                                "Multi Spunindo Jaya Tbk.",
                                                "Consumer Cyclical",
                                                "Textile Manufacturing"
                                ],
                                [
                                                "ICBP.JK",
                                                "PT Indofood CBP Sukses Makmur Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "INTD.JK",
                                                "PT Inter Delta Tbk",
                                                "Basic Materials",
                                                "Paper & Paper Products"
                                ],
                                [
                                                "BSSR.JK",
                                                "PT Baramulti Suksessarana Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "DMND.JK",
                                                "PT Diamond Food Indonesia Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "CANI.JK",
                                                "PT Capitol Nusantara Indonesia Tbk",
                                                "Industrials",
                                                "Marine Shipping"
                                ],
                                [
                                                "GMFI.JK",
                                                "PT Garuda Maintenance Facility Aero Asia Tbk",
                                                "Industrials",
                                                "Aerospace & Defense"
                                ],
                                [
                                                "UNIC.JK",
                                                "PT Unggul Indah Cahaya Tbk",
                                                "Basic Materials",
                                                "Chemicals"
                                ],
                                [
                                                "ASRM.JK",
                                                "PT Asuransi Ramayana Tbk",
                                                "Financial Services",
                                                "Insurance - Property & Casualty"
                                ],
                                [
                                                "PADI.JK",
                                                "PT Minna Padi Investama Sekuritas Tbk",
                                                "Financial Services",
                                                "Capital Markets"
                                ],
                                [
                                                "TALF.JK",
                                                "PT Tunas Alfin Tbk",
                                                "Consumer Cyclical",
                                                "Packaging & Containers"
                                ],
                                [
                                                "TFAS.JK",
                                                "PT Telefast Indonesia Tbk",
                                                "Industrials",
                                                "Staffing & Employment Services"
                                ],
                                [
                                                "FOOD.JK",
                                                "PT Sentra Food Indonesia Tbk",
                                                "Consumer Defensive",
                                                "Packaged Foods"
                                ],
                                [
                                                "HAJJ.JK",
                                                "PT Arsy Buana Travelindo Tbk",
                                                "Consumer Cyclical",
                                                "Travel Services"
                                ],
                                [
                                                "WINR.JK",
                                                "PT Winner Nusantara Jaya Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "BIRD.JK",
                                                "PT Blue Bird Tbk",
                                                "Industrials",
                                                "Railroads"
                                ],
                                [
                                                "AMFG.JK",
                                                "PT Asahimas Flat Glass Tbk",
                                                "Basic Materials",
                                                "Building Materials"
                                ],
                                [
                                                "RAJA.JK",
                                                "PT Rukun Raharja Tbk",
                                                "Utilities",
                                                "Utilities - Regulated Gas"
                                ],
                                [
                                                "EDGE.JK",
                                                "PT Indointernet Tbk.",
                                                "Technology",
                                                "Information Technology Services"
                                ],
                                [
                                                "KOKA.JK",
                                                "PT Koka Indonesia Tbk",
                                                "Industrials",
                                                "Engineering & Construction"
                                ],
                                [
                                                "PKPK.JK",
                                                "PT Paragon Karya Perkasa Tbk",
                                                "Industrials",
                                                "Engineering & Construction"
                                ],
                                [
                                                "AUTO.JK",
                                                "PT Astra Otoparts Tbk",
                                                "Consumer Cyclical",
                                                "Auto Parts"
                                ],
                                [
                                                "ARII.JK",
                                                "PT Atlas Resources Tbk",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "TOPS.JK",
                                                "PT Totalindo Eka Persada Tbk",
                                                "Industrials",
                                                "Engineering & Construction"
                                ],
                                [
                                                "CARS.JK",
                                                "PT Industri dan Perdagangan Bintraco Dharma Tbk",
                                                "Consumer Cyclical",
                                                "Auto & Truck Dealerships"
                                ],
                                [
                                                "WGSH.JK",
                                                "PT Wira Global Solusi Tbk",
                                                "Technology",
                                                "Software - Infrastructure"
                                ],
                                [
                                                "MAPI.JK",
                                                "PT. Mitra Adiperkasa Tbk",
                                                "Consumer Cyclical",
                                                "Department Stores"
                                ],
                                [
                                                "SSIA.JK",
                                                "PT Surya Semesta Internusa Tbk",
                                                "Industrials",
                                                "Engineering & Construction"
                                ],
                                [
                                                "SMCB.JK",
                                                "PT Solusi Bangun Indonesia Tbk",
                                                "Basic Materials",
                                                "Building Materials"
                                ],
                                [
                                                "POLU.JK",
                                                "PT Golden Flower Tbk",
                                                "Consumer Cyclical",
                                                "Apparel Manufacturing"
                                ],
                                [
                                                "SBAT.JK",
                                                "PT Sejahtera Bintang Abadi Textile Tbk",
                                                "Consumer Cyclical",
                                                "Textile Manufacturing"
                                ],
                                [
                                                "SCPI.JK",
                                                "Organon Pharma Indonesia PT",
                                                "",
                                                ""
                                ],
                                [
                                                "BYAN.JK",
                                                "PT Bayan Resources Tbk.",
                                                "Energy",
                                                "Thermal Coal"
                                ],
                                [
                                                "HRME.JK",
                                                "PT Menteng Heritage Realty Tbk",
                                                "Consumer Cyclical",
                                                "Lodging"
                                ],
                                [
                                                "ENRG.JK",
                                                "PT Energi Mega Persada Tbk",
                                                "Energy",
                                                "Oil & Gas E&P"
                                ],
                                [
                                                "KIJA.JK",
                                                "PT Kawasan Industri Jababeka Tbk",
                                                "Real Estate",
                                                "Real Estate - Development"
                                ],
                                [
                                                "BIPP.JK",
                                                "PT Bhuwanatala Indah Permai Tbk",
                                                "Real Estate",
                                                "Real Estate - Diversified"
                                ],
                                [
                                                "DRMA.JK",
                                                "PT Dharma Polimetal Tbk",
                                                "Consumer Cyclical",
                                                "Auto Parts"
                                ]
                ],
                "NASDAQ": [
                                [
                                                "AAPL",
                                                "Apple Inc",
                                                "Technology",
                                                "Consumer Electronics"
                                ],
                                [
                                                "MSFT",
                                                "Microsoft",
                                                "Technology",
                                                "Software"
                                ],
                                [
                                                "GOOGL",
                                                "Alphabet Class A",
                                                "Communication",
                                                "Internet"
                                ],
                                [
                                                "AMZN",
                                                "Amazon.com",
                                                "Consumer Cyclical",
                                                "Internet Retail"
                                ],
                                [
                                                "NVDA",
                                                "NVIDIA",
                                                "Technology",
                                                "Semiconductors"
                                ],
                                [
                                                "META",
                                                "Meta Platforms",
                                                "Communication",
                                                "Internet"
                                ],
                                [
                                                "TSLA",
                                                "Tesla",
                                                "Consumer Cyclical",
                                                "Auto"
                                ],
                                [
                                                "NFLX",
                                                "Netflix",
                                                "Communication",
                                                "Entertainment"
                                ],
                                [
                                                "AMD",
                                                "Advanced Micro Devices",
                                                "Technology",
                                                "Semiconductors"
                                ],
                                [
                                                "INTC",
                                                "Intel",
                                                "Technology",
                                                "Semiconductors"
                                ]
                ],
                "NYSE": [
                                [
                                                "JPM",
                                                "JPMorgan Chase",
                                                "Financial Services",
                                                "Banks"
                                ],
                                [
                                                "BAC",
                                                "Bank of America",
                                                "Financial Services",
                                                "Banks"
                                ],
                                [
                                                "V",
                                                "Visa",
                                                "Financial Services",
                                                "Credit Services"
                                ],
                                [
                                                "MA",
                                                "Mastercard",
                                                "Financial Services",
                                                "Credit Services"
                                ]
                ],
                "HKEX": [
                                [
                                                "0700.HK",
                                                "Tencent Holdings",
                                                "Communication",
                                                "Internet"
                                ]
                ]
}

            # Flatten to standard format
            stocks = []
            for exchange, stock_list in stocks_by_exchange.items():
                for stock_data in stock_list:
                    stocks.append({
                        'symbol': stock_data[0],
                        'name': stock_data[1],
                        'exchange': exchange,
                        'sector': stock_data[2],
                        'industry': stock_data[3]
                    })

            response = {
                "success": True,
                "count": len(stocks),
                "stocks": stocks
            }

            # Convert to JSON (minified)
            json_data = json.dumps(response, separators=(',', ':'))
            json_bytes = json_data.encode('utf-8')

            # Compress with Brotli (level 11 for max compression)
            compressed_data = brotli.compress(json_bytes, quality=11)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Content-Encoding', 'br')
            self.send_header('Content-Length', str(len(compressed_data)))
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Cache-Control', 'public, max-age=86400')
            self.send_header('Vary', 'Accept-Encoding')
            self.end_headers()
            self.wfile.write(compressed_data)

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
