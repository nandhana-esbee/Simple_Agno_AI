import yfinance as yf

def stock_tool(symbol: str):
    stock = yf.Ticker(symbol)
    return stock.info.get("currentPrice", "No data")