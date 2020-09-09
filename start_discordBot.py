### Summary

# This module initalises the discord commands and waits for
# the send command module to send instructions

# -------------------------------------------------

import os
os.system("cls")
print("[*] Loading...")

import discord #python3 -m pip install -U discord.py[voice]
from discord.ext import commands
from discord.ext.commands import check
from discord import voice_client
from discord import Role
from discord import Guild
from modules.config import *

bot = commands.Bot(command_prefix = ".")

@bot.event
async def on_ready():
    print("[*] Bot is ready!\n[*] Please run start.py")

@bot.command()
async def mute(ctx):
    for member in list(bot.get_all_members()):
        if member.voice == None:
            pass
        else:
            print(f"Muting: {member}")
            await member.edit(mute = True)

@bot.command()
async def unmute(ctx):
    for member in list(bot.get_all_members()):
        if member.voice == None:
            pass
        else:
            print(f"Unmuting: {member}")
            await member.edit(mute = False)

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

bot.run(discord_bot_token)
