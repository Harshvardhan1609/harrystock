# 📈 Dhando Stock

<div align="center">

```
██████╗ ██╗  ██╗ █████╗ ███╗   ██╗██████╗  ██████╗ 
██╔══██╗██║  ██║██╔══██╗████╗  ██║██╔══██╗██╔═══██╗
██║  ██║███████║███████║██╔██╗ ██║██║  ██║██║   ██║
██║  ██║██╔══██║██╔══██║██║╚██╗██║██║  ██║██║   ██║
██████╔╝██║  ██║██║  ██║██║ ╚████║██████╔╝╚██████╔╝
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ 
                    S T O C K
```

**Smart. Simple. Streamlit-Powered Stock Analysis.**

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![yFinance](https://img.shields.io/badge/yFinance-Live%20Data-00897B?style=for-the-badge&logo=yahoo&logoColor=white)](https://pypi.org/project/yfinance/)
[![License](https://img.shields.io/badge/License-MIT-F7DC6F?style=for-the-badge)](LICENSE)

</div>

---

## 🚀 What is Dhando Stock?

> *"Dhando" — a Gujarati word meaning "business." Inspired by the philosophy of low-risk, high-reward investing.*

**Dhando Stock** is an interactive, browser-based stock market dashboard built with **Streamlit**, **Pandas**, and **yFinance**. It empowers investors, traders, and enthusiasts to visualize, compare, and analyze stock data — without writing a single line of code at runtime.

Whether you're tracking your portfolio, comparing blue-chip stocks, or studying market trends, Dhando Stock gives you the tools to make informed decisions — fast.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📊 **Interactive Dashboard** | Fully responsive UI powered by Streamlit with real-time chart interactions |
| 🔍 **Stock Search** | Lookup any ticker symbol traded on NSE, BSE, NYSE, NASDAQ & more |
| 📅 **Comparison Ranges** | Compare stocks across custom date ranges — 1W, 1M, 3M, 6M, 1Y, 5Y, or custom |
| 📉 **Multi-Stock Comparison** | Plot multiple stocks on the same chart for side-by-side analysis |
| 💹 **Live Market Data** | Pulls real-time and historical data via the **yFinance API** |
| 📈 **Price & Volume Charts** | Candlestick charts, line charts, and volume bars |
| 📋 **Key Metrics Panel** | Current price, % change, market cap, P/E ratio, 52W High/Low |
| 🧮 **Returns Calculator** | Compare percentage returns between stocks over selected periods |
| 💾 **Export Data** | Download filtered stock data as CSV |

---

## 🛠️ Tech Stack

```
┌─────────────────────────────────────────────────────┐
│                  DHANDO STOCK STACK                  │
├─────────────────────┬───────────────────────────────┤
│  Frontend / UI      │  Streamlit                    │
│  Data Processing    │  Pandas, NumPy                │
│  Market Data API    │  yFinance (Yahoo Finance)     │
│  Charting           │  Plotly / Matplotlib          │
│  Language           │  Python 3.9+                  │
└─────────────────────┴───────────────────────────────┘
```

---

## 📦 Installation

### Prerequisites

Make sure you have **Python 3.9+** installed on your system.

```bash
python --version
# Python 3.9.x or higher
```

### Step 1 — Clone the Repository

```bash
git clone https://github.com/yourusername/dhando-stock.git
cd dhando-stock
```

### Step 2 — Create a Virtual Environment *(Recommended)*

```bash
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Run the App 🚀

```bash
streamlit run app.py
```

The app will open automatically at **`http://localhost:8501`**

---

## 📁 Project Structure

```
dhando-stock/
│
├── 📄 app.py                  # Main Streamlit application entry point
├── 📄 requirements.txt        # Python dependencies
├── 📄 README.md               # You are here!
│
├── 📂 components/
│   ├── dashboard.py           # Main dashboard layout
│   ├── charts.py              # Chart rendering (Plotly/Matplotlib)
│   ├── metrics.py             # Key stock metrics panel
│   └── comparison.py         # Multi-stock comparison logic
│
├── 📂 utils/
│   ├── fetcher.py             # yFinance data fetching helpers
│   ├── processor.py           # Pandas data processing
│   └── formatter.py          # Number & date formatting utilities
│
└── 📂 assets/
    └── styles.css             # Custom CSS overrides
```

---

## 🖥️ Usage Guide

### 🔎 Search a Stock
1. Enter a valid ticker symbol in the **search bar** (e.g., `RELIANCE.NS`, `TCS.NS`, `AAPL`, `TSLA`)
2. Hit **Enter** or click **Fetch Data**
3. The dashboard will load with current price, metrics, and historical charts

### 📅 Adjust Date Range
- Use the **range selector buttons** — `1W | 1M | 3M | 6M | 1Y | 5Y`
- Or pick a **custom date range** using the date pickers
- Charts and metrics update **instantly**

### 📊 Compare Multiple Stocks
1. Add multiple tickers using the **"Add Stock"** button
2. All selected stocks are plotted on a **unified comparison chart**
3. Returns (%) are normalized from the start date for fair comparison

### 💾 Export Data
- Click **"Download CSV"** to export the filtered dataset for offline analysis

---

## 📊 Sample Tickers to Try

| Exchange | Example Tickers |
|---|---|
| 🇮🇳 NSE India | `RELIANCE.NS` `TCS.NS` `INFY.NS` `HDFCBANK.NS` |
| 🇮🇳 BSE India | `RELIANCE.BO` `TCS.BO` `WIPRO.BO` |
| 🇺🇸 NASDAQ/NYSE | `AAPL` `MSFT` `GOOGL` `TSLA` `AMZN` |
| 📈 Indices | `^NSEI` (Nifty 50) `^BSESN` (Sensex) `^GSPC` (S&P 500) |

---

## 🔧 Requirements

```txt
streamlit>=1.28.0
pandas>=2.0.0
yfinance>=0.2.28
plotly>=5.17.0
numpy>=1.24.0
requests>=2.31.0
```

Install all at once:
```bash
pip install streamlit pandas yfinance plotly numpy requests
```

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

```bash
# 1. Fork the repository
# 2. Create your feature branch
git checkout -b feature/awesome-new-feature

# 3. Commit your changes
git commit -m "feat: add awesome new feature"

# 4. Push to the branch
git push origin feature/awesome-new-feature

# 5. Open a Pull Request
```

Please follow the **[Conventional Commits](https://www.conventionalcommits.org/)** standard for commit messages.

---

## 🐛 Known Issues / Roadmap

- [ ] 🔔 Price alert notifications
- [ ] 🤖 AI-powered stock sentiment analysis
- [ ] 📱 Mobile-optimized layout
- [ ] 🌙 Dark / Light mode toggle
- [ ] 📰 Live news feed integration
- [ ] 💼 Personal portfolio tracker with P&L

---

## ⚠️ Disclaimer

> **Dhando Stock is built for educational and informational purposes only.**
> Nothing in this application constitutes financial advice. Always do your own research (DYOR) before making any investment decisions. Past performance is not indicative of future results.

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

<div align="center">

Built with ❤️ by **[Your Name]**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/yourprofile)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/yourhandle)

---

*"The stock market is a device for transferring money from the impatient to the patient."*
— **Warren Buffett**

⭐ **Star this repo if you found it useful!**

</div>
