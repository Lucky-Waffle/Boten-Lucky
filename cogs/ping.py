from discord.ext import commands

class Ping(commands.Cog):
    """Receives ping commands"""

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Checks for a response from the bot"""
        await ctx.send("Pong")

def setup(client):
    client.add_cog(Ping(client))