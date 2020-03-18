# bot.py
import os
import re

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Hola {member.name}, benvingut al servidor de l'Ajuntament de Sant Vicenç de Castellet."
        f'Per que puguis entrar als xats del teu Departament, comenta a consultes en Informàtica o demana-ho als administradors'
        f'Recorda marcar les entrades i sortides de la jornada laboral a travès de https://forms.gle/fTtS8RHNVmXwV7d18'
        f'Que tinguis un bon dia.'
    )
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    sol = ['Possiblement el problema es que no cliques el enllaç del llamp. Alla veuras els desplegables per fer cont+alt+sup']
    patron = re.compile(r'\bloqueig\b')
    if patron.match(message.content) != None:
        response = random.choice(sol[0])
        await message.channel.send(response)
client.run(TOKEN)
