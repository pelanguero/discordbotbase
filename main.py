import discord
import os
import requests
import json
from discord.utils import get
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
playerUrl = "https://api.clashofclans.com/v1/players/%23"
getHeader = {"authorization": "Bearer "+os.getenv("TOKEN-COC")}
clan = "#VYUPLPP8"


def jugador(idd):
    responsee = requests.get(playerUrl+idd, headers=getHeader)
    print(responsee)
    return responsee.json()


bot = commands.Bot(command_prefix='!!')


@bot.event
async def on_ready():
    print("Logueado")


@bot.command()
async def register(ctx, arg):
    # intenta cambiar el rol del usuario segun el api de coc
    naame = ""+arg
    if naame.startswith("#"):
        pro = jugador(naame[1:])
    else:
        pro = jugador(naame)
    print("Asignando Usuario")
    if pro["role"] == "leader":
        rolee = get(ctx.guild.roles, name="Líder")
        await ctx.author.add_roles(rolee)
        await ctx.send(ctx.author.name+" ahora es de rango "+"Líder")


@bot.command()
async def player(ctx, arg):
    print("se esta probando el jugador "+arg)
    name = ""+arg
    if name.startswith("#"):
        pro = jugador(name[1:])
    else:
        pro = jugador(name)
    await ctx.send("Nombre: "+pro["name"]+"\n"+"THlvl: "+str(pro["townHallLevel"])+"\n"+"BHlvl: "+str(pro["builderHallLevel"])+"\n"+"XPlvl: "+str(pro["expLevel"])+"\n")
    pass


# @bot.command()
# async def help(ctx, arg):
#     if arg == "coc":
#         bot.commands
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     if message.content.startswith("!coc:"):
#         clashofclans(message)

bot.run(os.getenv("TOKEN"))
