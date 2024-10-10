import os
from discord.ext import commands
import discord
import asyncio
from dotenv import load_dotenv


load_dotenv()
bot_token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=".",case_insensitive=True,intents=intents)




@bot.event
async def on_ready():
    print(f'{bot.user} It\'s on!')

@bot.event
async def on_command_error(ctx, err):
        print(err)

@bot.command()
async def channelID(ctx):
    await ctx.send(ctx.channel.id)


async def main():
  async with bot:
    await bot.load_extension('cogs.statistika')
    await bot.load_extension('cogs.schedule')
    await bot.start(bot_token)

if __name__ == '__main__':
  asyncio.run(main())
