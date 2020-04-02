# bot.py
# AvailabilityBot for Discord.
# This bot will provide availability management in order to track who is available at what time for each day.
# Bot URL: https://discordapp.com/api/oauth2/authorize?client_id=694343099714895873&permissions=8&scope=bot
import os
from discord.ext import commands
# from .schedule_manager import ScheduleManager
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') # Create .env file to hold DISCORD_TOKEN

bot = commands.Bot(command_prefix='!')
# availability = ScheduleManager()

def do_nothing():
    print(f'Doing nothing!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to Discord!'
    )

@bot.event
async def on_reaction_add(reaction, user):
    do_nothing()

@bot.event
async def on_reaction_remove(reaction, user):
    do_nothing()

@bot.command(name='squad_availability', help='Gives current availbility on clan members')
async def squad_avail(ctx):
    response = 'Filler Text!'
    await ctx.send(response)

bot.run(TOKEN)