import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do .env

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="v.", intents=intents)

TOKEN = os.getenv("DISCORD_TOKEN")  # Obtém o token de forma segura

# ================================ COMANDOS E EVENTOS ================================= #

@bot.event
async def on_ready():
    print(f'Logado como {bot.user.name}')
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            await bot.load_extension(f'commands.{filename[:-3]}')
    print('Comandos carregados!')
    
@bot.event
async def on_ready(): 
    print("Bot ON")
    canal = bot.get_channel(1349391839610011659)
    if canal:
        await canal.send("BOT ON ✅")
    else:
        print("Canal não encontrado.")

# ================================ RUN ================================= #

bot.run(TOKEN)
