import discord
from discord.ext import commands
from constants.prepared_texts import *
from secrets import TOKEN

bot = commands.Bot(command_prefix='slp ')
bot.remove_command('help')

extensions = [
    "cogs.slp",
    "cogs.axs",
    "cogs.errors"
]

@bot.event 
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("getting created..."))

    print(f"Running SLP Bot...")
    print(f"SLP Bot online on version 0.1")
    print("EVERYTHING BELOW THIS WILL BE THE LOG INSTANCES")
    print("===============================================")

@bot.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    try:
        bot.load_extension(extension)
        await ctx.send(SUCC_LOAD.format(extension))
        print(f"{extension} was loaded.")
    except Exception as e:
        await ctx.send(ERR_LOAD.format(extension, e))

@bot.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    try:
        bot.unload_extension(extension)
        await ctx.send(SUCC_UNLOAD.format(extension))
        print(SUCC_UNLOAD.format(extension))
    except Exception as e:
        await ctx.send(ERR_LOAD.format(extension, e))

@bot.command()
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        description="Displays all the command functions of the bot.",
        color=0x1ABC9C,
    )
    embed.set_author(
        name="SLP Bot Help",
        icon_url="https://cdn.discordapp.com/attachments/545533157131288587/876658614553686016/slp.png"
    )
    embed.add_field(
        name="Prefix",
        value="`slp`",
        inline=False
    )
    embed.add_field(
        name="rate <currency>",
        value="Displays the current SLP rate for input currency.",
        inline=False
    )
    embed.add_field(
        name="axsrate/axsr <currency>",
        value="Displays the current AXS rate for input currency.",
        inline=False
    )
    embed.add_field(
        name="historyminutely/hm <currency>",
        value="Displays the minutely graph of SLP based on input currency.",
        inline=False
    )
    embed.add_field(
        name="axshistoryminutely/axshm <currency>",
        value="Displays the minutely graph of AXS based on input currency.",
    )

    await ctx.send(embed=embed)

if __name__ == '__main__':
    for ext in extensions:
        try:
            bot.load_extension(ext)
            print(f"Loaded extesion: {ext}")
        except Exception as e:
            print(ERR_LOAD.format(ext, e))

bot.run(TOKEN)