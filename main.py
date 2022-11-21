import discord
import os
from keep_alive import keep_alive

intents = discord.Intents.all()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))

@bot.event
async def on_message(message):
    if str(message.channel) == 'meatflag' and message.content[:2] != "$$":
        print("deleting unauthorized message: ", message.content)
        await message.channel.purge(limit=1)

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET_R")
bot.run(token)
