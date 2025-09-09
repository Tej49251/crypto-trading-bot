Simplified Crypto Trading Bot
This project is a functional prototype of a cryptocurrency trading bot that interacts with the Binance Futures Testnet. It features a secure Python backend powered by Flask and a clean, responsive web interface for manual order placement.

This application was created to demonstrate the core principles of building a trading system, including API interaction, secure key management, and the separation of backend logic from the user interface.

Features
Secure Backend: Python backend using Flask to handle trading logic securely.

Web-Based UI: An intuitive and responsive user interface built with HTML and Tailwind CSS.

Multiple Order Types: Supports placing Market, Limit, and Stop-Limit orders.

Binance Testnet Integration: All trades are placed on the Binance Futures Testnet (USDT-M), allowing for safe testing without real funds.

Secure API Key Handling: API keys are managed securely using environment variables (.env file) and are never exposed to the frontend.

Comprehensive Logging: The backend logs all API requests, responses, and errors to both the console and a trading_bot.log file.

Real-time Feedback: The UI provides immediate status updates and detailed logs for all submitted orders.

Project Structure
trading_bot_project/
├── .env                  # Stores secret API keys (must be created manually)
├── .gitignore            # Specifies files for Git to ignore
├── bot_backend.py        # The Python Flask server and trading logic
├── trading_bot_ui.html   # The frontend web interface
└── README.md             # This file

Setup and Installation
Follow these steps to get the application running on your local machine.

1. Prerequisites
Python 3.7+

A Binance Testnet account with API credentials.

2. Clone the Repository (Example)
git clone [https://github.com/your-username/trading-bot-project.git](https://github.com/your-username/trading-bot-project.git)
cd trading-bot-project

3. Create the Environment File
Create a file named .env in the root of the project directory. This is where you will store your secret API keys.

Copy the following into your .env file and replace the placeholders with your actual Binance Testnet credentials:

# Binance Testnet API Credentials
BINANCE_API_KEY=YOUR_TESTNET_API_KEY_HERE
BINANCE_API_SECRET=YOUR_TESTNET_API_SECRET_HERE

4. Install Dependencies
Install the required Python libraries using pip:

pip install Flask python-binance Flask-Cors python-dotenv

How to Run the Application
The application consists of two parts that must be running simultaneously: the backend server and the frontend interface.

Step 1: Start the Backend Server
Open your terminal, navigate to the project directory, and run the following command:

python bot_backend.py

The server will start, and you will see log messages in your terminal indicating that it is running on http://127.0.0.1:5000/. Keep this terminal window open.

Step 2: Open the Frontend Interface
Navigate to the project directory in your file explorer and open the trading_bot_ui.html file in your web browser (e.g., Chrome, Firefox).

You can now use the interface to place orders. All actions will be sent to your local backend server for processing.

<img width="2879" height="1295" alt="image" src="https://github.com/user-attachments/assets/e984afcb-e936-4f13-aec7-c0b272fe6262" />


Technologies Used
Backend: Python, Flask, python-binance

Frontend: HTML, Tailwind CSS, JavaScript

Security: python-dotenv for environment variable management
