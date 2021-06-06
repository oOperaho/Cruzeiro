# Simple start

import discord
from discord.ext import commands
import emoji

intents = discord.Intents.default()
intents.members = True
cruzeiro = commands.Bot(command_prefix='.', intents=intents)


# Event Decorators -
@cruzeiro.event
async def on_ready():
    print(f"Logged as: {cruzeiro.user};")
    stats = discord.Game(".about")
    await cruzeiro.change_presence(status=discord.Status.do_not_disturb, activity=stats)


@cruzeiro.event
async def on_member_join(member):
    print(f"{member.name} has joined the server.")
    await member.send(f"Bem-vindo(a) ao servidor da Cruzeiro do sul, {member.name}!"
                      f"\nReaja essa mensagem para receber o cargo de acordo com sua área: "
                      f"https://discord.com/channels/605585174209495060/685884303057485849/744748856507498527")


@cruzeiro.event
async def on_member_remove(member):
    print(f"{member.name} just left the server.")


@cruzeiro.event
async def on_message(ctx):
    ctx.content.lower()
    if ctx.author == cruzeiro.user:
        return
    if "cruzeiro" in ctx.content:
        await ctx.channel.send(emoji.emojize(":eye:"))
    await cruzeiro.process_commands(ctx)


# Command Decorators -
@cruzeiro.command()
async def ping(ctx):
    await ctx.send(f"Ping: {round(cruzeiro.latency*1000)}ms")


@cruzeiro.command()
async def about(ctx):
    await ctx.send(f"Regras do servidor → "
                   f"https://discord.com/channels/605585174209495060/797518209364000788/797526727806681089"
                   f"\nColetar cargos → "
                   f"https://discord.com/channels/605585174209495060/685884303057485849/744748856507498527")


@cruzeiro.command()
async def botcode(ctx):
    await ctx.send(f"Repositório: https://github.com/oOperaho/Cruzeiro")


# Running bot
cruzeiro.run('token')
