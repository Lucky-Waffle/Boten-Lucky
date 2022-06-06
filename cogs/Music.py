import discord
import os
import youtube_dl
from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


queues = {}

def check_queue(ctx, id):
    if queues[id] != []:
        voice = ctx.guild.voice_client
        source = queues[id].pop(0)
        player = voice.play(source)


class Music(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context = True)
    async def join(self, ctx):
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("You are not in a voice channel, you must be in a voice channel to run this command")

    @commands.command(pass_context = True)
    async def leave(self, ctx):
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
            await ctx.send("I left the voice channel")
        else:
            await ctx.send("I'm not in a voice channel")

    @commands.command(pass_context = True)
    async def pause(self, ctx):
        voice = discord.utils.get(self.client.voice_client, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("At the moment, there is no audio playing on the voice channel")

    @commands.command(pass_context = True)
    async def resume(self, ctx):
        voice = discord.utils.get(self.client.voice_client, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("At the moment, no song is paused")

    @commands.command(pass_context = True)
    async def stop(self, ctx):
        voice = discord.utils.get(self.client.voice_client, guild=ctx.guild)
        voice.stop()

    @commands.command(pass_context = True)
    async def play(self, ctx, url:str):
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()

            # download the youtube video
            ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors':[{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    os.rename(file, "song.mp3")

            source = FFmpegPCMAudio("song.mp3")
            player = voice.play(source)
        else:
            await ctx.send("You are not in a voice channel, you must be in a voice channel to run this command")


def setup(client):
    client.add_cog(Music(client))