from secrets import choice
from discord.ext import commands
import random

class Random(commands.Cog):
    """Receives random results"""

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def roll(self, ctx: commands.Context, dice: str):
        """Rolls a given amount of dice in the form _d_
        Example: -roll 2d20
        """
        try:
            rolls = ""
            total = 0
            amount, die = dice.split("d")
            for _ in range (int(amount)):
                roll = random.randint(1, int(die))
                total += roll
                rolls += f"{roll} "
            await ctx.send(f"Rolls: {rolls}\nSum: {total}")
        except ValueError:
            await ctx.send("Dice must be in the format _d_ (example: 2d6)")

    @commands.command()
    async def choose(self, ctx: commands.Context, *args):
        """Chooses a random item from a list
        Example: -choose "First Option" "Second Option" "Third Option"
        """
        choice = random.choice(args)
        await ctx.send(choice)

def setup(client):
    client.add_cog(Random(client))