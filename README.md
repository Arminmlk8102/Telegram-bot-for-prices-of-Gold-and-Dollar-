Gold & Dollar Price Telegram Bot

This project is a simple Telegram bot written in Python that responds with gold and dollar price information based on user messages in Persian.

Features

/start command to welcome users

/help command to explain the bot’s purpose

Responds to:

قیمت طلا (Gold price)

قیمت دلار (Dollar price)

Built using python-telegram-bot (async version)

⚠️ Note: In the current version, prices are placeholder responses and not fetched from a real API.

Requirements

Python 3.9+

Telegram Bot Token

Required libraries:

python-telegram-bot

requests

Install dependencies:

pip install python-telegram-bot requests

Configuration

Before running the bot, edit the following variables in the code:

Token = 'Your Token'
BOT_USERNAME = 'Your Bot Username'


Replace them with your actual Telegram bot token and bot username.

How It Works

The bot listens for text messages.

If the message contains:

قیمت طلا → responds with a gold-related message

قیمت دلار → responds with a dollar-related message

If the input is not recognized, the bot asks the user to type a valid request.

Running the Bot

Run the script using:

python telegram_bot.py


You should see:

Bot is running...


The bot will start polling and respond to messages on Telegram.

Project Structure
telegram_bot.py
README.md

Future Improvements

Connect to real APIs for live gold and dollar prices

Add gold purity (عیار) selection

Improve message parsing

Add inline keyboards

Error handling and logging

Language

User interaction messages: Persian

Code and documentation: English
