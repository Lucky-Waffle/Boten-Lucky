import os
import discord
from dotenv.main import load_dotenv
from discord.ext import commands


def main():
    #intents = discord.Intents.default()
    #intents.members = True
    #intents.reactions = True
    #activity = discord.Activity(type=discord.ActivityType.watching, name="the battle of Schrute Farms")
    client = commands.Bot(command_prefix="-")
    
    load_dotenv()

    @client.event
    async def on_ready():
        print (f"{client.user.name} has connected to Discord")


    @client.command()
    async def ping(ctx):
        """Checks for a response from the bot"""
        await ctx.send("Pong")


    client.run(os.getenv("DISCORD_TOKEN"))


if __name__ == "__main__":
    main()