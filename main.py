import requests
import discord
from discord.ext import commands, tasks
import threading
from server import run_server

# Start the Flask server in a separate thread
threading.Thread(target=run_server).start()

BASE_LINK = "https://clientsettings.roblox.com/v2/client-version"
WINDOWS_VERSION = requests.get(f"{BASE_LINK}/WindowsPlayer").json()["version"]
MAC_VERSION = requests.get(f"{BASE_LINK}/MacPlayer").json()["version"]

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Logged in")
    roblox_check.start()

@tasks.loop(seconds=10)
async def roblox_check():
    global WINDOWS_VERSION, MAC_VERSION, BASE_LINK
    channel = bot.get_guild(1291783058080534638).get_channel(1291785859586068606)

    windows_req = requests.get(f"{BASE_LINK}/WindowsPlayer").json()["version"]
    mac_req = requests.get(f"{BASE_LINK}/MacPlayer").json()["version"]

    if windows_req != WINDOWS_VERSION: 
        embed = discord.Embed(
            title="VoidX roblox update checker", 
            description="Roblox has updated, VoidX might be down!",
            colour=discord.Color.red(),
            timestamp=discord.utils.utcnow(),
        )
        embed.set_footer(text="Made by koashi")
        embed.add_field(name="Old Version", value=WINDOWS_VERSION, inline=True)
        embed.add_field(name="New Version", value=windows_req, inline=True)
        await channel.send(embed=embed)
        WINDOWS_VERSION = windows_req

    if mac_req != MAC_VERSION: 
        embed = discord.Embed(
            title="VoidX roblox update checker", 
            description="Roblox has updated, VoidX might be down!",
            colour=discord.Color.red(),
            timestamp=discord.utils.utcnow(),
        )
        embed.set_footer(text="Made by koashi")
        embed.add_field(name="Old Version", value=MAC_VERSION, inline=True)
        embed.add_field(name="New Version", value=mac_req, inline=True)
        await channel.send(embed=embed)
        MAC_VERSION = mac_req

@bot.command()
async def check(ctx):
    windows_req = requests.get(f"{BASE_LINK}/WindowsPlayer").json()["version"]
    mac_req = requests.get(f"{BASE_LINK}/MacPlayer").json()["version"]

    embed = discord.Embed(
        title="VoidX roblox update checker", 
        description=f"Windows: {windows_req}\nMac: {mac_req}",
        colour=discord.Color.green(),
        timestamp=discord.utils.utcnow(),
    )
    embed.set_footer(text="Made by koashi")
    await ctx.send(embed=embed)

bot.run("MTI5NjY2ODE1NDYyOTQ1NTkwNA.GcJrdH.0aiJrOYJeB3lGYozc2pOpgjgWsijWAKy4bznj8")
