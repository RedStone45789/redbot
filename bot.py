import discord, datetime, time
from discord.ext import commands
from datetime import date, datetime

intents = discord.Intents.all()
client = commands.Bot(command_prefix="r!", case_insensitive=True, intents=intents)
times_used = 0


@client.command(name="ping")
async def _ping(ctx):
  global times_used
  await ctx.send(f"Ping: {client.latency}")
  times_used = times_used + 1
@client.command(name="commands")
async def _help(ctx):
    global times_used
    embed=discord.Embed(title="Help", description="Commands of the bot")
    embed.add_field(name="Commands:", value="", inline=False)
    await ctx.send(embed=embed)

















client.run("OTk1Njg1MzI5MTE1ODI0MTQ4.GOwm-9.KlQkx-9LlpGNVEc2tRHmlk1VvVM2eaT-zX1KFI")