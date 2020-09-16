# Among Us Discord Bot

Join our discord server if you have any ideas, issues, or want early access to new updates and features! https://discord.gg/PVfewrM<br />

THIS IS CURRENTLY DISCONTINUED - Please check out https://github.com/denverquane/amongusdiscord !

This is an Among Us Discord bot that auto mutes and unmutes players in certain situations, without *anyone in the game needing to mute manually*. This will make Among Us way more intense and doesn't break the immersion of the game having to mute all the time.

## Installation and setup

Please bare with the setup of this process, it will take a moment so make sure to follow each step carefully. <br />
Note: make sure you have python3 and pip3 already installed on your windows machine

1) Download the dependancies - go to your command prompt, navigate to your folder where you downloaded the AmongUsBot using "cd" command (Check https://www.digitalcitizen.life/command-prompt-how-use-basic-commands if you are stuck on this step)
2) Type this into your cmd and wait for the download to finish
``` 
python3 -m pip install -r requirements.txt
```
3) Go to https://discord.com/developers/applications and create a new application and add a new bot in the bot panel
4) Navigate to the OAuth2 panel and in scopes, click bot. Then scroll down and choose "Mute members" and "Deafen members" as the permissions of the bot. Copy the link and paste it onto another tab and authorize this bot to your server
6) Copy the bot token in the bot panel.
7) Go to the config.py file and edit it. Change the discord_bot_token to your discord bot token e.g. (discord_bot_token = "XzUzMjgzODaddasfxMjAxMzAy.X1j8QQ.kGDZ54234123X2XQkQ_eUasdFSIzmI") and save it
8) Run the start.bat file
9) Now read the discord server setup

# Set up discord server

Currently the bot wont respond if you don't assign it a host (the bot will mute/unmute/deafen everyone in the same voice channel as the host)

1) Make sure the bot has come online, you can type .ping in any chat on your server to check!
2) Now type .host and you should be assigned as host. 
3) Thats it! Check out .help for more commands (I would recommend activating .ghostmode, its pretty fun)

NOTE: When a member dies, they must type .dead in discord so they will be muted until the end of the game. Also someone can instead type .kill @Discordname1 @Discordname2 instead so not everyone needs to type .dead

This video is outdated, but may help if your struggling with setting up the discord bot! Click the image below to watch the video!
[![IMAGE ALT TEXT](https://i.imgur.com/VgEd7qa.jpg)](https://www.youtube.com/watch?v=TrBBLbwmQic "AMONG US Discord Mute Bot [Download and Setup Tutorial]")

# Fixing errors

If the program is not quite picking up on some instances where, for example, it doesnt mute when voting has ended. Try and run test.py and use an image of when "voting ended" text appears and callibrate it using the settings in config.py to make sure the text fits nicely inside the smaller window. 

If you get a tesseract error, open module_process.py and change pytesseract.pytesseract.tesseract_cmd = r"C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe" to pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" to r"C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe", changing USER to your computer name, of course

If you are getting a connection error, try change 'address = "127.0.0.1"' to either "0.0.0.0" or "localhost"

If you are getting a Discord SSL Certificate error, install this certificate: https://crt.sh/?d=2835394

# Dev note

Thanks for everyone that was interested in my project. Although I didn't expect it to blow up (and cause so much issues for people haha). Nonetheless thank you. This has spawned alot a discussion and some amazing people are brewing up a way better and intuitive bot that looks extrememly promising! Head over to our discord https://discord.gg/PVfewrM for more updates
