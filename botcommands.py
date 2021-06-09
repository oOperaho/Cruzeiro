from discord.ext import commands
import main

main.setting()

cruzeiro = commands.Bot(command_prefix=".")


# Command Decorators -
def pingcmd():
    @cruzeiro.command()
    async def ping(ctx):
        await ctx.send(f"Ping: {round(cruzeiro.latency*1000)}ms")


def aboutcmd():
    @cruzeiro.command()
    async def about(ctx):
        await ctx.send(f"Regras do servidor → "
                       f"https://discord.com/channels/605585174209495060/797518209364000788/797526727806681089"
                       f"\nColetar cargos → "
                       f"https://discord.com/channels/605585174209495060/685884303057485849/744748856507498527")


def botcodecmd():
    @cruzeiro.command()
    async def botcode(ctx):
        await ctx.send(f"Repositório: https://github.com/oOperaho/Cruzeiro")
