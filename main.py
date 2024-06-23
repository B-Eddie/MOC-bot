import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Required for handling slash command interactions
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.tree.command(  # Update here: Use bot.tree.command
    name="ping",  # Name of the command (what users will type)
    description="Checks the bot's latency"  # Short description for the command
)
async def ping(ctx):
    await ctx.respond(f"Pong! Latency is {round(bot.latency * 1000)}ms")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    await bot.tree.sync()  # Sync commands with Discord

# Retrieve the bot token from environment variable
bot_token = os.environ.get('TOKEN')
if bot_token is None:
    print("Bot token not found in environment variable.")
else:
    # Run the bot with the retrieved token
    bot.run(bot_token)
