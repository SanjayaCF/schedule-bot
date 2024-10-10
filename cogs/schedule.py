from PyPDF2 import PdfReader
import re
from pymongo import MongoClient,DESCENDING,ASCENDING
import discord
from discord.ext import commands
import io
import requests
import datetime
import asyncio
import os
from discord.ext import tasks
from dotenv import load_dotenv



load_dotenv()
MONGO_URL = os.getenv('MONGO_URL')
DB_CLUSTER = os.getenv('DB_CLUSTER')
DB_COLLECTION = os.getenv('DB_COLLECTION')


intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=".",case_insensitive=True,intents=intents)
cluster = MongoClient(MONGO_URL)
db = cluster[DB_CLUSTER]
collection = db[DB_COLLECTION]

class Schedule(commands.Cog):
    def __init__(self, client):
        self.bot = bot
        self.check_schedule_task = None

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.check_schedule_task or self.check_schedule_task.is_cancelled():
            self.check_schedule_task = self.check_schedule.start()
        print(f'Logged in as {self.bot.user}')

    def insert_matkul(self, text, authorId):
        exist, success = ["Matkul Berikut Sudah Ada:"], ["Berhasil Ditambahkan:"]
        keys = ('_id', 'matkul', 'grup', 'hari', 'jam', 'ruang')
        for raw_subjects in re.findall('([A-Z]{2}\d{4})  ([A-Z].+)  ([A-Z])(?: \d \d\.\d) ([A-Za-z].+), (.+) (\w.+)', text):
            _id = raw_subjects[0] + raw_subjects[2]
            if collection.count_documents({'_id': _id}, limit=1) == 1:
                exist.append(f'{raw_subjects[1]} Grup {raw_subjects[2]}')
                collection.update_one({'_id': _id}, {'$push': {'mentions': authorId}})
                continue
            subjects = {'_id': _id} | ({key: subject for key, subject in zip(keys[1:], raw_subjects[1:])} | {'mentions': [authorId]})
            jamMulai, jamSelesai = subjects['jam'].split('-')
            subjects['jamMulai'] = jamMulai
            subjects['jamSelesai'] = jamSelesai
            collection.insert_one(subjects)
            success.append(f'{raw_subjects[1]} Grup {raw_subjects[2]}')
        return (success, exist)



    @commands.command()
    async def kelas(self, ctx):
        embed = discord.Embed(title=f"Kelas **{ctx.author.name}**:", timestamp=datetime.datetime.utcnow(), color=0xFF5733)
        embed.set_footer(icon_url=ctx.author.display_avatar.url, text=ctx.author.name)
        embed.set_thumbnail(url="https://i.pinimg.com/originals/29/ac/32/29ac324edd6a070fb97590f1c16d78eb.jpg")
        for num, kelas in enumerate(collection.find({'mentions': {'$in': [ctx.author.id]}}).sort([('hari', DESCENDING), ('jam', ASCENDING)]), start=1):
            embed.add_field(name=f'{num}. {kelas["matkul"]} {kelas["grup"]}', value=f'__{kelas["hari"]} | **{kelas["jam"]}** | {kelas["ruang"]}__', inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def krs(self, ctx):
        authorId = ctx.author.id
        for attachment in ctx.message.attachments:
            response = requests.get(url=attachment, headers={'User-Agent': 'Mozilla/5.0 (X11; Windows; Windows x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36'}, timeout=120)
            on_fly_mem_obj = io.BytesIO(response.content)
            reader = PdfReader(on_fly_mem_obj)
            page = reader.pages[0]
            text = page.extract_text()
            async with ctx.typing():
                embed = discord.Embed(title=f"Penambahan dari {attachment.filename}", timestamp=datetime.datetime.utcnow(), color=0xFF5733)
                embed.set_thumbnail(url="https://i.imgflip.com/3cfko6.jpg")
                embed.set_footer(icon_url=ctx.author.display_avatar.url, text=ctx.author.name)
                for status in self.insert_matkul(text, authorId):
                    if len(status) <= 1:
                        continue
                    embed.add_field(name=status[0], value="\n".join(f"{num}. {matkul}" for num, matkul in enumerate(sorted(status[1:]))), inline=False)
                embed.add_field(name="\u200b", value=f"\n\n<@!{authorId}> **Anda Akan Dimention Ketika Sesi Matkul Dimulai.**", inline=False)
            await ctx.send(embed=embed)

    @commands.command()
    async def mention(self, ctx):
        await ctx.send(ctx.author.display_avatar.url)


async def setup(bot):
    await bot.add_cog(Schedule(bot))
