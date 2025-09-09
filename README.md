AI-Powered Crypto Trading Bot
An intelligent, automated cryptocurrency trading bot that interacts with the Binance Futures Testnet. This application features a secure Python backend, a dynamic web UI, an AI-powered trade analysis engine using the Gemini API, and a fully automated trading strategy based on the Moving Average Crossover.

This project demonstrates a comprehensive approach to building a modern trading system, from secure API interaction and modular architecture to the integration of machine learning and real-time data visualization.

✨ Key Features
Secure & Modular Backend: Python backend using Flask, with logic separated into distinct modules for the bot, configuration, and API clients.

Dynamic Web Interface: An intuitive and responsive UI built with HTML, Tailwind CSS, and vanilla JavaScript.

Multiple Order Types: Supports manual placement of Market, Limit, and Stop-Limit orders.

Automated Trading Engine: Implements a Moving Average (MA) Crossover strategy that can run autonomously in a background thread.

AI Trade Analysis: Integrates the Google Gemini API to provide AI-powered analysis of potential trades directly in the UI.

Real-Time Data: Displays a live price ticker, account balance, and open positions, updating automatically.

Secure API Key Handling: API keys for Binance and Gemini are managed securely using environment variables (.env file).

Comprehensive Logging: Logs all backend activities, API calls, and strategy decisions to both the console and a trading_bot.log file.

📸 Screenshot
Here's a look at the main user interface, showing the manual trade panel, live data, and the AI analysis section.

(How to add your screenshot: Take a screenshot of your running application, upload it to your GitHub repository, and then replace the placeholder URL below with the direct link to your image.)

<img width="2879" height="1295" alt="Screenshot 2025-09-09 105042" src="https://github.com/user-attachments/assets/47e80c78-77c8-4a6e-a09c-cc6b1006beb9" />


📂 Project Structure
The project is organized into a modular structure for better maintainability and scalability.

trading_bot_project/
├── .env                  # Stores secret API keys (must be created manually)
├── .gitignore            # Specifies files for Git to ignore
├── app.py                # Main Flask application and API endpoints
├── bot.py                # Core trading bot logic and strategy engine
├── config.ini            # Configuration for URLs, strategy, etc.
├── config.py             # Loads all configuration from .env and .ini files
├── gemini_client.py      # Handles all interaction with the Gemini API
├── requirements.txt      # Lists all Python dependencies for the project
├── trading_bot_ui.html   # The frontend web interface
├── trading_theme.css     # Custom CSS stylesheet for the UI
└── README.md             # This file

🛠️ Setup and Installation
Follow these steps to get the application running on your local machine.

1. Prerequisites
Python 3.7+

A Binance Testnet account with API credentials.


2. Clone the Repository
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

3. Create the Environment File
Create a file named .env in the root of the project directory and add your secret API keys.

# Binance Testnet API Credentials
BINANCE_API_KEY=YOUR_TESTNET_API_KEY_HERE
BINANCE_API_SECRET=YOUR_TESTNET_API_SECRET_HERE


4. Install Dependencies
Install all the required Python libraries using the requirements.txt file. It's highly recommended to do this within a virtual environment.

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

🚀 How to Run the Application
Step 1: Start the Backend Server
Open your terminal, ensure your virtual environment is activated, and run the main application file:

python app.py

The server will start on http://127.0.0.1:5000/. Keep this terminal window open.

Step 2: Open the Frontend Interface
Navigate to the project directory in your file explorer and open the trading_bot_ui.html file in your web browser.

You can now use the interface to place manual trades, get AI analysis, or start and stop the automated trading strategy.

💻 Technologies Used
Backend: Python, Flask, python-binance

Frontend: HTML, Tailwind CSS, JavaScript

Security: python-dotenv for environment variable management

Code Quality: Modular architecture, comprehensive logging
