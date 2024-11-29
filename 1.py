import ccxt
import pandas as pd

def fetch_binance_spot_prices():
    binance_spot = ccxt.binance({
        'enableRateLimit': True, 
    })

    try:
        tickers = binance_spot.fetch_tickers()
        spot_prices = {symbol: ticker['last'] for symbol, ticker in tickers.items()}
        return spot_prices
    except Exception as e:
        print(f"현물 가격 가져오기 오류: {e}")
        return {}

def fetch_binance_futures_prices():
    binance_futures = ccxt.binance({
        'enableRateLimit': True,
        'options': {
            'defaultType': 'future', 
        },
    })

    try:
        tickers = binance_futures.fetch_tickers()
        futures_prices = [{'symbol': symbol.split(':')[0], 'last_future_price': ticker['last']} for symbol, ticker in tickers.items()]
        return futures_prices
    except Exception as e:
        print(f"선물 가격 가져오기 오류: {e}")
        return []

def main():
    spot_prices = fetch_binance_spot_prices()
    futures_prices = fetch_binance_futures_prices()

    df = pd.DataFrame(futures_prices)
    df['last_spot_price'] = df['symbol'].map(spot_prices)
    df.dropna(subset=['last_spot_price'], inplace= True)
    df['price_ratio'] = df['last_spot_price'] / df['last_future_price']
    df.sort_values(by='price_ratio', ascending=False, inplace=True)
    df.to_csv('binance_prices.csv', index=False)

if __name__ == "__main__":
    main()