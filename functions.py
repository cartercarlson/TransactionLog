#TODO: figure out if I need to update exchange every time, or just fetchBalance()
from database import db_session, engine
from models import Transaction
from exchange import exchange

# Function to get current coin price in $
def coin_price(coin):
	btc_price = float(exchange.fetch_ticker('BTC/USDT')['info']['lastPrice'])
	if coin == 'BTC':
		price = btc_price
	elif coin == 'DOGE':
		price = float(exchange.fetch_ticker('DOGE/USDT')['info']['lastPrice'])
	else:
		btc_ratio = float(exchange.fetch_ticker(coin + '/BTC')['info']['lastPrice'])
		price = btc_ratio * btc_price

	return price
