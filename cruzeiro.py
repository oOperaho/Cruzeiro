# Simple start, import packages and connect to Discord API

import discord
from discord.ext import commands
import events
import botcommands


# Function used to call intents, also in other files
def setting():
    intents = discord.Intents.default()
    intents.members = True


cruzeiro = commands.Bot(command_prefix=".",)


# Calling event Decorators from events.pu
events.login()

events.newmember()

events.memberleft()

events.newmsg()

# Calling command Decorators from botcommands.py
botcommands.pingcmd()

botcommands.aboutcmd()

botcommands.botcodecmd()


# Running bot
cruzeiro.run("Njk2NzQyOTgyODk1Nzk2Mjg1.XotKdw.UPdWnzDmYltTRerENeVZfsI8VYU")
