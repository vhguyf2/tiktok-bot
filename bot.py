import discord
from discord.ext import commands
import random
import string
import os
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.command()
async def create_4letter(ctx, count: int = 1):
    if count > 10:
        await ctx.send("Max 10 per request.")
        return
    
    created = []
    for i in range(count):
        handle = ''.join(random.choices(string.ascii_lowercase, k=4))
        created.append(f"✅ `{handle}`")
    
    embed = discord.Embed(title="4-Letter Handles", color=discord.Color.green())
    embed.add_field(name="Generated", value="\n".join(created), inline=False)
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    print(f"Bot online as {bot.user}")

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")
    bot.run(TOKEN)
