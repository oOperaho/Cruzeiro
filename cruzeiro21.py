# Simple start, import packages and connect to Discord API

import discord
from discord.ext import commands
import events
import botcommands


# Function used to call intents, also in other files
intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix=".")


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
bot.run("token")
