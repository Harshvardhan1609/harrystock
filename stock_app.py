import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import io

# Page config
st.set_page_config(
    page_title="dhando | Pro Intelligence",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize Session State
if 'watchlist' not in st.session_state:
    st.session_state.watchlist = ["AAPL", "NVDA", "BTC-USD"]

# dhando Maroon & Gold Premium Theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] { font-family: 'Outfit', sans-serif; }
    
    /* Maroon & Gold Design System */
    .stApp { background: radial-gradient(circle at top right, #300a0a, #121212); }
    
    [data-testid="stSidebar"] { 
        background-color: #4a0e0e !important; 
        border-right: 2px solid #d4af37;
    }
    
    /* Metric Cards Styling */
    [data-testid="stMetric"] {
        background-color: rgba(212, 175, 55, 0.05);
        border: 1px solid rgba(212, 175, 55, 0.2);
        padding: 15px;
        border-radius: 12px;
    }
    
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-weight: 900; }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #d4af37 0%, #8a6d3b 100%);
        color: #4a0e0e !important;
        border: none; border-radius: 8px; font-weight: 800;
        width: 100%; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        text-transform: uppercase; letter-spacing: 1px;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(212, 175, 55, 0.3);
        color: #4a0e0e !important;
    }
    
    /* Titles & Headers */
    .main-title {
        color: #d4af37;
        font-weight: 900; font-size: 4rem; margin-bottom: 0;
        text-shadow: 2px 2px 10px rgba(212, 175, 55, 0.2);
    }
    
    h1, h2, h3 { color: #d4af37 !important; }
    
    /* Footer Styling */
    .footer {
        text-align: center; padding: 2rem; color: rgba(212, 175, 55, 0.5);
        border-top: 1px solid rgba(212, 175, 55, 0.1); margin-top: 5rem;
    }
</style>
""", unsafe_allow_html=True)

def calculate_rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).ewm(com=period - 1, adjust=False).mean()
    loss = (-delta.where(delta < 0, 0)).ewm(com=period - 1, adjust=False).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

# App Header
st.markdown('<h1 class="main-title">dhando</h1>', unsafe_allow_html=True)
st.markdown("<p style='color: #d4af37; opacity: 0.8;'>The High-Performance Capital Intelligence Engine</p>", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("<h2 style='color: white !important;'>dhando</h2>", unsafe_allow_html=True)
    page = st.radio("Navigation", ["Deep Asset Analysis", "Market Benchmarking"], label_visibility="collapsed")
    
    st.markdown("---")
    st.markdown("<h3 style='color: white !important;'>Watchlist</h3>", unsafe_allow_html=True)
    for symbol in st.session_state.watchlist:
        w_cols = st.columns([0.7, 0.3])
        w_cols[0].markdown(f"<span style='color: white;'>{symbol}</span>", unsafe_allow_html=True)
        if w_cols[1].button("🗑️", key=f"del_{symbol}"):
            st.session_state.watchlist.remove(symbol)
            st.rerun()
    
    add_col1, add_col2 = st.columns([0.7, 0.3])
    new_ticker = add_col1.text_input("New", key="new_t", label_visibility="collapsed", placeholder="Ticker...")
    if add_col2.button("➕"):
        if new_ticker and new_ticker.upper() not in st.session_state.watchlist:
            st.session_state.watchlist.append(new_ticker.upper())
            st.rerun()

    st.markdown("---")
    plotly_theme = "plotly_dark" # Maroon theme looks best with dark charts

# Asset Analysis Page
if page == "Deep Asset Analysis":
    with st.sidebar:
        st.markdown("<h3 style='color: white !important;'>Parameters</h3>", unsafe_allow_html=True)
        ticker = st.text_input("Asset Ticker", value="AAPL").upper()
        date_range = st.date_input("Time Horizon", value=(datetime.now() - timedelta(days=365), datetime.now()))
        indicators = st.multiselect("Technical Signals", ["SMA 20", "SMA 50", "EMA 20"])
        fetch_btn = st.button("💎 GENERATE INSIGHTS")

    if fetch_btn:
        if len(date_range) != 2:
            st.warning("Please select a complete date range.")
        else:
            try:
                ticker_obj = yf.Ticker(ticker)
                info = ticker_obj.info
                data = ticker_obj.history(start=date_range[0], end=date_range[1])
                
                if data.empty:
                    st.error(f"Asset '{ticker}' not found in global databases.")
                else:
                    # Metrics
                    st.markdown(f"### {ticker} Core Performance")
                    m1, m2, m3, m4, m5 = st.columns(5)
                    
                    cur_price = info.get('currentPrice', data['Close'].iloc[-1])
                    prev_close = info.get('previousClose', data['Close'].iloc[-2])
                    pct_change = ((cur_price - prev_close) / prev_close) * 100
                    
                    m1.metric("Current Price", f"${cur_price:,.2f}", f"{pct_change:+.2f}%")
                    m2.metric("Market Capital", f"${info.get('marketCap', 0)/1e9:.1f}B")
                    m3.metric("52-Week High", f"${info.get('fiftyTwoWeekHigh', 0):,.2f}")
                    m4.metric("52-Week Low", f"${info.get('fiftyTwoWeekLow', 0):,.2f}")
                    m5.metric("Avg Volume", f"{info.get('averageVolume', 0)/1e6:.1f}M")

                    # Actions Bar
                    col_dl1, col_dl2, col_dl3 = st.columns([0.2, 0.2, 0.6])
                    csv_data = data.to_csv().encode('utf-8')
                    col_dl1.download_button("📥 EXPORT CSV", data=csv_data, file_name=f"dhando_{ticker}.csv", mime="text/csv")
                    
                    # Technical Charting
                    fig = make_subplots(
                        rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.04, 
                        subplot_titles=(f'{ticker} Tactical View', 'Trading Volume', 'RSI Index'),
                        row_heights=[0.5, 0.2, 0.3]
                    )

                    fig.add_trace(go.Candlestick(
                        x=data.index, open=data['Open'], high=data['High'], 
                        low=data['Low'], close=data['Close'], name='OHLC',
                        increasing_line_color='#d4af37', decreasing_line_color='#4a0e0e'
                    ), row=1, col=1)

                    if "SMA 20" in indicators:
                        fig.add_trace(go.Scatter(x=data.index, y=data['Close'].rolling(20).mean(), name='SMA 20', line=dict(color='#ffd700')), row=1, col=1)
                    if "SMA 50" in indicators:
                        fig.add_trace(go.Scatter(x=data.index, y=data['Close'].rolling(50).mean(), name='SMA 50', line=dict(color='#c0c0c0')), row=1, col=1)
                    if "EMA 20" in indicators:
                        fig.add_trace(go.Scatter(x=data.index, y=data['Close'].ewm(span=20).mean(), name='EMA 20', line=dict(color='#cd7f32')), row=1, col=1)

                    fig.add_trace(go.Bar(x=data.index, y=data['Volume'], name='Volume', marker_color='#4a0e0e'), row=2, col=1)
                    
                    rsi = calculate_rsi(data['Close'])
                    fig.add_trace(go.Scatter(x=data.index, y=rsi, name='RSI', line=dict(color='#d4af37')), row=3, col=1)
                    fig.add_hline(y=70, line_dash="dash", line_color="#800000", row=3, col=1)
                    fig.add_hline(y=30, line_dash="dash", line_color="#d4af37", row=3, col=1)

                    fig.update_layout(template=plotly_theme, xaxis_rangeslider_visible=False, height=900,
                                    paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                                    hovermode='x unified')
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Image Download
                    try:
                        img_bytes = pio.to_image(fig, format="png")
                        col_dl2.download_button("🖼️ EXPORT PNG", data=img_bytes, file_name=f"dhando_{ticker}.png", mime="image/png")
                    except: pass

                    # Intelligence Records (Expander Fix)
                    st.markdown("### Data & Intelligence")
                    with st.expander("📁 Asset Raw Data Logs"):
                        st.dataframe(data, use_container_width=True)

                    # News Section
                    st.markdown("### 📰 Latest Global Intelligence")
                    news = ticker_obj.news
                    if news:
                        for n in news[:5]:
                            with st.container():
                                st.markdown(f"#### [{n['title']}]({n['link']})")
                                st.caption(f"Source: {n['publisher']} | Published: {datetime.fromtimestamp(n['providerPublishTime']).strftime('%Y-%m-%d %H:%M')}")
                                st.markdown("---")
                    else:
                        st.info("No recent news cycles detected for this asset.")

            except Exception as e:
                st.error(f"Intelligence Failure: {str(e)}")

# Comparison Page
elif page == "Market Benchmarking":
    st.markdown("### Comparative Performance Intelligence")
    with st.sidebar:
        t_input = st.text_input("Comparison Tickers", value="AAPL, TSLA, NVDA")
        c_date = st.date_input("Benchmark Window", value=(datetime.now() - timedelta(days=365), datetime.now()))
        c_btn = st.button("🏦 RUN BENCHMARK")

    if c_btn:
        tickers = [t.strip().upper() for t in t_input.split(",")]
        try:
            with st.spinner("Processing benchmark data..."):
                c_data = yf.download(tickers, start=c_date[0], end=c_date[1])['Close']
                norm = (c_data / c_data.iloc[0] - 1) * 100
                
                st.markdown("#### Cumulative Returns (%)")
                f_comp = px.line(norm, template=plotly_theme, color_discrete_sequence=px.colors.sequential.YlOrBr)
                f_comp.update_layout(height=500, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(f_comp, use_container_width=True)
                
                st.markdown("#### Portfolio Correlation Analysis")
                fig_heat = px.imshow(c_data.corr(), text_auto=True, color_continuous_scale='YlOrBr', template=plotly_theme)
                st.plotly_chart(fig_heat, use_container_width=True)
        except Exception as e:
            st.error(f"Benchmark Error: {str(e)}")

# Footer
st.markdown(f"""
<div class="footer">
    <p><b>dhando Capital Intelligence</b> • Precision Market Analysis Engine</p>
    <p>Data provided by Yahoo Finance via yfinance • Last Update: {datetime.now().strftime('%Y-%m-%d')}</p>
    <p style="font-size: 0.7rem; opacity: 0.5;">Disclaimer: dhando is a technical analysis tool. Information provided is for educational purposes only. Investing involves risk. Consult a financial advisor before making decisions.</p>
</div>
""", unsafe_allow_html=True)
