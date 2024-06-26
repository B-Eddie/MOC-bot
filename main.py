import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

tree = bot.tree

@tree.command(name="info", description="Provides information about MOC bot")
async def info(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Murder Of Code bot",
        description="This is the person bot of Murder of Codes!",
        color=discord.Color.blue()
    )
    await interaction.response.send_message(embed=embed)

@tree.command(name="brainrot_translator", description="Changes normal human phrases into brainrot phrases.")
async def brainrot_translator(interaction: discord.Interaction, phrase: str):
    translated_phrase = phrase.replace("normal", "brainrot").replace("human", "brainroteeee")
    await interaction.response.send_message(translated_phrase)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    await tree.sync()  # Sync commands with Discord

bot.run(os.getenv('TOKEN'))