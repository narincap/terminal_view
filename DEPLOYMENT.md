# Vercel Deployment Guide

## What Was Fixed

Your backend wasn't working on Vercel because:
1. Frontend was hardcoded to fetch from `http://localhost:5001`
2. Flask server (`server.py`) can't run persistently on Vercel
3. Missing Vercel configuration and serverless API setup

## Changes Made

### 1. Created Serverless API Function
- **File**: `api/stock/[symbol].py`
- Converts Flask backend to Vercel serverless function
- Handles dynamic stock symbol routes
- Includes CORS headers for cross-origin requests

### 2. Added Vercel Configuration
- **File**: `vercel.json`
- Configures Python runtime for API routes
- Sets memory (1GB) and timeout (10s) limits
- Routes `/api/stock/*` to serverless function

### 3. Added Python Dependencies
- **File**: `requirements.txt`
- Lists packages: flask, flask-cors, yfinance, pandas
- Vercel installs these automatically during build

### 4. Updated Frontend
- **File**: `index.html` (line 368)
- Changed from `http://localhost:5001/api/stock/...` to `/api/stock/...`
- Now uses relative URLs that work on Vercel

### 5. Created Ignore File
- **File**: `.vercelignore`
- Excludes old `server.py` and unnecessary files

## How to Deploy

### Option A: Deploy via Vercel Dashboard
1. Go to [vercel.com](https://vercel.com)
2. Click "Add New Project"
3. Import your GitHub repository
4. Vercel auto-detects configuration
5. Click "Deploy"

### Option B: Deploy via Vercel CLI
```bash
# Install Vercel CLI (if not installed)
npm install -g vercel

# Deploy from project directory
cd /Users/rizkynarindra1611gmail.com/Documents/quant/tradingview
vercel

# Follow prompts to link project
# Deploy to production
vercel --prod
```

## Testing Locally (Optional)

To test the serverless function locally:

```bash
# Install Vercel CLI
npm install -g vercel

# Run local dev server
vercel dev
```

This starts:
- Frontend at `http://localhost:3000`
- API at `http://localhost:3000/api/stock/[symbol]`

## Verify Deployment

After deploying, test your API:

1. Visit your Vercel URL: `https://your-app.vercel.app`
2. Open browser console (F12)
3. Click "LOAD" button
4. Check console for API requests
5. Should see: `Fetching from API: /api/stock/BBCA.JK?interval=...`

## Troubleshooting

### "No data found for symbol"
- yfinance might be slow on first request (cold start)
- Try again after 10-15 seconds

### "Backend server not running"
- Check Vercel deployment logs
- Verify `api/stock/[symbol].py` deployed correctly
- Check Function logs in Vercel dashboard

### CORS Errors
- Serverless function includes CORS headers
- If still occurring, check browser console for exact error

## Important Notes

- **Old `server.py` is no longer needed** for Vercel deployment
- Keep it if you want to run locally: `python3 server.py`
- Serverless functions have **10 second timeout** (configurable in vercel.json)
- First request might be slow (cold start), subsequent requests are fast
- Free tier includes 100GB bandwidth/month

## Next Steps

1. Commit all changes to git
2. Push to GitHub
3. Deploy to Vercel
4. Test the live site

Your backend should now work on Vercel!
