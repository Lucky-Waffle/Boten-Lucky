import discord
import re
import csv
import os
import random
from discord.ext import commands


def open_csv(nameOfList, appendList):
    for filename in os.listdir('./csv'):
        if filename.endswith('.csv'):
            with open(nameOfList + ".csv") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    appendList.append(row[0]) #(command_prefix + row[0])

#Svar tilbake-------------------------
msg_encouragements = []
open_csv("msg_encouragements", msg_encouragements)

msg_hello = []
open_csv("msg_hello", msg_hello)

msg_goodbye = []
open_csv("msg_goodbye", msg_goodbye)

msg_officejoke = []
open_csv("msg_officejoke", msg_officejoke)

msg_thanks = []
open_csv("msg_thanks", msg_thanks)

#Trigger ord--------------------------
words_sad = []
open_csv("words_sad", words_sad)

words_hello = []
open_csv("words_hello", words_hello)

words_goodbye = []
open_csv("words_goodbye", words_goodbye)

words_bad = []
open_csv("words_bad", words_bad)

words_thanks = []
open_csv("words_thanks", words_thanks)


class Response_Auto_Msg(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.client.user:
            return

        msg = message.content.lower()
        user = str(message.author.name)

        if any(word in msg for word in words_hello):
            await message.channel.send(random.choice(msg_hello)) # + " " + user
        
        if any(word in msg for word in words_sad):
            await message.channel.send(random.choice(msg_encouragements))
        
        if any(word in msg for word in words_goodbye):
            await message.channel.send(random.choice(msg_goodbye) + " " + user)

        if any(word in msg for word in words_thanks):
            await message.channel.send(random.choice(msg_thanks))

        if any(word in msg for word in words_bad):
            await message.delete()
            await message.channel.send(f"{message.author.mention} Don't use that word! Your message have been reported")
            self.client.dispatch('profanity', message, msg)
            return #Slik at den ikke prøver å slette meldingen igjen.

        if message.channel.id == 801100859789541376: #Legger til emoji i meme
            if len(message.attachments) > 0:
                for file in message.attachments:
                    await message.add_reaction("😆")

        if message.channel.id == 835232028533194752: #Legger til emoji i clips-and-highlight
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',msg)
            if len(message.attachments) > 0:
                for file in message.attachments:
                    await message.add_reaction("⭐")
            if msg in urls:
                await message.add_reaction("⭐")

        if message.channel.id == 877465817871163442: #Legger til emoji i rate-my-setup
            if len(message.attachments) > 0:
                for file in message.attachments:
                    await message.add_reaction("👍")
                    await message.add_reaction("👎")

    @commands.command()
    async def office(self, ctx):
        await ctx.send(random.choice(msg_officejoke))

    @commands.Cog.listener()
    async def on_profanity(self, message, word):
        channel = self.client.get_channel(883276017819590656) #bad_words_log (channel)
        embed = discord.Embed(title="Profanity Alert!", description=f"{message.author.mention} just said ||{word}||", color=discord.Color.blurple()) #discord.Color.from_rgb(87, 242, 135)
        await channel.send(embed=embed)


def setup(client):
    client.add_cog(Response_Auto_Msg(client))