from binance.client import Client
from binance.exceptions import BinanceAPIException
import logging
import tkinter as tk
from tkinter import messagebox
import getpass
import time
import threading

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        base_url = "https://testnet.binancefuture.com" if testnet else "https://fapi.binance.com"
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = base_url
        logging.basicConfig(level=logging.INFO)

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            logging.info("Market order placed: %s", order)
            return order
        except Exception as e:
            logging.error("Failed to place market order: %s", str(e))
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=price
            )
            logging.info("Limit order placed: %s", order)
            return order
        except Exception as e:
            logging.error("Failed to place limit order: %s", str(e))
            return None

    def place_stop_limit_order(self, symbol, side, quantity, stop_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='STOP_MARKET',
                stopPrice=stop_price,
                quantity=quantity,
                timeInForce='GTC'
            )
            logging.info(f"Stop-Limit order placed: {order}")
            return order
        except BinanceAPIException as e:
            logging.error(f"Failed to place stop-limit order: {e}")
            return None

    def place_twap_order(self, symbol, side, total_qty, intervals, delay_sec):
        qty_per_order = total_qty / intervals
        for i in range(intervals):
            self.place_market_order(symbol, side, qty_per_order)
            time.sleep(delay_sec)

    def log_order_status(self, order):
        if order:
            print("Order status:")
            print(order)
        else:
            print("No order to show.")

# --- CLI Mode ---
def cli_mode():
    print("--- Binance Futures Testnet Trading Bot ---")
    api_key = input("Enter your Binance API Key: ")
    api_secret = getpass.getpass("Enter your Binance API Secret: ")

    bot = BasicBot(api_key, api_secret)

    while True:
        print("\nChoose order type:")
        print("1. Market Order")
        print("2. Limit Order")
        print("3. Stop-Limit Order")
        print("4. TWAP Order")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            symbol = input("Enter symbol (e.g., BTCUSDT): ")
            side = input("Enter side (BUY/SELL): ")
            quantity = float(input("Enter quantity: "))
            order = bot.place_market_order(symbol, side.upper(), quantity)
            bot.log_order_status(order)

        elif choice == "2":
            symbol = input("Enter symbol (e.g., BTCUSDT): ")
            side = input("Enter side (BUY/SELL): ")
            quantity = float(input("Enter quantity: "))
            price = float(input("Enter price: "))
            order = bot.place_limit_order(symbol, side.upper(), quantity, price)
            bot.log_order_status(order)

        elif choice == "3":
            symbol = input("Enter symbol (e.g., BTCUSDT): ")
            side = input("Enter side (BUY/SELL): ")
            quantity = float(input("Enter quantity: "))
            stop_price = float(input("Enter stop price: "))
            order = bot.place_stop_limit_order(symbol, side.upper(), quantity, stop_price)
            bot.log_order_status(order)

        elif choice == "4":
            symbol = input("Enter symbol (e.g., BTCUSDT): ")
            side = input("Enter side (BUY/SELL): ")
            total_qty = float(input("Enter total quantity: "))
            intervals = int(input("Enter number of intervals: "))
            delay_sec = int(input("Enter delay in seconds: "))
            bot.place_twap_order(symbol, side.upper(), total_qty, intervals, delay_sec)

        elif choice == "5":
            print("Exiting bot.")
            break
        else:
            print("Invalid choice. Try again.")

# --- GUI Mode ---
def gui_mode():
    def submit_order():
        symbol = symbol_entry.get().upper()
        side = side_var.get().upper()
        qty = float(qty_entry.get())

        try:
            order = bot.place_market_order(symbol, side, qty)
            messagebox.showinfo("Order Placed", str(order))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    api_key = input("Enter your Binance API Key for GUI: ")
    api_secret = getpass.getpass("Enter your Binance API Secret: ")
    global bot
    bot = BasicBot(api_key, api_secret)

    root = tk.Tk()
    root.title("Binance Futures Bot")

    tk.Label(root, text="Symbol").grid(row=0, column=0)
    symbol_entry = tk.Entry(root)
    symbol_entry.grid(row=0, column=1)

    tk.Label(root, text="Side").grid(row=1, column=0)
    side_var = tk.StringVar(root)
    side_var.set("BUY")
    tk.OptionMenu(root, side_var, "BUY", "SELL").grid(row=1, column=1)

    tk.Label(root, text="Quantity").grid(row=2, column=0)
    qty_entry = tk.Entry(root)
    qty_entry.grid(row=2, column=1)

    tk.Button(root, text="Submit Market Order", command=lambda: threading.Thread(target=submit_order).start()).grid(row=3, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    mode = input("Choose mode: 1. CLI  2. GUI (Enter 1 or 2): ")
    if mode == "1":
        cli_mode()
    elif mode == "2":
        gui_mode()
    else:
        print("Invalid input. Exiting.")
