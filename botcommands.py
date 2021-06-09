from discord.ext import commands
import cruzeiro

cruzeiro.setting()

bot = commands.Bot(command_prefix=".")


# Command Decorators -
def pingcmd():
    @bot.command()
    async def ping(ctx):
        await ctx.send(f"Ping: {round(bot.latency*1000)}ms")


def aboutcmd():
    @bot.command()
    async def about(ctx):
        await ctx.send(f"Regras do servidor → "
                       f"https://discord.com/channels/605585174209495060/797518209364000788/797526727806681089"
                       f"\nColetar cargos → "
                       f"https://discord.com/channels/605585174209495060/685884303057485849/744748856507498527")


def botcodecmd():
    @bot.command()
    async def botcode(ctx):
        await ctx.send(f"Repositório: https://github.com/oOperaho/Cruzeiro")
