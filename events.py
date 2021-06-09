import discord
from discord.ext import commands
import emoji
import main

main.setting()

cruzeiro = commands.Bot(command_prefix=".")


# Event Decorators -
def login():
    @cruzeiro.event
    async def on_ready():
        print(f"Logged as: {cruzeiro.user};")
        stats = discord.Game(".about")
        await cruzeiro.change_presence(status=discord.Status.do_not_disturb, activity=stats)


def newmember():
    @cruzeiro.event
    async def on_member_join(member):
        print(f"{member.name} has joined the server.")
        await member.send(f"Bem-vindo(a) ao servidor da Cruzeiro do sul, {member.name}!"
                          f"\nReaja essa mensagem para receber o cargo de acordo com sua área: "
                          f"https://discord.com/channels/605585174209495060/685884303057485849/744748856507498527")


def memberleft():
    @cruzeiro.event
    async def on_member_remove(member):
        print(f"{member.name} just left the server.")


def newmsg():
    @cruzeiro.event
    async def on_message(ctx):
        ctx.content.lower()
        if ctx.author == cruzeiro.user:
            return
        if "cruzeiro" in ctx.content:
            await ctx.channel.send(emoji.emojize(":eye:"))
        await cruzeiro.process_commands(ctx)
