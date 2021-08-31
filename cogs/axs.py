import discord
from discord.ext import commands
from datetime import datetime
from pycoingecko import CoinGeckoAPI
from utils.axs_helpers import *
from utils.embed_messages import easyembed

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

        past = get_minutely_market_history(currency)
        past = past[len(past)-2]

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
        embed.add_field(
            name=f"Direction",
            value="⬆" if past < price else "⬇"
        )
        embed.set_footer(
            text="Rate as of"
        )

        await ctx.send(embed=embed)

    @commands.command(aliases=['axshm'],
        name="axshistoryminutely",
        description="Displays the minutely graph of AXS prices.",
        usage="slp axshistoryminutely <currency>")
    async def axshistoryminutely(self, ctx, currency):
        await ctx.message.channel.trigger_typing()

        graph_day_market_history(currency)

        file = discord.File("assets/images/graphs/axs/minutely.png", filename="mnt.png")

        embed = discord.Embed(
            description="Graph of the minutely behavior of AXS today.",
            color=0x1ABC9C,
            timestamp=datetime.utcnow()
        )
        embed.set_image(url="attachment://mnt.png")
        embed.set_footer(
            text="Graph as of"
        )
        embed.set_author(
            name="AXS Minutely Behavior",
            icon_url="https://cdn.discordapp.com/attachments/545533157131288587/876658614553686016/slp.png"
        )

        await ctx.send(file=file, embed=embed)

    @axsrate.error 
    async def rate_error(self, ctx, error):
        error = getattr(error, 'original', error)
        if isinstance(error, KeyError):
            e = easyembed("Error in AXS Rate Command", 
                "error",
                "The currency you have provided does not exist. Please try another currency.", 
                "Use the help command for more information."
            )

            await ctx.send(embed=e)

            return 
        
        if isinstance(error, commands.MissingRequiredArgument):
            e = easyembed("Error in AXS Rate Command", 
                "error",
                f"You are missing the `{error.param}` argument. Please provided all the required arguments for the command to work.", 
                "Use the help command for more information."
            )

            await ctx.send(embed=e)

            return 
        
        e = easyembed("Error in AXS Rate Command", 
            "error",
            "An unhandled error has been detected. Please report this to the developers.", 
            "Use the help command for more information."
        )

        await ctx.send(embed=e)

    @axshistoryminutely.error 
    async def historyminutely_error(self, ctx, error):
        error = getattr(error, 'original', error)
        if isinstance(error, ValueError):
            e = easyembed("Error in AXS Historyminutely Command", 
                "error",
                "The currency you have provided does not exist. Please try another currency.", 
                "Use the help command for more information."
            )

            await ctx.send(embed=e)

            return 
        
        if isinstance(error, commands.MissingRequiredArgument):
            e = easyembed("Error in AXS Historyminutely Command", 
                "error",
                f"You are missing the `{error.param}` argument. Please provided all the required arguments for the command to work.", 
                "Use the help command for more information."
            )

            await ctx.send(embed=e)

            return 
        
        e = easyembed("Error in AXS Historyminutely Command", 
            "error",
            "An unhandled error has been detected. Please report this to the developers.", 
            "Use the help command for more information."
        )

        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(AXS(bot))