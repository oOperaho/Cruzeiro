import discord
import emoji

intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged as → {client.user};")
    actv = discord.Game("CSUL")
    await client.change_presence(status=discord.Status.do_not_disturb, activity=actv)
    print("Ready;")


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    if msg.content == ".lat":
        pong = client.latency
        await msg.channel.send(f"{msg.author.mention} {pong:1f}")
    if "cruzeiro" in msg.content or "Cruzeiro" in msg.content:
        await msg.channel.send(emoji.emojize(":eye:"))
    if client.user in msg.content:
        await msg.channel.send(emoji.emojize(":eye:"))


@client.event
async def on_member_join(member):
    print(f"{member.name} has joined the server.")
    await member.send(f"Bem-vindo(a) ao servidor da Cruzeiro do sul, {member.name}!")


@client.event
async def on_member_remove(member):
    print(f"{member.name} left the server.")


client.run('lmao token')
