# Basic Discord Bot

## Commands
Commands for the bot use the prefix `;` and are as follows:
1. **`;cat`** - Get a random picture of a cat via third party API
2. **`;dadjoke`** - Get a "dad joke" via third party API
3. **`;help`** - Show this very list of commands
4. **`;meme`** - Get a random meme via third party API
5. **`;quote`** - Get a random quote via third party API

## Set up:
1. Create a new application on the Discord Developer Portal
2. Generate a bot token, and store this in a file named `.env` as follows:
```
#.env
SECRET_TOKEN= <your bot token>
```
3. Setup bot permissions to read and send messages
4. Run paulls-bot.py