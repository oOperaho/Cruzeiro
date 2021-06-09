# Simple start, import packages and connect to Discord API

import discord
from discord.ext import commands
import events
import botcommands


def setting():
    intents = discord.Intents.default()
    intents.members = True


cruzeiro = commands.Bot(command_prefix=".",)


events.login()

events.newmember()

events.memberleft()

events.newmsg()

botcommands.pingcmd()

botcommands.aboutcmd()

botcommands.botcodecmd()


# Running bot
cruzeiro.run('token')
