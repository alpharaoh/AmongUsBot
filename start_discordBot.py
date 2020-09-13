### Summary

# This module initalises the discord commands and waits for
# the send command module to send instructions

# -------------------------------------------------

import os
os.system("cls")
print("[*] Loading...")

from http.server import HTTPServer, BaseHTTPRequestHandler

import discord #python3 -m pip install -U discord.py[voice]
from discord.ext import commands
from discord.ext.commands import check
from discord import voice_client
from discord import Role
from discord import Guild
from discord import VoiceClient
from modules.config import *

bot = commands.Bot(command_prefix = ".")

# class handleRequest(BaseHTTPRequestHandler):
#     def _set_response(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/html')
#         self.end_headers()

#     def do_GET(self):
#         if str(self.path) == "/mute":
#             print("[*] Muting")
#             #Do stuff

#         self._set_response()

@bot.event
async def on_ready(server_class=HTTPServer, handler_class=handleRequest):
    print("[*] Bot is ready!\n\n[*] Why not join our discord if you have any issues, ideas, \nor for early access to new updates and features!\nhttps://discord.gg/PVfewrM")
    
    # server_address = ('', 8000)
    # httpd = server_class(server_address, handler_class)

    # print("\n[*] Listening for requests...")

    # try:
    #     httpd.serve_forever()
    # except KeyboardInterrupt:
    #     pass

    # httpd.server_close()
    # print("\n[*] Stopping...")

global ghostmode
ghostmode = False

global dead_members
dead_members = []

global in_channel
in_channel = [] #whoever is in the channel

@bot.command()
async def members(ctx):
    global in_channel

    if len(in_channel) == 0:
        await ctx.send("[*] There is no members that have joined this channel")
        await ctx.send("[*] every member should use .join CHANNELNAME")
    else:
        all_members = "[*] List of people that have joined, if your name is missing type .join CHANNELNAME:\n"
        for member in in_channel:
            all_members = all_members + f" - {member}\n"

        await ctx.send(all_members)
            
@bot.command()
async def join(ctx, arg):
    try:
        global channel_connected
        global in_channel

        if ctx.author.name in in_channel:
            await ctx.send("[*] You are already in this channel")
        elif arg == channel_connected:
            await ctx.send(f'[*] Added "{ctx.author.name}" to {channel_connected}')
            in_channel.append(ctx.author.name)
        else: 
            await ctx.send(f'[*] There is no channel named: {arg}')

    except Exception as e:
        print(e)
        await ctx.send("[*] You have no connected to any channels")

@bot.command()
async def mute(ctx):
    try:
        global in_channel
        global ghostmode

        for member in list(bot.get_all_members()):
            if member.voice == None:
                continue
            elif member.name not in in_channel:
                continue
            elif member.name in in_channel and member.name in dead_members and ghostmode:
                continue
            else:
                print(f"[*] Muting: {member}")
                await member.edit(mute = True)

    except Exception as e:
        print(e)
        await ctx.send("[*] You have no connected to any channels")

@bot.command()
async def unmute(ctx):
    global in_channel
    global dead_members
    global ghostmode

    for member in list(bot.get_all_members()):
        if member.name in in_channel and member.name in dead_members and ghostmode:
            member.edit(mute = True)
            continue
        if member.voice == None:
            continue
        elif member.name in dead_members:
            continue
        elif member.name in in_channel:
            print(f"[*] Unmuting: {member}")
            await member.edit(mute = False)
        else: pass

@bot.command()
async def unmute_and_clear(ctx):
    global in_channel
    global dead_members
    dead_members = []

    for member in list(bot.get_all_members()):
        if member.voice == None:
            continue
        elif member.name not in in_channel:
            continue
        else:
            print(f"[*] Unmuting: {member}")
            await member.edit(mute = False)

@bot.command()
async def ping(ctx):
    await ctx.send("[*] Pong")

@bot.command()
async def disconnect(ctx):
    global in_channel

    try:
        if ctx.author.name in in_channel:
            print("[*] You have been removed!")
            in_channel.remove(ctx.author.name)
              
    except Exception as e:
        print(f"[*] ERROR: {e}")
        await ctx.send(f"[*] Something went wrong, check the logs in command prompt")

@bot.command()
async def dead(ctx):
    global in_channel
    global dead_members

    if ctx.author.name in in_channel and ctx.author.name not in dead_members:
        dead_members.append(ctx.author.name)

@bot.command()
async def channel(ctx, arg):
    global connected
    connected = False

    for channel in range(len(list(bot.get_all_channels()))):
        if arg == str(list(bot.get_all_channels())[channel]):
            await ctx.send(f"[*] Bot successfully connected to: {arg}")

            global channel_connected
            channel_connected = arg
            connected = True

            #Use only this channel to mute
    else:
        if channel + 1 == len(list(bot.get_all_channels())) and connected == False:
            await ctx.send(f"[*] No channel found named: {arg}")

@bot.command()
async def ghostmode(ctx):
    await ctx.send(f"[*] Ghost mode activated")
    global ghostmode
    ghostmode = True

@bot.command()
async def commands(ctx):
    help_message = """```
# Commands:

.ping                       | To see if the bot is alive!

.channel CHANNEL_NAME       | Connect bot to this channel 

.join CHANNEL_NAME          | Each member must connect to the channel using this

.disconnect                 | Disconnect from your channel

.dead                       | Do this if you are dead, so you stay muted until you win or lose!

.members                    | List all the members in the channel

NOTE: If you don't want everyone to be muted in discussion but during rounds you do want people to be muted just make sure no one types .dead!

# Python bot commands (you can also use this manually if you dont want to set up the python program!)
    
.mute                       | Mutes everyone that is currently not dead

.unmute                     | Unmutes everyone that is currently not dead

.unmute_and_clear           | Unmutes everyone including the dead (This is used when you win or lose!)

.ghostmode                  | NOTE WORKING - Mute mics AND headphones for everyone between rounds except the dead (so they can talk with each other)

```"""
    await ctx.send(help_message)

try:
    bot.run(discord_bot_token)
except Exception as e:
    print(f"{e}\n\nYou have an invalid bot token in config.py")
