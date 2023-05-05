import requests

url ="https://api.upbit.com/v1/market/all"
response = requests.get(url)
data = response.json()

tickers = []

for coin in data:
    ticker = coin['market']
    if (ticker.startswith("KRW")):
        tickers.append(ticker)

print(tickers)