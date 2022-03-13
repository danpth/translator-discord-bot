from discord.ext import commands #discord api
import os  #access environment variables
import deepl   #deepl api
import keep_alive  #keeps the server alive

key=os.getenv('deeplKey')  #deeplKey is your key to access deepl api
client = commands.Bot(command_prefix="$") #initialize discord - every command for your bort will start with $
translator=deepl.Translator(key) #initialize deepl translator

@client.event  #on login
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

#translates to italian
@client.command(pass_context=True)
async def it(ctx): #the command is called by a message starting with $it
  string=ctx.message.content[4:] #the message to translate is what comes after the command $it
  translated=translator.translate_text(string, target_lang="IT") #this method sends the string parameter to deepl and returns a string containing the translated message
  await ctx.channel.send(translated) #sends string parameter in the discord channel

#translates to japanese
@client.command(pass_context=True)
async def jp(ctx, string): 
  string=ctx.message.content[4:]
  translated=translator.translate_text(string, target_lang="JA")
  await ctx.channel.send(translated)

#translates to english
@client.command(pass_context=True)
async def en(ctx, string): 
  string=ctx.message.content[4:]
  translated=translator.translate_text(string, target_lang="EN-US")
  await ctx.channel.send(translated)

keep_alive.keep_alive()
client.run(os.getenv('token')) #token is your discord app key