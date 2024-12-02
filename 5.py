import ccxt

def fetch_btcusd_cm_ticker():
    exchange = ccxt.binancecoinm({
        'enableRateLimit': True,
    })

    symbol = 'BTC/USD'
    try:
        ticker = exchange.fetch_ticker(symbol)
        print(ticker)
    except Exception as e:
        print(f"데이터를 가져오는 중 오류 발생: {e}")

if __name__ == "__main__":
    fetch_btcusd_cm_ticker()