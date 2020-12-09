import discord
from discord.ext import commands
import praw
import random
from PIL import Image , ImageDraw , ImageFont
import dbl
import os
from discord.ext import menus

def get_prefix(client , message):
	main_server = client.get_guild(730075470694973461)
	if len(main_server.text_channels) > 480:
		main_server_2 = client.get_guild(753269919684231178)
		for channel in main_server_2.text_channels:
			if str(channel.name) == str(message.guild.id):
				prfx = channel.topic
				return prfx


	for channel in main_server.text_channels:
		if str(channel.name) == str(message.guild.id):
			prfx = channel.topic
			return prfx

	basic_prefix = "a!"
	return basic_prefix

class Helpfunc(menus.Menu):
    def __init__(self , client):
        self.client = client
        self.token = os.environ.get('dbl_token')
        self.dblpy = dbl.DBLClient(client , self.token)
        super().__init__(timeout=90.0 , delete_message_after=True)

    async def send_initial_message(self , ctx ,channel):
        start = discord.Embed(title = 'Among Us Help' , description = 'React below to pick an option\n:radioactive: ➜ Among Us Utilities\n:game_die: ➜ Fun & Games\n:clipboard: ➜ Utilities\n🤩 ➜ Memes\n`Liked the bot? To vote it` : **[Click here](https://top.gg/bot/757272442820362281/vote)**\n`To join support server` : [Click Here](https://discord.gg/tgyW2Jz)\n`To go to bots website` : [Click Here](https://amongusunofficial.godaddysites.com/)\n`To browse through bots code` : [Click Here](https://github.com/Cooldude069/AmongUs.git)' , color = discord.Color.orange())
        start.set_thumbnail(url = "https://lh3.googleusercontent.com/VHB9bVB8cTcnqwnu0nJqKYbiutRclnbGxTpwnayKB4vMxZj8pk1220Rg-6oQ68DwAkqO")
        start.set_footer(text = f'Command ran by {self.ctx.author.display_name}')

        return await channel.send(embed = start)

    @menus.button('☢')
    async def amngutils(self , payload):
        p = get_prefix(self.client , self.message)
        au = discord.Embed(title = '☢ Among us Utilities' , description = f'`{p}guide` ➜ Will teach you to play\n`{p}maps` ➜ Will show you the blueprints of all maps\n`{p}vc <code> <server>` ➜ Will create a voice channel\n`{p}mute` ➜ Mutes people lower than you in the vc\n`{p}unmute` ➜ Unmutes people lower than you in the vc\n`{p}host <Code> <Server>` ➜ Makes your game discoverable to others\n`{p}match <server>` ➜ Shows you the visible games in that server' , color = discord.Color.orange())
        au.set_thumbnail(url = 'https://lh3.googleusercontent.com/VHB9bVB8cTcnqwnu0nJqKYbiutRclnbGxTpwnayKB4vMxZj8pk1220Rg-6oQ68DwAkqO')
        au.set_footer(text = f'Command ran by {self.ctx.author.display_name}')
        await self.message.edit(embed = au)

    @menus.button('🎲')
    async def fng(self , payload):
        p = get_prefix(self.client , self.message)
        f = discord.Embed(title = '🎲 Fun & Games' , description = f'`{p}rps` ➜ Starts a rock, paper , scissors game with the bot\n`{p}challenge <user>` ➜ Play a 1v1 rock, paper scissors with your friend\n`{p}flip` ➜ Flips a coin for you\n`{p}kill <user>` ➜ Sends a cool among us killing gif\n`{p}imposter <user>` ➜ makes him/her an Imposter\n`{p}crewmate <user>` ➜ makes him/her a Crewmate\n`{p}guess` ➜ You have to guess the imposter\n`{p}ascii <text>` ➜ Creates an ASCII banner of that text' , color = discord.Color.orange())
        f.set_thumbnail(url = 'https://lh3.googleusercontent.com/VHB9bVB8cTcnqwnu0nJqKYbiutRclnbGxTpwnayKB4vMxZj8pk1220Rg-6oQ68DwAkqO')
        f.set_footer(text = f'Command ran by {self.ctx.author.display_name}')
        await self.message.edit(embed = f)

    @menus.button('📋')
    async def utils(self , payload):
        p = get_prefix(self.client , self.message)
        u = discord.Embed(title = '📋 Utilities' , description = f'`{p}emoji` ➜ Generates a random Among Us emoji\n`{p}add` ➜ Adds emojis to your server\n`{p}ping` ➜ displays the bots latency\n`{p}prefix <new prefix>` ➜ Changes the bots prefix' , color = discord.Color.orange())
        u.set_thumbnail(url = 'https://lh3.googleusercontent.com/VHB9bVB8cTcnqwnu0nJqKYbiutRclnbGxTpwnayKB4vMxZj8pk1220Rg-6oQ68DwAkqO')
        u.set_footer(text = f'Command ran by {self.ctx.author.display_name}')
        await self.message.edit(embed = u)

    @menus.button('🤩')
    async def mc(self , payload):
        p = get_prefix(self.client , self.message)
        voted = await self.dblpy.get_user_vote(self.ctx.author.id)
        if voted:
            description = f'`{p}meme` ➜ Fetches a funny meme from Reddit\n`{p}drake <text> , <text>` ➜ Generates a Drake meme\n`{p}sword <text> , <text>`➜ Generates a Sword meme\n`{p}announce <text>` ➜ Generates a Simpson meme.\n`{p}patrick <text>` ➜ Generates a Patrick meme\n`{p}spongebob <text>` ➜ Generates a Spongebob meme\n`{p}shit <text>` ➜ Generates a stepped-in-shit meme\n`{p}santa <text>` ➜ Generates a Santa meme'
        else:
            description = '''```
        .--------.
       / .------. \ 
      / /        \ \ 
      | |        | |
     _| |________| |_
    .'|_|        |_| '.
    '._____ ____ _____.'
    |     .'____'.     |
    '.__.'.'    '.'.__.'
    '.__  |      |  __.'
    |   '.'.____.'.'   |
    '.____'.____.'____.'
    '.________________.'```\nUpvote the Bot to access this category.\n`To upvote the Bot ` **[Click Here](https://top.gg/bot/757272442820362281/vote)**'''
                                            
        m = discord.Embed(title = '🤩 Memes' , description = description , color = discord.Color.orange())
        m.set_thumbnail(url = 'https://lh3.googleusercontent.com/VHB9bVB8cTcnqwnu0nJqKYbiutRclnbGxTpwnayKB4vMxZj8pk1220Rg-6oQ68DwAkqO')
        m.set_footer(text = f'Command ran by {self.ctx.author.display_name}')
        await self.message.edit(embed = m)

    @menus.button('🏠')
    async def home(self , payload):
        start = discord.Embed(title = 'Among Us Help' , description = 'React below to pick an option\n:radioactive: ➜ Among Us Utilities\n:game_die: ➜ Fun & Games\n:clipboard: ➜ Utilities\n🤩 ➜ Memes\n`Liked the bot? To vote it` : **[Click here](https://top.gg/bot/757272442820362281/vote)**\n`To join support server` : [Click Here](https://discord.gg/tgyW2Jz)\n`To go to bots website` : [Click Here](https://amongusunofficial.godaddysites.com/)\n`To browse through bots code` : [Click Here](https://github.com/Cooldude069/AmongUs.git)' , color = discord.Color.orange())
        start.set_thumbnail(url = "https://lh3.googleusercontent.com/VHB9bVB8cTcnqwnu0nJqKYbiutRclnbGxTpwnayKB4vMxZj8pk1220Rg-6oQ68DwAkqO")
        start.set_footer(text = f'Command ran by {self.ctx.author.display_name}')
        await self.message.edit(embed = start)

class Memes(commands.Cog):
    def __init__(self , client):
        self.client = client
        self.token = os.environ.get('dbl_token')
        self.dblpy = dbl.DBLClient(self.client , self.token)

    @commands.command(aliases = ['Meme' , 'MEME'])
    async def meme(self , ctx):
        voted = await self.dblpy.get_user_vote(ctx.author.id)
        print(voted)
        if not voted:
            embed = discord.Embed(description = 'You Need to Upvote the bot to use this command.\nTo upvote the bot **[Click Here](https://top.gg/bot/757272442820362281/vote)**' , color = discord.Color.red())
            return await ctx.send(embed = embed)

        reddit = praw.Reddit(client_id = '0bD1UHrRzjDbGQ',
                            client_secret = '9xoApJv0eZeRr1QVGJJulIE5cjXyFg',
                            username = 'CooLDuDE-6_9',
                            password = 'samarth1709',
                            user_agent = 'AmongUsUnofficial')

        memeList = []

        dankmemes = reddit.subreddit('dankmemes')
        hot = dankmemes.hot(limit = 50)
        for meme in hot:
            memeList.append(meme)

        rmemes = reddit.subreddit('memes')
        mHot = rmemes.hot(limit = 50)
        for nmeme in mHot:
            memeList.append(nmeme)

        sendable_meme = random.choice(memeList)
        embed = discord.Embed(description = f'**[{sendable_meme.title}]({sendable_meme.url})**' , color = discord.Color.from_rgb(random.randint(0 , 255), random.randint(0 , 255) ,random.randint(0 , 255)))
        embed.set_image(url = sendable_meme.url)
        embed.set_footer(text = f'🔥 {sendable_meme.score} | 💬 {len(sendable_meme.comments)}')
        await ctx.send(embed = embed)

    @commands.command(aliases = ['Drake' , 'DRAKE'])
    async def drake(self , ctx , * , text = ''):
        voted = await self.dblpy.get_user_vote(ctx.author.id)
        print(voted)
        if not voted:
            embed = discord.Embed(description = 'You Need to Upvote the bot to use this command.\nTo upvote the bot **[Click Here](https://top.gg/bot/757272442820362281/vote)**' , color = discord.Color.red())
            return await ctx.send(embed = embed)

        if text == '':
            return await ctx.send('You need to pass some text separated by a ","')

        index = text.find(',')
        if index == -1:
            return await ctx.send('You need to pass some text separated by a ","')

        text_one , text_two = text.split(',')

        if len(text_one) > 42 or len(text_two) > 42:
            return await ctx.send('Your text cannot exceed 48 characters(total of 84 including both).')

        img = Image.open('drake.jpg')
        draw = ImageDraw.Draw(img)
        t_one = text_one
        t_two = text_two
        font = ImageFont.truetype('arial.ttf' , 60)
        increment = 0
        if len(t_one) > 14:
            while len(text_one) > 14:
                t_one = text_one[0:13]
                draw.text((520 , 40 + increment) , t_one , (0 , 0, 0),font = font)
                increment += 130
                text_one = text_one[13:]

            draw.text((520 , 40 + increment) , text_one , (0 , 0, 0),font = font)
        else:
            draw.text((520 , 40) , t_one , (0 , 0, 0),font = font)

        increment = 0 
        if len(text_two) > 14:
            while len(text_two) > 14:
                t_two = text_two[0:13]
                draw.text((520 , 460 + increment) , t_two , (0 , 0, 0),font = font)
                increment += 130
                text_two = text_two[13:]
            
            draw.text((520 , 460 + increment) , text_two , (0 , 0, 0),font = font)
        else:
            draw.text((520 , 460) , t_two , (0 , 0, 0),font = font)

        img.save('drakeout.jpg')
        await ctx.send(file = discord.File('drakeout.jpg'))

    @commands.command(aliases = ['Sword' , 'SWORD'])
    async def sword(self , ctx , *,text = ''):
        voted = await self.dblpy.get_user_vote(ctx.author.id)
        print(voted)
        if not voted:
            embed = discord.Embed(description = 'You Need to Upvote the bot to use this command.\nTo upvote the bot **[Click Here](https://top.gg/bot/757272442820362281/vote)**' , color = discord.Color.red())
            return await ctx.send(embed = embed)
            
        if text == '':
            return await ctx.send('You have to provide two texts separated by a ","')

        index = text.find(',')

        if index == -1:
            return await ctx.send('You have to provide two texts separated by a ","')

        # 132,73 font = 40

        # 11 , 12

        text_one , text_two = text.split(',')
        if len(text_one) > 10 or len(text_two) > 20:
            return await ctx.send('The first text should not exceed 11 characters and second cannot exceed 21.')

        img = Image.open('sword.jfif')
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('arial.ttf' , 40)
        draw.text((132,73) , text_one , (0,0,0) , font = font)
        draw.text((68,273) , text_two , (0,0,0) , font = font)

        img.save('swordout.jpg')
        await ctx.send(file = discord.File('swordout.jpg'))

    @commands.command(aliases = ['Announce' , 'ANNOUNCE'])
    async def announce(self , ctx , * , text = ''):
        voted = await self.dblpy.get_user_vote(ctx.author.id)
        print(voted)
        if not voted:
            embed = discord.Embed(description = 'You Need to Upvote the bot to use this command.\nTo upvote the bot **[Click Here](https://top.gg/bot/757272442820362281/vote)**' , color = discord.Color.red())
            return await ctx.send(embed = embed)

        if text == '':
            return await ctx.send('You need to pass some text.')

        if len(text) > 78:
            return await ctx.send('Your text cannot exceed 78 characters.')

        font = ImageFont.truetype('arial.ttf' , 60)
        img = Image.open('announce.png')
        draw = ImageDraw.Draw(img)
        #450 , 80
        #450 , 225
        increment = 0
        if len(text) > 26:
            txt = ''
            while len(text) > 26:
                txt = text[0:25]
                draw.text((450 , 80+increment) , txt , (0,0,0) , font = font)
                increment += 145
                text = text[25:]

            draw.text((450 , 80+increment) , text , (0,0,0) , font = font)
        else:
            draw.text((450 , 80) , text , (0,0,0) , font = font)

        img.save('announceout.png')
        await ctx.send(file = discord.File('announceout.png'))

    @commands.command(aliases = ['Patrick' , 'PATRICK'])
    async def patrick(self , ctx , * , text = ''):
        voted = await self.dblpy.get_user_vote(ctx.author.id)
        print(voted)
        if not voted:
            embed = discord.Embed(description = 'You Need to Upvote the bot to use this command.\nTo upvote the bot **[Click Here](https://top.gg/bot/757272442820362281/vote)**' , color = discord.Color.red())
            return await ctx.send(embed = embed)

        if text == '':
            return await ctx.send('You need to pass some text.')

        #11 , 130 , 470
        img = Image.open('patrick.jpg')
        font = ImageFont.truetype('arial.ttf' , 40)
        draw = ImageDraw.Draw(img)
        
        if len(text) > 33:
            return await ctx.send('Your text cannot excceed 33 characters.')

        increment = 0
        if len(text) > 11:
            txt = ''
            while len(text) > 11:
                txt = text[0:10]
                draw.text((130,470+increment) , txt , (0,0,0) , font = font)
                increment += 70
                text = text[10:]

            draw.text((130,470+increment) , text , (0,0,0) , font = font)

        else:
            draw.text((130,470) , text , (0,0,0) , font = font)

        img.save('patrickout.jpg')
        await ctx.send(file = discord.File('patrickout.jpg'))

    @commands.command(aliases = ['Spongebob' , 'SPONGEBOB'])
    async def spongebob(self , ctx , * , text = ''):
        voted = await self.dblpy.get_user_vote(ctx.author.id)
        print(voted)
        if not voted:
            embed = discord.Embed(description = 'You Need to Upvote the bot to use this command.\nTo upvote the bot **[Click Here](https://top.gg/bot/757272442820362281/vote)**' , color = discord.Color.red())
            return await ctx.send(embed = embed)

        if text == '':
            return await ctx.send('You need to pass some text.')

        img = Image.open('spongebob.png')
        font = ImageFont.truetype('arial.ttf' , 30)
        draw = ImageDraw.Draw(img)
        
        if len(text) > 44:
            return await ctx.send('Your text cannot excceed 44 characters.')

        increment = 0
        if len(text) > 11:
            txt = ''
            while len(text) > 11:
                txt = text[0:10]
                draw.text((60,85+increment) , txt , (0,0,0) , font = font)
                increment += 40
                text = text[10:]

            draw.text((60,85+increment) , text , (0,0,0) , font = font)

        else:
            draw.text((60,85) , text , (0,0,0) , font = font)

        img.save('spongeout.png')
        await ctx.send(file = discord.File('spongeout.png'))

    @commands.command(aliases = ['Shit' , 'SHIT'])
    async def shit(self , ctx , * , text = ''):
        voted = await self.dblpy.get_user_vote(ctx.author.id)
        print(voted)
        if not voted:
            embed = discord.Embed(description = 'You Need to Upvote the bot to use this command.\nTo upvote the bot **[Click Here](https://top.gg/bot/757272442820362281/vote)**' , color = discord.Color.red())
            return await ctx.send(embed = embed)

        if text == '':
            return await ctx.send('You need to pass some text.')

        img = Image.open('shit.jpg')
        font = ImageFont.truetype('arial.ttf' , 15)
        draw = ImageDraw.Draw(img)
        
        if len(text) > 33:
            return await ctx.send('Your text cannot excceed 33 characters.')

        increment = 0
        if len(text) > 11:
            txt = ''
            while len(text) > 11:
                txt = text[0:10]
                draw.text((90,210+increment) , txt , (0,0,0) , font = font)
                increment += 30
                text = text[10:]

            draw.text((90,210+increment) , text , (0,0,0) , font = font)

        else:
            draw.text((90,210) , text , (0,0,0) , font = font)

        img.save('shitout.jpg')
        await ctx.send(file = discord.File('shitout.jpg'))

    @commands.command(aliases = ['Santa' , 'SANTA'])
    async def santa(self , ctx , * , text = ''):
        voted = await self.dblpy.get_user_vote(ctx.author.id)
        print(voted)
        if not voted:
            embed = discord.Embed(description = 'You Need to Upvote the bot to use this command.\nTo upvote the bot **[Click Here](https://top.gg/bot/757272442820362281/vote)**' , color = discord.Color.red())
            return await ctx.send(embed = embed)

        if text == '':
            return await ctx.send('You need to pass some text.')

        img = Image.open('santa.jpg')
        font = ImageFont.truetype('arial.ttf' , 30)
        draw = ImageDraw.Draw(img)
        
        if len(text) > 72:
            return await ctx.send('Your text cannot excceed 72 characters.')

        increment = 0
        if len(text) > 18:
            txt = ''
            while len(text) > 18:
                txt = text[0:17]
                draw.text((40,475+increment) , txt , (0,0,0) , font = font)
                increment += 40
                text = text[17:]

            draw.text((40,475+increment) , text , (0,0,0) , font = font)

        else:
            draw.text((40,475) , text , (0,0,0) , font = font)

        img.save('santaout.jpg')
        await ctx.send(file = discord.File('santaout.jpg'))

    @commands.command()
    async def help(self , ctx):
        h = Helpfunc(self.client)
        await h.start(ctx)


        
def setup(client):
    client.add_cog(Memes(client))