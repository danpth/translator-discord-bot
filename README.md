# Italian-Japanese translation discord bot "Koba-Chan" (in python)

![alt text](images_videos/bot-test.gif)

## About this bot

As a japanese language learner I joined several language exchange discord servers. In particular I'm very active in an italian-japanese exchange server.
This server has a lot of begginer level learners that often inevitably find themselves to have to rely on automatic translation machines.
Because of that I thought it could have been educational to me (and, hopefully, useful to the server members) to try to learn how to create in python a discord that can translate a text into italian, japanese or enhlish.
This bot I'm showing here is the result of my experiment.
The bot is called by the command prefix '$', followed by 'it', 'jp' or 'en', depending on the language you want your text to be translated into. You have to include the text you want to translate after the command in the same message.

### Requirements to create the bot

- A discord acount to access the Discord Developer portal and creat the bot.
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

## Learning Resources

- I learned everything that you need to now to start creating discord bots in python, hosting them on replit and deploy a server on UptimeRobbot watching this video on youtube: https://www.youtube.com/watch?v=SPTfmiYiuok
- https://discordpy.readthedocs.io/en/stable/index.html Discord python library documentation
- https://www.deepl.com/en/docs-api/ Deepl API documentation
