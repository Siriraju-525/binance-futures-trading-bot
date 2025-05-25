# Binance Futures Trading Bot (Python)

A Python trading bot for Binance Futures supporting Market, Limit, Stop-Limit, and TWAP orders.  
Includes both Command Line Interface (CLI) and Graphical User Interface (GUI) using Tkinter for easy interaction.

---

## Features

- Market, Limit, Stop-Limit, and TWAP order types  
- CLI and GUI modes  
- Uses Binance Futures Testnet API for safe testing  
- Logging and error handling  
- Easy to extend for advanced strategies  

---

## Installation

1. Clone the repository or download `chatbot.py` and `requirements.txt`.

2. Install required packages:  
   ```bash
   pip install -r requirements.txt
   ```

3. Tkinter is included in standard Python installations, so no extra installation needed.

---

## Usage

Run the bot with:

```bash
python chatbot.py
```

- Choose mode:  
  - Enter `1` for CLI mode  
  - Enter `2` for GUI mode  

### CLI Mode

Follow the prompts to place Market, Limit, or Stop-Limit orders.  
You will enter the symbol (e.g., BTCUSDT), side (BUY/SELL), quantity, and price/stop price if needed.

### GUI Mode

Fill in the symbol, side, and quantity, then click **Submit Market Order**.

---

## Requirements

- Python 3.7+  
- `python-binance` library  
- Binance Futures Testnet API key and secret (get at https://testnet.binancefuture.com/)  

---

## Notes

- This bot connects to the Binance Futures Testnet for safe development and testing.  
- Never expose your real API keys publicly.  
- Test thoroughly on testnet before considering live trading.

---

## Author

[Your Name]  
[GitHub Profile] (optional)  
[Portfolio/LinkedIn] (optional)  

---

## Submission

Submitted as part of the Junior Python Developer – Crypto Trading Bot role at PrimeTrade.ai.

---

Feel free to reach out if you have questions or want to contribute!
