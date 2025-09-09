# config.py
import os
import sys
import configparser
from dotenv import load_dotenv

# --- Secure Configuration ---
load_dotenv()
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# --- Load Application Settings from config.ini ---
config = configparser.ConfigParser()
files_read = config.read('config.ini')
if not files_read:
    print("FATAL ERROR: Configuration file 'config.ini' not found or is empty.", file=sys.stderr)
    sys.exit("Critical: config.ini not found.")

# --- Exported Configuration Variables ---
BINANCE_URL = config.get('binance', 'testnet_fapi_url')
SERVER_HOST = config.get('server', 'host')
SERVER_PORT = config.getint('server', 'port')
