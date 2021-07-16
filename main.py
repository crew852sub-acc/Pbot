import discord
from discord_slash import SlashCommand

import os
import asyncio
import numpy as np
import random

import bot_func as bf

bot = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)
guild_ids = bot.guilds

#캐릭목록
charlist_path = os.path.dirname(os.path.abspath(__file__)) + "/캐릭목록.txt"
o = open(charlist_path, "r", encoding="utf-8")
charlist = o.read().split()


# events

@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("'/'로 기능확인"))

# commands

@slash.slash(name="골라줘", description='두 옵션중 하나를 골라줍니다.', guild_ids=guild_ids)
async def vs(ctx, opt1, opt2):
    srgd = bf.random([opt1, opt2], [0.5, 0.5])
    embed=discord.Embed(title=srgd, description="이게 좋을 듯 :thumbsup:", color=0xffae00)
    await ctx.send(embed=embed)

@slash.slash(name="청소", description='입력받은 줄 수만큼 채팅을 지워줍니다.', guild_ids=guild_ids)
async def clear(ctx, sheep : int):
    await ctx.send(":broom: 청소중...")
    await ctx.channel.purge(limit = sheep+1)

@slash.slash(name="주사위", description='입력받은 눈 수만큼의 주사위를 굴려줍니다.', guild_ids=guild_ids)
async def dice(ctx, number : int):
    embed=discord.Embed(title=':game_die: 주사위를 굴려서 나온 숫자는...', description=f'[{random.randint(1,int(number))}]  이(가) 나왔습니다.', color=0xffae00)
    await ctx.send(embed=embed)

@slash.slash(name="철권랜덤", description='랜덤으로 아무 캐릭터나 뽑아줍니다.(철권)', guild_ids=guild_ids)
async def r(ctx):
    choicechar = random.choice(charlist)
    embed = discord.Embed(title=":game_die: 캐릭터 랜덤 선택 결과...", description=f'[{choicechar}] (이)가 나왔습니다.', color=0xb377ee)
    await ctx.send(embed=embed)


bot.run(os.environ['token'])