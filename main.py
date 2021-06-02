import discord
from discord.ext import commands
import emoji


client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print(f"Logged as → {client.user};")
    actv = discord.Game("CSUL")
    await client.change_presence(status=discord.Status.do_not_disturb, activity=actv)
    print(f"Ready;")


@client.event
async def on_member_join(member):
    print(f"{member.name} has joined the server.")
    await member.send(f"Bem-vindo(a) ao servidor da Cruzeiro do sul, {member.name}!")


@client.event
async def on_member_remove(member):
    print(f"{member.name} left the server.")


@client.command()
async def ping(ctx):
    latency = client.latency
    await ctx.send(f"Ping: {round(latency*1000)}ms")


@client.event
async def cruzeiro(ctx):
    await ctx.send(emoji.emojize(":eye:"))


client.run('lmao token')
