import discord, random
from discord.ext import commands
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

def get_slpprice(currency): # function to retrieve specifically SLP price rate
    price = cg.get_price(ids='smooth-love-potion', vs_currencies=currency)
    return(price)

class SLP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    @commands.command(name="rate", 
        description="Displays the SLP Rate for the specified currency.",
        usage="slp rate <currency>")
    async def rate(self, ctx, currency):
        price = float(get_slpprice(currency)['smooth-love-potion'][currency]) 

        await ctx.send(f"The SLP rate for {currency} is {price}")

def setup(bot):
    bot.add_cog(SLP(bot))