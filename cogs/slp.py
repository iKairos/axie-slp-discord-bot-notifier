import discord, random
from discord.ext import commands
from datetime import datetime
from pycoingecko import CoinGeckoAPI
from utils.slp_helpers import *

class SLP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    @commands.command(name="rate", 
        description="Displays the SLP Rate for the specified currency.",
        usage="slp rate <currency>")
    async def rate(self, ctx, currency):
        await ctx.message.channel.trigger_typing()

        cg = CoinGeckoAPI()
        price = float(get_slpprice(currency)['smooth-love-potion'][currency]) 

        symbol = cg.get_exchange_rates()['rates'][currency]['unit']

        past = get_minutely_market_history(currency)
        past = past[len(past)-2]

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
            name=f"Current SLP to {currency.upper()} rate",
            value=f"{symbol}{price}"
        )
        embed.add_field(
            name=f"Direction",
            value="⬆" if past < price else "⬇"
        )
        embed.set_footer(
            text="Rate as of"
        )

        await ctx.send(embed=embed)
    
    @commands.command(aliases=['hm'],
        name="historyminutely", 
        description="Displays the minutely graph of SLP prices.",
        usage="slp historyminutely <currency>")
    async def historyminutely(self, ctx, currency):
        await ctx.message.channel.trigger_typing()

        graph_day_market_history(currency)

        file = discord.File("assets/images/graphs/minutely.png", filename="mnt.png")

        embed = discord.Embed(
            description="Graph of the minutely behavior of SLP today.",
            color=0x1ABC9C,
            timestamp=datetime.utcnow()
        )
        embed.set_image(url="attachment://mnt.png")
        embed.set_footer(
            text="Graph as of"
        )
        embed.set_author(
            name="SLP Minutely Behavior",
            icon_url="https://cdn.discordapp.com/attachments/545533157131288587/876658614553686016/slp.png"
        )

        await ctx.send(file=file, embed=embed)

    @commands.command(aliases=['conv'],
        name="convert",
        description="Converts the number of slp to its final price based on the given currency.",
        usage="slp convert <currency> <total_slp>")
    async def convert(self, ctx, currency, total_slp):
        await ctx.message.channel.trigger_typing()

        cg = CoinGeckoAPI()
        price = float(get_slpprice(currency)['smooth-love-potion'][currency]) 

        symbol = cg.get_exchange_rates()['rates'][currency]['unit']

        total = price * float(total_slp)

        embed = discord.Embed(
            description=f"The converted value of {total_slp} SLP to {currency.upper()}.",
            color=0x1ABC9C,
            timestamp=datetime.utcnow()
        )
        embed.set_author(
            name="Total SLP Converter",
            icon_url="https://cdn.discordapp.com/attachments/545533157131288587/876658614553686016/slp.png"
        )
        embed.add_field(
            name=f"Current SLP to {currency.upper()} rate",
            value=f"{symbol}{price}"
        )
        embed.add_field(
            name=f"Total SLP converted to {currency.upper()}",
            value=f"{symbol}{total}"
        )
        embed.set_footer(
            text="As of"
        )

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(SLP(bot))