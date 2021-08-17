import discord
from discord.ext import commands
from datetime import datetime
from pycoingecko import CoinGeckoAPI
from utils.slp_helpers import *

class AXS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['axsr'], 
        name="axsrate",
        description="Displays the AXS Rate for the specified currency",
        usage="slp axsrate <currency>"
    )
    async def axsrate(self, ctx, currency):
        await ctx.message.channel.trigger_typing()

        cg = CoinGeckoAPI()
        price = float(get_axsprice(currency)['axie-infinity'][currency])
        symbol = cg.get_exchange_rates()['rates'][currency]['unit']

        embed = discord.Embed(
            description=f"The current AXS rate for currency {currency.upper()}.",
            color=0x1ABC9C,
            timestamp=datetime.utcnow()
        )
        embed.set_author(
            name="Axie Infinity Rates",
            icon_url="https://cdn.discordapp.com/attachments/788393250377564174/877202573965295616/6783.png"
        )
        embed.add_field(
            name=f"Current AXS to {currency.upper()} rate",
            value=f"{symbol}{price}"
        )
        embed.set_footer(
            text="Rate as of"
        )

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(AXS(bot))