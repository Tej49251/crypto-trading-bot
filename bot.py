# bot.py
import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException
from config import BINANCE_URL # Import URL from the new config file

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.api_key = api_key
        self.api_secret = api_secret
        try:
            self.client = Client(self.api_key, self.api_secret, testnet=testnet)
            self.client.FUTURES_URL = BINANCE_URL
            self.client.get_server_time()
            logging.info("Binance client initialized and connection successful.")
        except BinanceAPIException as e:
            logging.error(f"Failed to initialize Binance client: {e}")
            raise

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            params = {
                'symbol': symbol.upper(),
                'side': side.upper(),
                'type': order_type.upper(),
                'quantity': quantity,
            }
            order_type_upper = order_type.upper()

            if order_type_upper == 'LIMIT':
                if not price:
                    raise ValueError("Price is required for LIMIT orders.")
                params['price'] = price
                params['timeInForce'] = 'GTC'
            
            elif order_type_upper == 'STOP_LIMIT':
                if not price or not stop_price:
                    raise ValueError("Price and Stop Price are required for STOP_LIMIT orders.")
                params['price'] = price
                params['stopPrice'] = stop_price
                params['timeInForce'] = 'GTC'

            logging.info(f"Placing order with params: {params}")
            order = self.client.futures_create_order(**params)
            logging.info(f"Successfully placed order: {order}")
            return order
        
        except BinanceAPIException as e:
            logging.error(f"Binance API Error while placing order: {e}")
            if e.code == -2019: message = "Margin is insufficient. You do not have enough funds."
            elif e.code == -1111: message = "Invalid quantity. Check precision rules for the symbol."
            elif e.code == -4014: message = "Price not increased by tick size. Adjust the price value."
            elif e.code == -1121: message = "Invalid symbol. Please check the symbol and try again."
            else: message = e.message
            return {'error': True, 'code': e.code, 'message': message}

        except ValueError as e:
            logging.error(f"Validation error: {e}")
            return {'error': True, 'message': str(e)}

        except Exception as e:
            logging.error(f"An unexpected error occurred while placing order: {e}")
            return {'error': True, 'message': f"An unexpected error occurred: {str(e)}"}

    def get_current_price(self, symbol):
        """Fetches the last price for a given symbol."""
        try:
            ticker = self.client.futures_symbol_ticker(symbol=symbol.upper())
            logging.info(f"Fetched ticker for {symbol}: {ticker}")
            return {'symbol': ticker['symbol'], 'price': ticker['price']}
        except BinanceAPIException as e:
            logging.error(f"Binance API Error fetching price for {symbol}: {e}")
            return {'error': True, 'message': e.message}
        except Exception as e:
            logging.error(f"An unexpected error occurred fetching price for {symbol}: {e}")
            return {'error': True, 'message': str(e)}

