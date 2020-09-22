import discord
from discord.ext import commands, tasks
import random
from itertools import cycle
import time
import json
import os
import shutil
import asyncio
from discord.utils import get
import datetime
from discord import Spotify

client = commands.Bot(command_prefix="a!")
client.remove_command('help')
status = cycle(["Listening to a!help" , "Among Us"])

@client.event
async def on_ready():
	change_status.start()
	print("Bot is ready.")

@tasks.loop(minutes=60)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)))

@client.command(aliases = ["Invite" , "INVITE"])
async def invite(ctx):
	embed = discord.Embed(title = "Invite Among Us bot using the below link" , color = discord.Color.green())
	embed.add_field(name = "Go to the official website" , value = "https://bit.ly/3mGSXvR")
	embed.add_field(name = "Invite the best Among Us Bot" , value = "https://bit.ly/3ceYuEW")
	embed.set_thumbnail(url = "https://lh3.googleusercontent.com/VHB9bVB8cTcnqwnu0nJqKYbiutRclnbGxTpwnayKB4vMxZj8pk1220Rg-6oQ68DwAkqO")
	await ctx.send(embed = embed)
	

@client.command(aliases = ["Vc" , "VC"])
async def vc(ctx , code = None , server = None):
	if ctx.guild.id == 757239002826014731:
		cat = discord.utils.get(ctx.guild.categories , id = 757247392981450813)
	else:
		cat = ctx.message.channel.category

	await ctx.author.guild.create_voice_channel(name = f"🚀{code} -> {server}" , category = cat , user_limit = 11)
	vch = discord.utils.get(ctx.author.guild.voice_channels , name = f"🚀{code} -> {server}")
	vch.permissions_for(ctx.author)
	await ctx.author.create_dm()
	await ctx.author.dm_channel.send("Your voice channel has been created successfully, It will be deleted after 30 minutes. Here is your link.")
	link = await vch.create_invite(max_uses = 11)
	await ctx.author.dm_channel.send(f"{link}")
	await asyncio.sleep(1800)
	await vch.delete()

@client.command()
async def server_count(ctx):
	await ctx.send(f"I am in {len(client.guilds)} servers")

@client.command(aliases = ["Guide" , "GUIDE"])
async def guide(ctx):
	embed = discord.Embed(title = "Among Us Guide Page" , color = discord.Color.orange())
	embed.set_image(url = "https://static.wixstatic.com/media/9c8bab_551ea43d32db4c099dadc8d76509da95~mv2.gif")
	msg = await ctx.send(embed = embed)
	await asyncio.sleep(30)
	guide = discord.Embed(title = "Among Us Guide Page" , color = discord.Color.orange())
	guide.add_field(name = ":map:Full Guide" , value = "https://bit.ly/2ZHsF2A")
	guide.add_field(name = "<:among_us:755993889508163655>Crewmate" , value = "https://bit.ly/3khxtU6")
	guide.add_field(name = ":detective:Imposter" , value = "https://bit.ly/2ZHsF2A")
	guide.add_field(name = "To learn about maps use the below command" , value = "a!maps" , inline = False)
	guide.set_thumbnail(url = "https://lh3.googleusercontent.com/VHB9bVB8cTcnqwnu0nJqKYbiutRclnbGxTpwnayKB4vMxZj8pk1220Rg-6oQ68DwAkqO")
	await msg.edit(embed = guide)

@client.command(aliases = ['Maps' , 'MAPS'])
async def maps(ctx):
	among = discord.Embed(title = "Choose one of the below maps by typing the command `a!{map name}`.\n Eg. a!skeld \nyou can choose between skeld, mirahq and polus" , color = discord.Color.orange())
	among.set_thumbnail(url = 'https://lh3.googleusercontent.com/VHB9bVB8cTcnqwnu0nJqKYbiutRclnbGxTpwnayKB4vMxZj8pk1220Rg-6oQ68DwAkqO')
	await ctx.send(embed = among)
	
@client.command(aliases = ['Info_skeld' , 'INFO_SKELD'])
async def skeld(ctx):
	skeld = discord.Embed(title = 'Skeld' , color = discord.Color.orange())
	skeld.set_image(url = 'https://preview.redd.it/tv8ef4iqszh41.png?auto=webp&s=46faf550020fd59c8d8bab29705b0fcb80521850')
	await ctx.send(embed = skeld)
	
@client.command(aliases = ['Info_polus' , 'INFO_POLUS'])
async def polus(ctx):
	polus = discord.Embed(title = 'Polus' , color = discord.Color.orange())
	polus.set_image(url = 'https://vignette.wikia.nocookie.net/among-us-wiki/images/4/4c/Polus.png/revision/latest?cb=20200907133344')
	await ctx.send(embed = polus)
	
@client.command(aliases = ['Info_mirahq' , 'INFO_MIRAHQ'])
async def mirahq(ctx):
	mira = discord.Embed(title = 'Mira HQ' , color = discord.Color.orange())
	mira.set_image(url = 'https://vignette.wikia.nocookie.net/among-us-wiki/images/0/0a/Mirahq.png/revision/latest?cb=20200907132939')
	await ctx.send(embed = mira)

@client.command(aliases = ["Ping" , "PING"])
async def ping(ctx):
	await ctx.send(f'Ping: {round(client.latency * 1000)} ms')

@client.command(aliases = ["Mod" , "MOD"])
async def mod(ctx):
	embed = discord.Embed(title = "Get free Among Us skins" , color = discord.Color.orange())
	embed.add_field(name = "Download mod the apk from the link below" , value = "https://bit.ly/2HnBp7K")
	embed.set_thumbnail(url = "https://lh3.googleusercontent.com/VHB9bVB8cTcnqwnu0nJqKYbiutRclnbGxTpwnayKB4vMxZj8pk1220Rg-6oQ68DwAkqO")
	await ctx.send(embed = embed)

@client.command(aliases=['HELP', 'Help'])
async def help(ctx):
	await ctx.message.author.create_dm()
	helpm  = discord.Embed(title = f"Among Us Help!" , color = discord.Color.darker_grey())
	helpm.set_thumbnail(url = 'https://lh3.googleusercontent.com/VHB9bVB8cTcnqwnu0nJqKYbiutRclnbGxTpwnayKB4vMxZj8pk1220Rg-6oQ68DwAkqO')
	helpm.add_field(name = "Hey! My prefix is a!" , value = "So Lets go through my commands" , inline = False)
	helpm.add_field(name = ":one: guide -> will guide you" , value = "This will give you all the required information about the game" , inline = False)
	helpm.add_field(name = ":two: maps -> will show you all maps" , value = "This will give you the blueprints of all the maps" , inline = False)
	helpm.add_field(name = ":three: ping -> Shows the bot's latency" , value = "Pong!" , inline = False)
	helpm.add_field(name = ":four: vc {code} {server} -> Makes a special voice channel" , value = "U can invite the people you want(limit = 11)" , inline = False)
	await ctx.message.author.dm_channel.send(embed = helpm)
	await ctx.send("You've got mail!!")

client.run("NzU3MjcyNDQyODIwMzYyMjgx.X2d-6w.IFFVlAkqE_16LP41xGMCpFiJAy4")