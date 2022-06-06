import discord
import json
import requests
from discord.ext import commands


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


class Response(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def inspire(self, ctx):
        quote = get_quote()
        await ctx.send (quote)

    @commands.command()
    async def members(self, ctx):
        channel = self.client.get_channel(759151135105351770) #WelcomeChannel
        serverMember = len([m for m in channel.guild.members if not m.bot])
        await ctx.send ("Antall medlemmer: " + str(serverMember))


def setup(client):
    client.add_cog(Response(client))