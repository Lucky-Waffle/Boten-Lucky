import discord
from discord.ext import commands

class Greetings(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(759151135105351770) #WelcomeChannel
        serverMember = len([m for m in channel.guild.members if not m.bot])
        embed = discord.Embed(title=f"Velkommen {member.name} ! 🥰", description=f"Vi ser frem til å bli kjent med deg! \n\r Antall medlemmer: {serverMember}", color = discord.Color.green())
        embed.set_thumbnail(url=member.avatar_url)
        await channel.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.client.get_channel(920351795161755699) #GoodbyeChannel
        serverMember = len([m for m in channel.guild.members if not m.bot])
        embed = discord.Embed(title=f"Farvel", description=f"Håper vi sees snart igjen {member.name} ! ❤️ \n\r Antall medlemmer: {serverMember}", color = discord.Color.red())
        embed.set_thumbnail(url=member.avatar_url)
        await channel.send(embed=embed)


def setup(client):
    client.add_cog(Greetings(client))