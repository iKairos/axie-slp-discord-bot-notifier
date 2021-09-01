import discord
from discord import embeds
from discord.ext import commands
from datetime import datetime
from pycoingecko import CoinGeckoAPI
from utils.slp_helpers import *
from utils.embed_messages import easyembed

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
        past1 = past[len(past)-2]

        dXdY = (past[len(past)-1] - past[0])/(len(past) - 1)

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
            value=f"{symbol}{price}",
        )
        embed.add_field(
            name=f"Direction",
            value="⬆" if past1 < price else "⬇",
        )
        embed.add_field(
            name=f"Rate of Change",
            value=f"{symbol}{dXdY:.5f} per second",
            inline=False
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

        file = discord.File("assets/images/graphs/slp/minutely.png", filename="mnt.png")

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
    async def convert(self, ctx, currency, total_slp, percentage=None):
        await ctx.message.channel.trigger_typing()

        cg = CoinGeckoAPI()
        price = float(get_slpprice(currency)['smooth-love-potion'][currency]) 

        symbol = cg.get_exchange_rates()['rates'][currency]['unit']

        if percentage is None:
            total = price * float(total_slp)
        else:
            total = price * float(total_slp)
            total_part = price * float(total_slp) * (float(percentage)/100)

        embed = discord.Embed(
            description=f"The converted value of {total_slp} SLP to {currency.upper()}.",
            color=0x1ABC9C,
            timestamp=datetime.utcnow()
        )
        embed.set_author(
            name="Total SLP Converter",
            icon_url="https://cdn.discordapp.com/attachments/545533157131288587/876658614553686016/slp.png"
        )
        if percentage is None:
            embed.add_field(
                name=f"Current SLP to {currency.upper()} rate",
                value=f"{symbol}{price}",
                inline=False
            )
            embed.add_field(
                name=f"Total SLP converted to {currency.upper()}",
                value=f"{symbol}{total}",
                inline=False
            )
        else:
            embed.add_field(
                name=f"Current SLP to {currency.upper()} rate",
                value=f"{symbol}{price}",
                inline=False
            )
            embed.add_field(
                name=f"Total SLP converted to {currency.upper()}",
                value=f"{symbol}{total:.2f}",
                inline=False
            )
            embed.add_field(
                name=f"({percentage}%) of the total SLP converted to {currency.upper()} ",
                value=f"{symbol}{total_part:.2f}",
                inline=False
            )
        embed.set_footer(
            text="As of"
        )

        await ctx.send(embed=embed)
    
    @rate.error 
    async def rate_error(self, ctx, error):
        error = getattr(error, 'original', error)
        if isinstance(error, KeyError):
            e = easyembed("Error in Rate Command", 
                "error",
                "The currency you have provided does not exist. Please try another currency.", 
                "Use the help command for more information."
            )

            await ctx.send(embed=e)

            return 
        
        if isinstance(error, commands.MissingRequiredArgument):
            e = easyembed("Error in Rate Command", 
                "error",
                f"You are missing the `{error.param}` argument. Please provided all the required arguments for the command to work.", 
                "Use the help command for more information."
            )

            await ctx.send(embed=e)

            return 
        
        e = easyembed("Error in Rate Command", 
            "error",
            "An unhandled error has been detected. Please report this to the developers.", 
            "Use the help command for more information."
        )

        await ctx.send(embed=e)

    @historyminutely.error 
    async def historyminutely_error(self, ctx, error):
        error = getattr(error, 'original', error)
        if isinstance(error, ValueError):
            e = easyembed("Error in Historyminutely Command", 
                "error",
                "The currency you have provided does not exist. Please try another currency.", 
                "Use the help command for more information."
            )

            await ctx.send(embed=e)

            return 
        
        if isinstance(error, commands.MissingRequiredArgument):
            e = easyembed("Error in Historyminutely Command", 
                "error",
                f"You are missing the `{error.param}` argument. Please provided all the required arguments for the command to work.", 
                "Use the help command for more information."
            )

            await ctx.send(embed=e)

            return 
        
        e = easyembed("Error in Historyminutely Command", 
            "error",
            "An unhandled error has been detected. Please report this to the developers.", 
            "Use the help command for more information."
        )

        await ctx.send(embed=e)

    @convert.error 
    async def convert_error(self, ctx, error):
        error = getattr(error, 'original', error)
        if isinstance(error, KeyError):
            e = easyembed("Error in Convert Command", 
                "error",
                "The currency you have provided does not exist. Please try another currency.", 
                "Use the help command for more information."
            )

            await ctx.send(embed=e)

            return 

        if isinstance(error, ValueError):
            e = easyembed("Error in Convert Command", 
                "error",
                f"The argument you provided was not supported. Make sure you only provided integer values for the total slp and percentage parameters.", 
                "Use the help command for more information."
            )

            await ctx.send(embed=e)

            return 
        
        if isinstance(error, commands.MissingRequiredArgument):
            e = easyembed("Error in Convert Command", 
                "error",
                f"You are missing the `{error.param}` argument. Please provided all the required arguments for the command to work.", 
                "Use the help command for more information."
            )

            await ctx.send(embed=e)

            return 
        
        
        e = easyembed("Error in Convert Command", 
            "error",
            f"An unhandled error has been detected. Please report this to the developers.", 
            "Use the help command for more information."
        )

        await ctx.send(embed=e)
        
def setup(bot):
    bot.add_cog(SLP(bot))