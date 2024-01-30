import asyncio
import discord
from discord.ext import commands
import random

token = "your token"

bot = commands.Bot(command_prefix="!")

@bot.listen()
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.listen()
async def on_message(message):
    #print(message.content)
    pass

@bot.listen()
async def on_message(message):
    if message.content.lower() == "good morning":
        reply = f"Good morning, {message.author.mention}! Have an awesome day <3"
        await message.channel.send(reply)
    await bot.process_commands(message)

@bot.listen()
async def on_message(message):
    if message.content.lower() == "lil star" or message.content.lower() == "lil crab":
        await message.channel.send("shut up old man")
    await bot.process_commands(message)
    

@bot.listen()
async def on_message(message):
    if message.content.lower() == "ok buddy":
        gif_list = ["https://tenor.com/view/cursed-cat-walking-mir-gifs-gif-24160072","https://tenor.com/view/discord-mod-gif-26070007","https://tenor.com/view/discord-meme-spooked-scared-mod-gif-18361254","https://tenor.com/view/bo-gif-20912740","https://tenor.com/view/guy-typing-beanos21-gavin-lol-joke-gif-22174762","https://tenor.com/view/log-cabin-log-logged-get-logged-lolol-gif-20978297","https://tenor.com/view/park-dance-project-zomboid-gif-26426998","https://tenor.com/view/cat-cat-jumping-cat-excited-excited-dance-gif-19354605","https://tenor.com/view/i-want-to-break-free-i-want-to-break-free-music-video-queen-i-want-to-break-free-queen-music-videos-queen-music-video-gif-23659345","https://tenor.com/view/anong-us-gif-22575632","https://tenor.com/view/sdfg-gif-26030168","https://tenor.com/view/funny-animals-back-off-come-at-me-bull-duck-gif-10440887","https://tenor.com/view/shrek-sherk-when-you-h-gif-22237211","https://tenor.com/view/gandalf-smoking-gif-21189890","https://discord.com/channels/@me/644214411883708427/1089906752637640886","https://tenor.com/view/batman-superhero-gif-26117097","https://tenor.com/view/peks-kiss-kiss-creepy-selfie-gif-14709096","https://tenor.com/view/hmm-okay-gif-26217045","https://tenor.com/view/you-you-rn-emo-emo-emoji-emo-meme-gif-25613653","https://tenor.com/view/shit-yourself-ok-buddy-gif-22208644" ,"https://tenor.com/view/plink-wink-plink-wink-wink-plink-gif-27545571","https://tenor.com/view/groove-stickman-meme-dancing-gif-17755675"    ,"https://media.discordapp.net/attachments/831127406101528587/1078368859897200681/1677173161239954.gif", "https://tenor.com/view/uwu-gif-25515456", "https://tenor.com/view/eevo-eevolicious-tea-lara-croft-tomb-raider-gif-21288917"] # Replace with the URLs of the GIFs you want to use
        random_gif = random.choice(gif_list)
        await message.channel.send(random_gif)
    await bot.process_commands(message)
    
    
 #in on_message
async def on_message(message):
    #wont respond to messages sent by the bot
    if bot.user.id != message.author.id:
        ...   
    
    





@bot.listen()
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = "Command on cooldown"
        await ctx.send(msg) 

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def spammany(ctx, *args):
    message = ' '.join(args)
    num_messages = random.randint(10, 50)
    for _ in range(num_messages):
        await ctx.send(message)

bot.loop.create_task(bot.start(token))

try:
    bot.loop.run_forever()
finally:
    bot.loop.close()
