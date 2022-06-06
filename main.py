import os
import discord
from dotenv.main import load_dotenv
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True
intents.reactions = True
client = commands.Bot(command_prefix="-", intents=intents)

load_dotenv()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the battle of Schrute Farms"))
    #await client.change_presence(activity=discord.Streaming(name="Rocket League", url="https://www.twitch.tv/lucky4waffle"))
    print (f"{client.user.name} has connected to Discord")

initial_extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])

if __name__ == "__main__":
    for extension in initial_extensions:
        client.load_extension(extension)

client.run(os.getenv("DISCORD_TOKEN"))