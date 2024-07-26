# Discord Bot
This repository contains a simple Discord bot written in Python. The bot includes functionalities such as tracking messages and member joins, responding to commands, and managing nicknames.

## Features
- Message Tracking: Tracks the number of messages sent.
- Member Join Tracking: Tracks the number of new members joining the server.
- Nickname Management: Automatically reverts nicknames containing certain keywords.

## Commands:
- !hello: Greets the user.
- !users: Displays the number of members in the server.
- !help: Provides information about available commands.
- Bad Word Filtering: Deletes messages containing specified bad words.

## Technologies Used
- Python: Programming language used to write the bot.
- discord.py: Python library for interacting with the Discord API.

## Installation
1. Clone the repository to your local machine:
```sh

git clone https://github.com/yourusername/discord-bot.git
```

2. Navigate to the project directory:

```sh
cd discord-bot
```

3. Create and activate a virtual environment:

```sh
python3 -m venv venv
source venv/bin/activate
```

4. Install the required packages:
```sh
pip install -r requirements.txt
```

5. Create a token.txt file in the project directory and add your Discord bot token to it:

```sh
your_discord_bot_token
```

## Usage
1. Run the bot:
```sh
python bot.py
```
The bot will start and connect to your Discord server.
