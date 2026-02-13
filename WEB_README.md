# Multi-Timeframe Chart Viewer - Web Application

A standalone web application for viewing Indonesian stock market data across multiple configurable timeframes.

## Features

✅ **Single HTML File** - No installation or build process required
✅ **Indonesian Stocks** - Full support for IDX stocks (Jakarta Stock Exchange)
✅ **Multiple Timeframes** - View 1m, 5m, 15m, 30m, 1h, 4h, 1D, 1W simultaneously
✅ **Dynamic Panels** - Add and remove timeframe panels as needed
✅ **Real-Time Data** - Fetches live data from Yahoo Finance
✅ **Beautiful Charts** - Powered by TradingView Lightweight Charts
✅ **Responsive Design** - Works on desktop, tablet, and mobile
✅ **No Backend** - Runs entirely in your browser

## Quick Start

### Option 1: Open Directly

1. Navigate to the `tradingview` folder
2. Double-click `index.html`
3. The app opens in your default browser
4. Done! Start exploring stocks

### Option 2: Open in Browser

1. Open your web browser (Chrome, Firefox, Safari, Edge)
2. Press `Cmd+O` (Mac) or `Ctrl+O` (Windows)
3. Navigate to and select `index.html`
4. Click "Open"

### Option 3: Using a Local Server (Optional)

```bash
# Navigate to the tradingview directory
cd /path/to/quant/tradingview

# Python 3
python3 -m http.server 8000

# Then open: http://localhost:8000
```

## How to Use

### Loading a Stock

1. **Enter Stock Symbol**
   - Type an Indonesian stock symbol in the input field
   - Examples: `BBCA.JK`, `TLKM.JK`, `ASII.JK`
   - The `.JK` suffix is auto-added if you forget it

2. **Click "Load Data"**
   - All panels will fetch and display data
   - Loading indicators show progress
   - Or press `Enter` in the input field

3. **Quick Select**
   - Use the quick select buttons for popular stocks
   - Click any button (BBCA, TLKM, ASII, etc.)
   - Data loads automatically

### Managing Panels

**Add a Panel:**
- Click the "➕ Add Panel" button
- New panel appears in the grid
- Select timeframe from dropdown
- Chart loads automatically if stock is selected

**Remove a Panel:**
- Click "✕ Remove" button in panel header
- Panel is deleted
- Note: You can't remove the last panel

**Change Timeframe:**
- Use the dropdown in each panel header
- Select different timeframe (1m, 5m, 15m, etc.)
- Chart updates automatically

### Available Timeframes

| Timeframe | Label | Data Range |
|-----------|-------|------------|
| 1m | 1 Minute | 1 day |
| 5m | 5 Minutes | 5 days |
| 15m | 15 Minutes | 5 days |
| 30m | 30 Minutes | 1 month |
| 1h | 1 Hour | 1 month |
| 4h | 4 Hours | 3 months |
| 1D | 1 Day | 1 year |
| 1W | 1 Week | 5 years |

### Chart Interactions

**Zoom:**
- Scroll wheel up/down
- Pinch on mobile

**Pan:**
- Click and drag on chart
- Swipe on mobile

**Crosshair:**
- Hover over chart
- See exact OHLC values
- View timestamps

**Reset View:**
- Double-click chart
- Or click timeframe dropdown again

## Popular Indonesian Stocks

Quick reference for stock symbols (all end with `.JK`):

**Banking:**
- BBCA.JK - Bank Central Asia
- BMRI.JK - Bank Mandiri
- BBRI.JK - Bank Rakyat Indonesia
- BBNI.JK - Bank Negara Indonesia

**Telecommunications:**
- TLKM.JK - Telkom Indonesia
- EXCL.JK - XL Axiata

**Consumer Goods:**
- UNVR.JK - Unilever Indonesia
- INDF.JK - Indofood Sukses Makmur

**Automotive:**
- ASII.JK - Astra International

**Technology:**
- GOTO.JK - GoTo Gojek Tokopedia

**Energy:**
- PGAS.JK - Perusahaan Gas Negara

## Default Configuration

When you open the app:
- Default stock: **BBCA.JK** (Bank Central Asia)
- Two panels: **15m** and **1D** timeframes
- Auto-loads on startup

## Troubleshooting

### Stock Not Found

**Problem:** "Stock not found" error appears

**Solutions:**
- Verify the stock symbol is correct
- Ensure `.JK` suffix is included (it's auto-added)
- Check if market is open (IDX hours: 9:00-16:00 WIB)
- Try a different stock to test connection

### No Data Available

**Problem:** "No data available for this timeframe" message

**Solutions:**
- Try a different timeframe
- 1-minute data only available for current day
- Some stocks may not have complete historical data
- Wait a moment and retry

### Failed to Load Data

**Problem:** "Failed to load data" error

**Solutions:**
- Check your internet connection
- The app automatically tries CORS proxy if direct fetch fails
- Refresh the page
- Try again in a few seconds (rate limiting)

### Charts Not Displaying

**Problem:** Blank panels or no charts visible

**Solutions:**
- Ensure JavaScript is enabled in browser
- Clear browser cache and reload page
- Try a different browser
- Check browser console for errors (F12)

### Performance Issues

**Problem:** App is slow or laggy

**Solutions:**
- Reduce number of panels (remove unused ones)
- Avoid having too many 1-minute panels
- Close other browser tabs
- Try on desktop instead of mobile

## Browser Compatibility

**Recommended Browsers:**
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

**Mobile Browsers:**
- ✅ iOS Safari 14+
- ✅ Chrome Mobile
- ✅ Samsung Internet

## Technical Details

**Data Source:**
- Yahoo Finance API (free, public endpoints)
- Real-time data with ~15-minute delay
- Historical OHLC data

**Chart Library:**
- TradingView Lightweight Charts
- Loaded via CDN (no installation)
- High-performance rendering

**Architecture:**
- Single HTML file (~600 lines)
- Vanilla JavaScript (no frameworks)
- Client-side only (no server)
- Responsive CSS Grid layout

## Keyboard Shortcuts

- `Enter` - Load data (when in stock input field)
- Scroll wheel - Zoom in/out on charts
- Click + Drag - Pan chart timeline

## Tips & Best Practices

1. **Start with 2-4 panels** - More panels = more API calls
2. **Use higher timeframes for overview** - 1D, 1W for big picture
3. **Use lower timeframes for entry** - 5m, 15m for timing
4. **Refresh data periodically** - Click "Load Data" to update
5. **Try quick select buttons** - Fastest way to switch stocks
6. **Resize browser window** - Charts auto-adjust to fit

## Example Workflows

### Day Trading Setup
```
Stock: BBCA.JK
Panels:
- 5m  (entry timing)
- 15m (short-term trend)
- 1h  (session context)
- 1D  (daily trend)
```

### Swing Trading Setup
```
Stock: TLKM.JK
Panels:
- 1h  (hourly movement)
- 4h  (intraday swing)
- 1D  (daily trend)
- 1W  (weekly context)
```

### Long-Term Analysis
```
Stock: ASII.JK
Panels:
- 1D  (daily bars)
- 1W  (weekly trend)
```

## Data Limitations

- **1-minute data:** Only current trading day
- **5-minute data:** Last 5 days
- **15-minute data:** Last 5 days
- **30-minute data:** Last 1 month
- **1-hour data:** Last 1 month
- **4-hour data:** Last 3 months
- **Daily data:** Last 1 year
- **Weekly data:** Last 5 years

## Privacy & Security

- ✅ No data collection
- ✅ No cookies or tracking
- ✅ No user accounts
- ✅ No data sent to any server
- ✅ All processing happens in your browser
- ✅ API calls go directly to Yahoo Finance

## Limitations

- Cannot display multiple stocks simultaneously
- No technical indicators (RSI, MACD, etc.)
- No drawing tools
- No alerts or notifications
- No data export functionality
- Requires internet connection

## Future Enhancements (Not Yet Implemented)

- Save layout to browser storage
- Multiple stock comparison
- Technical indicators overlay
- Volume display toggle
- Dark mode theme
- Chart screenshot export
- Real-time WebSocket updates
- Custom color themes

## Files

```
/tradingview/
  index.html              # Main application (single file)
  WEB_README.md          # This file
  MTF_Monitor.pine       # TradingView Pine Script (different tool)
  README.md              # Pine Script README
```

## Support & Issues

For problems or questions:
1. Check this README first
2. Try in a different browser
3. Clear cache and reload
4. Refer to design document: `../docs/plans/2026-02-13-mtf-web-viewer-design.md`

## License

MIT License - Free to use and modify

---

**Enjoy analyzing Indonesian stocks across multiple timeframes!** 🚀📈
