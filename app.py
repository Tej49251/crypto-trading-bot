# app.py
# Main entry point for the Flask application.
# To run: python app.py

import logging
from flask import Flask, request, jsonify
from flask_cors import CORS

# Import configurations and the bot class from our new files
from config import API_KEY, API_SECRET, SERVER_HOST, SERVER_PORT
from bot import BasicBot

# --- Logging Setup ---
logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logging.getLogger().addHandler(console_handler)

# --- Flask App Initialization ---
app = Flask(__name__)
CORS(app) 

# --- Bot Initialization ---
if not API_KEY or not API_SECRET:
    logging.warning("API keys not found. Make sure you have a .env file with BINANCE_API_KEY and BINANCE_API_SECRET.")
    bot = None
else:
    try:
        bot = BasicBot(api_key=API_KEY, api_secret=API_SECRET, testnet=True)
    except Exception as e:
        logging.critical(f"Bot failed to initialize. Exiting. Error: {e}")
        bot = None

# --- API Endpoints ---
@app.route('/')
def index():
    return "Trading Bot Backend is running."

@app.route('/place_order', methods=['POST'])
def place_order_endpoint():
    if not bot:
        error_msg = "Bot is not initialized. Check API keys or logs for errors."
        logging.error(error_msg)
        return jsonify({'error': True, 'message': error_msg}), 500

    data = request.get_json()
    logging.info(f"Received order request: {data}")
    
    # Extract parameters from request
    params = {
        'symbol': data.get('symbol'),
        'side': data.get('side'),
        'order_type': data.get('type'),
        'quantity': data.get('quantity'),
        'price': data.get('price'),
        'stop_price': data.get('stopPrice')
    }

    if not all([params['symbol'], params['side'], params['order_type'], params['quantity']]):
        return jsonify({'error': True, 'message': 'Missing required parameters.'}), 400
    
    result = bot.place_order(**params)

    if result.get('error'):
        return jsonify(result), 400
    else:
        return jsonify(result), 200

# --- Main Execution ---
if __name__ == '__main__':
    if bot:
        app.run(host=SERVER_HOST, port=SERVER_PORT, debug=False)
    else:
        logging.error("Could not start Flask server because bot failed to initialize.")
