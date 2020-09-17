### Summary

# This module initalises the discord commands and waits for
# the send command module to send instructions

# -------------------------------------------------

print("[*] Loading bot...")

import asyncio
from aiohttp import web
import discord #python3 -m pip install -U discord.py[voice]
from discord.ext import commands
from discord.ext.commands import check
from discord import voice_client
from discord import Role
from discord import Guild
from modules.config import *
from modules import module_grabscreen

bot = commands.Bot(command_prefix = ".", help_command=None)

@bot.command()
async def help(ctx):
    help_message = """```
# Commands:

.ping                       | To see if the bot is alive!

.dead                       | Do this if you are dead, so you stay muted until you win or lose!

.kill @DiscordP1 @DiscordP2 | Alternative to .dead 

.ghostmode                  | Mute mics AND headphones for everyone between rounds except the dead (so they can talk with each other)

.users                      | See current users in the hosts voice channel

# Python bot commands (you can also use this manually if you dont want to set up the python program!)
    
.mute                       | Mutes everyone that is currently not dead

.unmute                     | Unmutes everyone that is currently not dead

.clear                      | Unmutes everyone including the dead (This is used when you win or lose!)

```"""
    await ctx.send(help_message)

global ghostmode_on
ghostmode_on = False

global dead_members
dead_members = []

global in_discussion
in_discussion = False

global leader
leader = None

@bot.event
async def on_ready():
    print("[*] Bot is ready!\n\n[*] Why not join our discord if you have any issues, ideas, \nor for early access to new updates and features!\nhttps://discord.gg/PVfewrM\n\n[*] Press Control+C to exit safely")

@bot.command()
async def host(ctx):
    global leader

    if leader == None:
        leader = ctx.author
        await ctx.send(f"```[*] Host connected: {ctx.author.name}```")
    elif leader != None and leader != ctx.author:
        await ctx.send(f"```[*] Sorry, {leader} is already a host. The host can disconnect by typing .host once more```")
    else:
        await ctx.send(f"```[*] Disconnected host: {ctx.author.name}```")
        leader = None


@bot.command()
async def users(ctx):
    global leader
    if leader == None:
        await ctx.send("[*] The host of the program must connect first using .host")
    else:
        string = "[*] Users connected: \n"

        for member in list(bot.get_channel(leader.voice.channel.id).members):
            string = string + f"- {member}\n"

        await ctx.send(f"```{string}```")


@bot.command()
async def mute(ctx):
    global leader
    global ghostmode_on

    global in_discussion
    in_discussion = False

    try:
        if ctx.author != leader: #make sure no one else can run these commands
            await ctx.send("```[*] Only the host can use this command```")
    except: pass

    try:
        for member in list(bot.get_channel(leader.voice.channel.id).members):
            if member.id in dead_members and ghostmode_on:
                await member.edit(mute = False)
            elif member.id not in dead_members and ghostmode_on:
                await member.edit(deafen = True, mute = True)
            else:
                await member.edit(mute = True)

    except AttributeError as e:
        print("[*] The host of the program must connect first using .host")


@bot.command()
async def unmute(ctx):
    global leader
    global dead_members
    global ghostmode_on

    global in_discussion
    in_discussion = True

    try:
        if ctx.author != leader: #make sure no one else can run these commands
            await ctx.send("```[*] Only the host can use this command```")
    except: pass

    try:
        for member in list(bot.get_channel(leader.voice.channel.id).members):
            if member.id in dead_members and ghostmode_on:
                await member.edit(mute = True)
            elif member.id in dead_members and ghostmode_on == False:
                await member.edit(mute = True)
            elif member.id not in dead_members and ghostmode_on:
                await member.edit(deafen = False, mute = False)
            else:
                await member.edit(mute = False)

    except AttributeError:
        print("[*] The host of the program must connect first using .host")


@bot.command()
async def clear(ctx):  #unmute and clear the dead
    global leader
    global dead_members
    dead_members = []

    try:
        if ctx.author != leader: #make sure no one else can run these commands
            await ctx.send("```[*] Only the host can use this command```")
    except: pass

    try:
        for member in list(bot.get_channel(leader.voice.channel.id).members):
                await member.edit(deafen = False, mute = False)

    except AttributeError:
        print("[*] The host of the program must connect first using .host")


@bot.command()
async def dead(ctx):
    global dead_members
    global ghostmode_on

    if ghostmode_on:
        await ctx.author.edit(mute = False, deafen = False)
    else:
        await ctx.author.edit(mute = True)

    if ctx.author.id not in dead_members:
        dead_members.append(ctx.author.id)


@bot.command()
async def kill(ctx, *members: discord.Member):
    global dead_members
    global ghostmode_on
    global leader

    for member in members:
        if member not in list(bot.get_channel(leader.voice.channel.id).members):
            await ctx.send(f"[*] User not in channel: {member}")
            continue
        try:
            if ghostmode_on and in_discussion:
                await member.edit(mute = True)
                valid = True
            if ghostmode_on and in_discussion == False:
                await member.edit(mute = False, deafen = False)
                valid = True
            else:
                await member.edit(mute = True)
                valid = True
        except Exception as e:
            print(e)
            await ctx.send(f"[*] Invalid user: {member}")
            valid = False

        if valid:
            if member.id not in dead_members:
                dead_members.append(member.id)
        print(dead_members)

@bot.command()
async def ghostmode(ctx):
    global ghostmode_on

    if ctx.author != leader: #make sure no one else can run these commands
        await ctx.send("```[*] Only the host can use this command```")
    else:
        if ghostmode_on == False:
            ghostmode_on = True
            await ctx.send("```[*] Ghost mode activated```")
        else:
            ghostmode_on = False
            await ctx.send("```[*] Ghost mode deactivated```")


@bot.command()
async def ping(ctx):
    await ctx.send("`[*] Pong`")


async def handle_request(request):
    action = request.match_info.get('action', "nothing")
    if action == "mute":
        await mute(None)
    elif action == "unmute":
        await unmute(None)
    elif action == "clear":
        await clear(None)

    return web.Response(text=None)
    

async def run_bot():
    app = web.Application()
    app.router.add_get('/', handle_request)
    app.router.add_get('/{action}', handle_request)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '', port)
    await site.start()

    try:
        await bot.start(discord_bot_token)

    except KeyboardInterrupt:
        bot.close(),

    finally:
        await runner.cleanup()

try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_bot())

except OSError:
    print("[*] ERROR: address already in use")

except Exception as e:
    print(f"{e}\n\n[*] ERROR: invalid discord bot token\n")

except KeyboardInterrupt:
    print("\n[*] Exiting..")
