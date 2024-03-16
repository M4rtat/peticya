import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$',intents=intents)

putin = False

@bot.event
async def on_ready():
    print('we have loged in as bot')
@bot.command()
async def peticya(ctx,daorno:str):
    await ctx.send('мы дожидаемся вашей подписи петиций')
    if daorno == 'Да':
        await ctx.send('вы сказали да урааа')
    if daorno == 'Нет':
        await ctx.send('вы сказали нет (')
bot.run('токен')
