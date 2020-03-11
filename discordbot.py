from discord.ext import commands
import os
import traceback
import discord
import asyncio

client = commands.Bot(command_prefix='!')

@client.event
async def on_error(ctx,message):
    pass

@client.event
async def on_ready():
    client.ch = client.get_channel(1) #channel.id
    await client.ch.send("..atk")

def battle_check(m):
    if not m.embeds:
        return 0
    if not m.embeds[0].title:
        return 0
    return "待ち構えている" in m.embeds[0].title

@client.event
async def on_message(msg):
    ch = msg.channel
    if ch.id == 1: #channel.id
        if msg.author.id == 567999794879135745:

            if battle_check(msg):
                await asyncio.sleep(3) 
                await ch.send("..i kn")
                try:
                    await client.wait_for('message', timeout=5)
                except TimeoutError:
                    await ch.send('..atk')

            if "攻撃失敗" in msg.content:
                await ch.send("..atk")

            if "アイテム使用失敗" in msg.content:
                await ch.send("..i e")

            if "既に戦闘中" in msg.content:
                await asyncio.sleep(10)
                await ch.send('..atk')
                try:
                    await client.wait_for('message', timeout=10)
                except TimeoutError:
                    await ch.send('..atk')

            if "全回復" in msg.content:
                await ch.send('..atk')

            if "やられている！" in msg.content:
                await ch.send("..i e")

            em = msg.embeds[0]
            if "Ren-testのHP" in em.description:
                await ch.send("..atk")

            else:

                if "HP" in message.embed.description: 
                    await message.channel.send("..atk")

client.run('Njg0NTc0NjIwNzI0MTAxMTMy.Xmjp9g.KFa6T33ebbv-QgzMYc-OxsPft3Y') 
