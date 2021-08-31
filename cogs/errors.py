from discord.ext import commands
from discord.ext.commands import Cog

class Errors(Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    @Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return

        ignored = (commands.CommandNotFound,)

        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return

        raise error

def setup(bot):
    bot.add_cog(Errors(bot))