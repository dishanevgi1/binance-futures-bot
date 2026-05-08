import os
import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException

logger = logging.getLogger(__name__)

class TradingBot:
    def __init__(self):
        self.client = Client(
            os.getenv("API_KEY"),
            os.getenv("API_SECRET"),
            testnet=True
        )

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                "symbol": symbol.upper(),
                "side": side.upper(),
                "type": order_type.upper(),
                "quantity": quantity,
            }

            if order_type.upper() == "LIMIT":
                params.update({
                    "price": str(price),
                    "timeInForce": "GTC"
                })

            logger.info(
                f"Sending {order_type} {side} order for {symbol}"
            )

            response = self.client.futures_create_order(**params)

            logger.info(f"API Response: {response}")

            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.message}")
            return None

        except Exception as e:
            logger.error(f"Unexpected Error: {str(e)}")
            return None