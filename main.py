import discord
from discord.ext import commands
import emoji

intents = discord.Intents.default()
intents.members = True
cruzeiro = commands.Bot(command_prefix='.', intents=intents)


@cruzeiro.event
async def on_ready():
    print(f"Logged as → {cruzeiro.user};")
    actv = discord.Game("CSUL")
    await cruzeiro.change_presence(status=discord.Status.do_not_disturb, activity=actv)


@cruzeiro.event
async def on_member_join(member):
    print(f"{member.name} has joined the server.")
    await member.send(f"Bem-vindo(a) ao servidor da Cruzeiro do sul, {member.name}!")


@cruzeiro.event
async def on_member_remove(member):
    print(f"{member.name} left the server.")


@cruzeiro.event
async def on_message(ctx):
    ctx.content.lower()
    if ctx.author == cruzeiro.user:
        return
    if "cruzeiro" in ctx.content:
        await ctx.channel.send(emoji.emojize(":eye:"))
    await cruzeiro.process_commands(ctx)


@cruzeiro.command()
async def ping(ctx):
    await ctx.send(f"Ping: {round(cruzeiro.latency*1000)}ms")


cruzeiro.run('lmao token')
