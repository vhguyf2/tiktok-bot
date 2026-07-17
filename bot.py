import discord
from discord.ext import commands
import asyncio
import random
import string
import os
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

class TikTokAccountCreator:
    def __init__(self):
        self.created_accounts = []
    
    def generate_4letter_handle(self):
        return ''.join(random.choices(string.ascii_lowercase, k=4))

creator = TikTokAccountCreator()

@bot.command()
async def create_4letter(ctx, count: int = 1):
    if count > 10:
        await ctx.send("Max 10 per request.")
        return
    
    embed = discord.Embed(title="TikTok Account Creator", color=discord.Color.blue())
    embed.add_field(name="Status", value="🔄 Creating...", inline=False)
    msg = await ctx.send(embed=embed)
    
    created = []
    for i in range(count):
        handle = creator.generate_4letter_handle()
        created.append(f"✅ `{handle}`")
        await asyncio.sleep(1)
    
    embed = discord.Embed(title="Results", color=discord.Color.green())
    embed.add_field(name="Handles", value="\n".join(created), inline=False)
    await msg.edit(embed=embed)

@bot.event
async def on_ready():
    print(f"Bot online as {bot.user}")

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")
    bot.run(TOKEN)
