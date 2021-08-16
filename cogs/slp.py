import discord, random
from discord.ext import commands
from pycoingecko import CoinGeckoAPI
from datetime import datetime

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

        symbol = cg.get_exchange_rates()['rates'][currency]['unit']

        embed = discord.Embed(
            description=f"The current SLP rate for currency {currency.upper()}.",
            color=0x1ABC9C,
            timestamp=datetime.utcnow()
        )
        embed.set_author(
            name="Smooth Love Potion Rates",
            icon_url="https://cdn.discordapp.com/attachments/545533157131288587/876658614553686016/slp.png"
        )
        embed.add_field(
            name=f"SLP Rate to {currency}",
            value=f"{symbol}{price}"
        )
        embed.set_footer(
            text="SLP Rate as of"
        )

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(SLP(bot))