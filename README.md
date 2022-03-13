# Italian-Japanese translation discord bot "Koba-Chan" (in python)

![alt text](images_videos/bot-test.gif)

## About this bot

As a japanese language learner I joined several language exchange discord servers. In particular I'm very active in an italian-japanese exchange server.
This server has a lot of begginer level learners that often inevitably find themselves to have to rely on automatic translation machines.
Because of that I thought it could have been educational to me (and, hopefully, useful to the server members) to try to learn how to create in python a discord that can translate a text into italian, japanese or english.
This bot I'm showing here is the result of my experiment.
The bot is called by the command prefix '$', followed by 'it', 'jp' or 'en', depending on the language you want your text to be translated into. You have to include the text you want to translate after the command in the same message.

### Requirements to create the bot

- A discord acount to access the Discord Developer portal and create the bot.
- A discord server where you can test and use your bot.
- A replit account to host and run your code.
- A UptimeRobot account to create a web server and keep your bot alive even when you close the replit tab (Replit keeps the app running for 30 minutes after closing the tab).
- A DeepL account to access their API

#### Libraries

- discord.py
- os
- deepl
- flask

## Add my bot to your discord server

Click the following link, choose the server in which you want to add the bot and give it the required authorizations:
https://discord.com/api/oauth2/authorize?client_id=897218429524803654&permissions=274877991936&scope=bot

### Warning

DeepL's free plan allows the user to request up to 500.000 carachters to translate per month. Because of that, if many servers start using the bot the monthly limit might be easily reached. If you want to heavily use this bot I suggest to create your own bot on the discord developer portal and make an account on deepl.com . Then copy my code replacing the tokens. In the video linked in the following section you can see how to easily set everything up!

## Learning Resources

- I learned everything that you need to know to start creating discord bots in python, hosting them on replit and deploy a server on UptimeRobot watching this video on youtube: https://www.youtube.com/watch?v=SPTfmiYiuok
- https://discordpy.readthedocs.io/en/stable/index.html Discord python library documentation
- https://www.deepl.com/en/docs-api/ Deepl API documentation
