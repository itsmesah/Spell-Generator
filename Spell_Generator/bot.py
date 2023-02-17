#!/usr/bin/python3.10

import disnake
from disnake.ext import commands
from googletrans import Translator
import subprocess
#---- Local includes ---------------------------------------#
from botpy.slashcommands import utility


bot = commands.Bot(
    command_prefix=commands.when_mentioned,
    description="Spell generator bot",
    intents=disnake.Intents.all()
)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


bot.add_cog(utility(bot))


with open('key','r') as f:
    key = f.readlines()[0]

bot.run(key)