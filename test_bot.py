토큰 = "ODM0OTk2NDM2NzIxODYwNjI4.YIJBBw.Ma5x25caiOv23SvOKovq9oTHjok"
import discord
#import youtube_dl
#import openpyxl
import sqlite3
import time
import asyncio
import random
import datetime
#import bs4
import os
import traceback
import contextlib
import io
from pytz import timezone 
from datetime import datetime
#import requests
import urllib
#from bs4 import BeautifulSoup
from discord.ext import commands
join_count = 0
max_count = 5
join_time = 10
delete_count = 0
max_delete = 5
ban_count = 0
max_ban = 5
_time = 10

pre_fix = "+"
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(intents=intents, command_prefix=pre_fix)
@client.event
async def on_ready():
    print("    디스코드 봇이 정상적으로 로그인 되었습니다.    ")
    print("    >> 다음으로 로그인합니다.")
    print("     : BOT NAME | " + client.user.name)
    print("     : BOT CLIENT ID | " + str(client.user.id))
    print(" ")
    print(" ")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("테스트 중"))
@client.command()
async def 안녕(ctx):
    await ctx.send("ㅎㅇ")
@client.event
async def on_member_update(before,after):
    added_role = [role.id for role in before.roles if role not in after.roles]
    if after.roles != before.roles:
        if 812714920952070203 in added_role:
            await client.get_channel(int(813292674127626250)).send(f"{after.mention} <@&830013637443452929>  {after.guild.name} 서버에 오신걸 환영합니다:ribbon:\n<#813288644218454057> 에 원하는 역할을 지급하시면 됩니다.")
@client.listen()
async def on_message(message):
    if message.channel.id == 825596587609948191:
        await message.add_reaction('✅')
        with open("안내실적.txt",'a',-1,'utf-8') as a:
            a.write(str(message.content)+"\n")
@client.listen()
async def on_member_join(member):
    if int(member.guild.id) == int(812713230320402452):
        await member.add_roles(discord.utils.get(member.guild.roles, id = 812786863042723840))#성별#
        await member.add_roles(discord.utils.get(member.guild.roles, id = 812714921728671744))#일반#
        await member.add_roles(discord.utils.get(member.guild.roles, id = 812786865853825045))#나이#
        await member.add_roles(discord.utils.get(member.guild.roles, id = 821380736673775666))#언급#
        await member.add_roles(discord.utils.get(member.guild.roles, id = 812714906251165707))#성격#
        await member.add_roles(discord.utils.get(member.guild.roles, id = 821380645871419422))#게임#
        await member.add_roles(discord.utils.get(member.guild.roles, id = 821384661182709830))#주의#
        await member.add_roles(discord.utils.get(member.guild.roles, id = 822050515763462155))#사용권#
        await member.add_roles(discord.utils.get(member.guild.roles, id = 822050515763462155))#사용권#
        await member.add_roles(discord.utils.get(member.guild.roles, id = 812714920952070203))#새로온 사람
        embed=discord.Embed(title="", description=f"""

<#813039442146623568> 에  닉네임/나이작성 필수 [나이비공개역할 ]/성별/들어온경로 적어주시고

<#825536880233414676> 에서 <@&825353627744993351> 또는 <@&825353712218275900> 을 불러주세요""",color=0x00FF7F)
        embed.set_author(name=f"{member}", icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"{member.guild.name}",icon_url = member.guild.icon_url)
        await client.get_channel(int(813037792501563432)).send(f"{member.mention} {member.guild.name} 에 오신걸 환영합니다.",embed=embed)
#@💛│뉴비왔어요!  :ribbon:가을동화:ribbon:서버에 오신걸 환영합니다:ribbon: #🏧│역할지급방 에 원하는 역할을 지급하시면 됩니다.





    #토큰 테러 보호
    global join_count
    global max_count
    global _time
    join_count = join_count + 1
    if join_count >= max_count:
        for invite in await member.guild.invites():
            await invite.delete()
        채널 = channel_id
        time_ = time.strftime('%m/%d %I:%M %p',time.localtime(time.time()))
        await client.get_channel(int(835027577805733918)).send(f"@everyone 토큰테러가 감지되었습니다\n시간: {time_}")
    await asyncio.sleep(10)
    join_count = 0
@client.listen()
async def on_guild_channel_delete(channel):
    async for entry in channel.guild.audit_logs(limit=1):
        user = '{0.user}'.format(entry) #print('{0.user} did {0.action} to {0.target}'.format(entry)) 
    global delete_count,max_delete,_time
    delete_count = delete_count + 1
    for user_id in channel.guild.members:
        if user_id.name+'#'+user_id.discriminator  == user:
            break
    if delete_count >= max_delete:
        print(user_id)
        await channel.guild.ban(user_id)
        time_ = time.strftime('%m/%d %I:%M %p',time.localtime(time.time()))
        await client.get_channel(835027577805733918).send(f"@everyone 클린테러가 감지되었습니다\n시간: {time_}")
    await asyncio.sleep(10)
    delete_count = 0
@client.listen()
async def on_member_ban(guild,user):
    async for entry in guild.audit_logs(limit=1):
        user = '{0.user}'.format(entry) #print('{0.user} did {0.action} to {0.target}'.format(entry))      
    global ban_count,max_ban,_time
    ban_count = ban_count + 1
    for user_id in guild.members:
        if user_id.name+'#'+user_id.discriminator  == user:
            break
    if ban_count >= max_ban:
        await guild.ban(user_id)
        time_ = time.strftime('%m/%d %I:%M %p',time.localtime(time.time()))
        await client.get_channel(835027577805733918).send(f"@everyone 차단테러가 감지되었습니다\n시간: {time_}")
    await asyncio.sleep(10)
    delete_count = 0
#AttributeError: / """



client.run(토큰)
