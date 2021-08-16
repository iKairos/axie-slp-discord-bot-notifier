import discord, random
from discord.ext import commands

class SLP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    @commands.command(name="say", 
        description="Repeats what you say.",
        usage="temp")
    async def say(self, ctx, *, message=None):
        await ctx.send(message)
    
def setup(bot):
    bot.add_cog(SLP(bot))