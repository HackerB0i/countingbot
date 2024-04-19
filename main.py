import discord, asyncio
import os
import json
import random
from dotenv import load_dotenv
from discord.ext import commands, tasks
from discord import Activity, ActivityType
import time
from ping import keep_alive
client = commands.Bot(command_prefix = 'e!')

@client.event
async def on_ready():
	print("egbot")
	await client.change_presence(status = discord.Status.online,activity = discord.Game("eg"))
	client.remove_command('help')
@client.command
async def count(countto, ctx):
	for x in countto:
		await ctx.send(x)
keep_alive()
client.run(os.getenv('token'))
