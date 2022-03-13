from discord.ext import commands 
import os  
import deepl   
import keep_alive  

key = os.getenv('deeplKey')  #deeplKey is your key to access deepl api
client = commands.Bot(command_prefix="$") #initialize discord - every command for your bot will start with $
translator = deepl.Translator(key) #initialize deepl translator

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

###translates to italian###
@client.command(pass_context=True)
async def it(ctx): #the command is called by a message starting with $it
  string = ctx.message.content[4:] 
  translated = translator.translate_text(string, target_lang="IT") 
  await ctx.channel.send(translated) 

###translates to japanese###
@client.command(pass_context=True)
#command: $jp
async def jp(ctx, string): 
  string = ctx.message.content[4:]
  translated = translator.translate_text(string, target_lang="JA")
  await ctx.channel.send(translated)

###translates to english###
@client.command(pass_context=True)
#command: $en
async def en(ctx, string): 
  string = ctx.message.content[4:]
  translated = translator.translate_text(string, target_lang="EN-US")
  await ctx.channel.send(translated)

keep_alive.keep_alive()
client.run(os.getenv('token')) #token is your discord app key