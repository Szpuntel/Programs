import yfinance as yf
import streamlit as st


st.write("""
# Prosta Aplikacja Cen Akcji 

Pokazane są ceny akcji po zamknięciu, infromacje pobierane z Google.
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write("""
## Ceny 
""")
st.line_chart(tickerDf.Close)
st.write("""
## Ceny Volumenów
""")
st.line_chart(tickerDf.Volume)

#To run in u need to be in the "simple stock price" folder and
# type "streamlit run main.py" in the terminal.