import os
import discord
from dotenv.main import load_dotenv
from discord.ext import commands


def main():
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

    for folder in os.listdir("modules"):
        if os.path.exists(os.path.join("modules", folder, "cog.py")):
            client.load_extension(f"modules.{folder}.cog")

    client.run(os.getenv("DISCORD_TOKEN"))


if __name__ == "__main__":
    main()