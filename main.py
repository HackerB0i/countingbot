import discord, asyncio
import os
import json
import random
from dotenv import load_dotenv
from discord.ext import commands, tasks
from discord import Activity, ActivityType
import time
client = commands.Bot(command_prefix = 'c!')

@client.event
async def on_ready():
	print("count bot initiated")
	await client.change_presence(status = discord.Status.online,activity = discord.Game("counts numbers!"))
	client.remove_command('help')
@client.command
async def count(countto, ctx):
	for x in countto:
		await ctx.send(x)
keep_alive()
client.run(os.getenv('token')) # this is your bot's token in the discord applications thing
