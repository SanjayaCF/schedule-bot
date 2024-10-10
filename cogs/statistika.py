import discord
from discord.ext import commands
import random


intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=".",case_insensitive=True,intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready.")

class Statistika(commands.Cog):  
  def __init__(self, client):
    self.bot = bot

  def mean(self,data):
    ind = len(data)//2
    if len(data)%2 == 0:
      mean = (data[ind]+data[ind-1])/2
    else:
      mean = data[ind]
    return mean
  
  def quartil(self,data):
    ind = len(data)//2
    if len(data)%2 == 0:
      q2 = self.mean(data)
      q1 = self.mean(data[:ind])
      q3 = self.mean(data[ind:])
    else:
      q2 = self.mean(data)
      q1 = self.mean(data[:ind])
      q3 = self.mean(data[ind+1:])
    iqr = q3-q1
    return [('Q1',q1),('Q2',q2),('Q3',q3),('IQR',iqr)]
    

  @commands.command()
  async def soal(self, ctx):
    n_soal = random.randint(10,15)
    data = [random.randint(1,100) for _ in range(n_soal)]
    await ctx.send(', '.join(map(str,data)))
    data.sort()
    await ctx.send('\n'.join(f'{i}: {j}' for i,j in self.quartil(data)))

  @commands.command()
  async def tes(self,ctx):
    await ctx.send('yolo')
  


async def setup(bot):
  await bot.add_cog(Statistika(bot))