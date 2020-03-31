# bot.py
# AvailabilityBot for Discord.
# This bot will provide availability management in order to track who is available at what time for each day.
# Bot URL: https://discordapp.com/api/oauth2/authorize?client_id=694343099714895873&permissions=8&scope=bot
import os
import discord
from .schedule_manager import ScheduleManager
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') # Create .env file to hold DISCORD_TOKEN

client = discord.Client()
availability = ScheduleManager()

def do_nothing():
    print(f'Doing nothing!')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to Reckless!'
    )

@client.event
async def on_reaction_add(reaction, user):
    do_nothing()

@client.event
async def on_reaction_remove(reaction, user):
    do_nothing()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '!squad_availability':
        response = 'Filler Text!'
        await message.channel.send(response)

client.run(TOKEN)