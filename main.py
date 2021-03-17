import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import urllib.request
from urllib import request, parse 
import re
import json
from random import randint

load_dotenv()
TOKEN = os.getenv ('DISCORD_TOKEN')

key='xxx you youtube key'



bot = commands.Bot(command_prefix="-")

saludos = ('Hola', 'Hola mamasita', 'Hola pishi putita', 'Hola Puñetas','Kpdo', 'Eri gei')
numaleatorio = ('1','34','63','85','53','23','45','76','32','52','82','92','18','2','4','56','10','83','94','91','192','217','823','83','283','17')



@bot.command(name='subs') #Funcion que mostrara los suscriptores de un canal de Youtube que le pasemos como parametro
async def subscriptores(ctx,username,channel):
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + username +"&key=" + key).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    response = username + " tiene " + "{:,d}".format(int(subs)) + " suscriptores!"
    await ctx.send(response)


@bot.command(name='Suma')
async def sumar(ctx , num1,num2):
    response = int(num1)+int(num2)
    await ctx.send(response)

@bot.command(name='resta')
async def resta(ctx, num1,num2):
    response = int(num1)-int(num2)
    await ctx.send(response)

@bot.command(name='multiplicacion')
async def multiplicacion(ctx, num1,num2):
    response = int(num1)*int(num2)
    await ctx.send(response)

@bot.command(name='division')
async def division(ctx, num1,num2):
    response = int(num1)/int(num2)
    await ctx.send(response)

@bot.command(name='Hola')
async def Hola(ctx):

    await ctx.send(saludos[randint(0,5)])

@bot.command(name='aleatorio')
async def aleatorio(ctx):

    await ctx.send(numaleatorio[randint(0,25)])

@bot.command(name='youtube')
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
  
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    print(search_results)
    
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])


  

#@bot.command(name='comocagar')
#async def comocagar(ctx):
#    await ctx.send('https://www.youtube.com/watch?v=SDpDuaPOIYI')
  
#@bot.command(name='help')
#async def help(ctx):
#    await ctx.send(Hola+'hola')


#@bot.command(name='numero')
#async def numero(ctx):
 #   await ctx.send()


#@bot.command(name='temp')
#async def temp(ctx, num1 ):
 #   response = int(num1)-int(num2)
  #  await ctx.send(response)  

bot.run(TOKEN)
