import argparse
from dotenv import load_dotenv

from bot.client import TradingBot
from bot.logging_config import setup_logging

load_dotenv()
setup_logging()

def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading pair symbol"
    )

    parser.add_argument(
        "--side",
        required=True,
        choices=["BUY", "SELL"],
        help="Order side"
    )

    parser.add_argument(
        "--type",
        required=True,
        choices=["MARKET", "LIMIT"],
        help="Order type"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Required only for LIMIT orders"
    )

    args = parser.parse_args()

    if args.type == "LIMIT" and not args.price:
        print("Error: LIMIT orders require --price")
        return

    bot = TradingBot()

    bot.place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

if __name__ == "__main__":
    main()