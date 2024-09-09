import discord
import requests
from dotenv import load_dotenv
import os
load_dotenv()  # Load environment variables from .env

# Set up the Discord client
intents = discord.Intents.default()
intents.message_content = True  # This is crucial to read message content

client = discord.Client(intents=intents)

'''
Helper functions for each action/command/feature
'''
# Function to fetch a dad joke
def get_dad_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        joke = response.json().get("joke")
        return joke
    else:
        return "Sorry, I couldn't fetch a joke right now."

# Function to fetch a meme
def get_meme():
    # https://github.com/D3vd/Meme_Api
    url = "https://meme-api.com/gimme"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        meme = response.json().get("url")
        return meme
    else:
        return "Sorry, I couldn't fetch a meme right now."

# Function to fetch a quote
def get_quote():
    url = "https://api.quotable.io/random"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        quote = response.json().get("content")
        author = response.json().get("author")
        return quote, author
    else:
        return "Sorry, I couldn't fetch a quote right now.", False

# Function to fetch a cat
def get_cat():
    url = "https://api.thecatapi.com/v1/images/search"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        cat = response.json()[0].get("url")
        return cat
    else:
        return "Sorry, I couldn't fetch a cat right now.", False

'''
Main loop
'''

# Event listener for when the bot is ready
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

# Event listener for handling messages
@client.event
async def on_message(message):

    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return
    

    # Check if message aligns with command/feature
    if message.content == ";help":
        commands = """**`;cat`** - Get a random picture of a cat via third party API\n**`;dadjoke`** - Get a "dad joke" via third party API\n**`;help`** - Show this very list of commands\n**`;meme`** - Get a random meme via third party API\n**`;quote`** - Get a random quote via third party API"""
        await message.channel.send(commands)
    elif message.content == ";dadjoke":
        joke = get_dad_joke()
        await message.channel.send(" > ## " + joke)
    elif message.content == ";meme":
        meme = get_meme()
        await message.channel.send(meme)
    elif message.content == ";quote":
        quote, author = get_quote()
        if author:
            await message.channel.send("> ## " + quote + "\n*" + author + "*")
        else:
            await message.channel.send(quote)
    elif message.content == ";cat":
        cat = get_cat()
        await message.channel.send(cat)
        
# Run the bot with the token
client.run(os.getenv("SECRET_TOKEN"))