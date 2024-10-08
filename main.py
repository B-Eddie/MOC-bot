import discord
from discord.ext import commands
import os
import csv
import re
from dotenv import load_dotenv

load_dotenv()

phrase_dict = {}
csv_path = os.path.join(os.path.dirname(__file__), 'brainrot.csv')
with open(csv_path, mode='r') as infile:
    reader = csv.reader(infile)
    next(reader)  # Skip header
    for rows in reader:
        normal_phrase = rows[0].strip().lower()
        brainrot_phrase = rows[1].strip().lower()
        phrase_dict[normal_phrase] = brainrot_phrase

def translate_phrase(text):
    # changed to whole words only
    pattern = re.compile(r'\b(' + '|'.join(re.escape(phrase) for phrase in phrase_dict.keys()) + r')\b', re.IGNORECASE)
    
    def replace(match):
        normal_phrase = match.group(0).lower()
        return phrase_dict.get(normal_phrase, match.group(0))
    
    return pattern.sub(replace, text)

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

bot.run(os.environ.get('TOKEN'))