import discord, random
from discord.ext import commands

class SLP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    
def setup(bot):
    bot.add_cog(SLP(bot))