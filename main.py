import discord
from discord.ext import commands
import os
import csv

import os

phrase_dict = {}
csv_path = os.path.join(os.path.dirname(__file__), 'brainrot.csv')
with open(csv_path, mode='r') as infile:
    reader = csv.reader(infile)
    next(reader)  # Skip header
    for rows in reader:
        normal_phrase = rows[0].strip().lower()
        brainrot_phrase = rows[1].strip().lower()
        phrase_dict[normal_phrase] = brainrot_phrase

# Function to replace phrases
def translate_phrase(text):
    for normal_phrase, brainrot_phrase in phrase_dict.items():
        text = text.replace(f" {normal_phrase} ", f" {brainrot_phrase} ")
    return text


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
    translated_phrase = translate_phrase(phrase)
    await interaction.response.send_message(translated_phrase)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    await tree.sync()  # Sync commands with Discord

bot.run(os.getenv('TOKEN'))