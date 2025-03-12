from discord.ext import commands

class Teste(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def teste(self, ctx):
        await ctx.send("Este é um comando de teste!")

# Certifique-se de que a função setup é assíncrona
async def setup(bot):
    await bot.add_cog(Teste(bot))