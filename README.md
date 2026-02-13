# MTF Monitor - Multi-Timeframe Monitor for TradingView

A TradingView Pine Script indicator that displays OHLC data from any timeframe as candlesticks or bars in separate panels.

## Quick Start

### Installation

1. Open TradingView and go to the Pine Editor (bottom of screen)
2. Click "New" → "Blank indicator script"
3. Delete the default code
4. Copy and paste the entire contents of `MTF_Monitor.pine`
5. Click "Save" and give it a name (e.g., "MTF Monitor")
6. Click "Add to Chart"

### Basic Usage

**Adding Multiple Timeframes:**

1. **Add first timeframe:**
   - The indicator should now appear on your chart in a separate panel
   - Click the gear icon ⚙️ next to "MTF Monitor" in the indicator list
   - Select your desired timeframe from the dropdown (e.g., "15" for 15 minutes)
   - Click "OK"

2. **Add more timeframes:**
   - Click "Indicators" button at top of chart
   - Find "MTF Monitor" in your list (under "My Scripts")
   - Click it again to add another instance
   - Configure it for a different timeframe (e.g., "60" for 1 hour)
   - Repeat for as many timeframes as you want

3. **Organize your panels:**
   - Drag panels up/down to reorder
   - Resize panels by dragging the borders
   - Right-click panel → Remove to delete one

## Configuration Options

### Timeframe Settings

- **Timeframe Preset:** Quick selection from common timeframes
  - 1, 3, 5, 15, 30 (minutes)
  - 60, 120, 240, 360, 720 (minutes/hours)
  - D (Daily), 3D (3 Days), W (Weekly), M (Monthly)

- **Manual Timeframe Override:** Enter custom values
  - Examples: "45" (45 min), "2H" (2 hours), "7D" (7 days)
  - Leave blank to use preset dropdown

### Visual Settings

- **Chart Type:** Switch between Candlesticks or OHLC Bars
- **Colors:**
  - Bullish Color (default: teal/green)
  - Bearish Color (default: red)
  - Custom border colors (optional)
  - Custom wick colors (optional)

### Optional Features

- **Show Volume:** Toggle volume bars at bottom of panel
- **Show Timeframe Label:** Display timeframe text (e.g., "15") on panel
- **Volume Colors:** Customize colors for up/down volume

### Data Mode

- **Confirmed bars only (no repaint):** Shows only closed bars (default, recommended)
- **Include current bar (live):** Shows live updating current bar (may repaint)

## Example Setups

### Day Trading Setup
```
Main Chart: 5-minute
Panel 1: MTF Monitor @ 15m
Panel 2: MTF Monitor @ 1h  (enter "60" or "1H")
Panel 3: MTF Monitor @ 4h  (enter "240" or "4H")
```

### Swing Trading Setup
```
Main Chart: 1-hour
Panel 1: MTF Monitor @ 4h  (enter "240")
Panel 2: MTF Monitor @ D
Panel 3: MTF Monitor @ W
```

### Scalping Setup
```
Main Chart: 1-minute
Panel 1: MTF Monitor @ 3
Panel 2: MTF Monitor @ 5
Panel 3: MTF Monitor @ 15
```

## Important Notes

- **Timeframe Limitation:** Selected timeframe must be >= your main chart timeframe
  - You CAN view higher timeframes (e.g., 1H on a 5m chart) ✅
  - You CANNOT view lower timeframes (e.g., 5m on a 1H chart) ❌
  - If you try, you'll see a warning message

- **Performance:** Each indicator instance is lightweight and uses minimal resources

- **Multiple Instances:** No limit on how many you can add, but 3-5 is typically most practical

## Customization Tips

1. **Color Coordination:** Use consistent color schemes across all your timeframe panels
2. **Panel Sizing:** Make higher timeframes slightly smaller since they update less frequently
3. **Volume Toggle:** Disable volume on higher timeframes if it clutters the view
4. **Save Layout:** Save your TradingView layout to preserve your multi-timeframe setup

## Troubleshooting

**Problem:** "Select timeframe >= chart timeframe" warning appears

**Solution:** The indicator cannot fetch lower timeframe data. Either:
- Increase the indicator's timeframe setting, OR
- Decrease your main chart's timeframe

**Problem:** Indicator not showing data

**Solution:**
- Check if the market is open (for non-24/7 markets)
- Verify the timeframe string is valid
- Try switching to preset dropdown instead of manual input

**Problem:** Bars look wrong or repaint

**Solution:** Make sure Data Mode is set to "Confirmed bars only (no repaint)"

## Files

- `MTF_Monitor.pine` - The indicator source code
- `README.md` - This file
- `../docs/plans/2026-02-13-multi-timeframe-monitor-design.md` - Complete design document

## License

Mozilla Public License 2.0

## Support

For issues or questions, refer to the design document in `docs/plans/` for detailed technical information.
