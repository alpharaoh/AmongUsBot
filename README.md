# Among Us Discord Bot (beta)

Join our discord server if you have any ideas, issues, or want early access to new updates and features! https://discord.gg/PVfewrM<br />
Check out https://github.com/denverquane/amongusdiscord !

THIS IS STILL A WORK IN PROGRESS, 

This is an Among Us Discord bot that auto mutes and unmutes players in certain situations, without *anyone in the game needing to mute manually*. This will make Among Us way more intense and doesn't break the immersion of the game having to mute all the time.

Note: I am aware of the bug that doesn't let you mute yourself during rounds (If you died). Working on a fix.<br />
Note: I have an idea and I'm working on a way to implement this on phones

## Installation PLEASE READ BEFORE DOING ANYTHING

Please bare with the setup of this process, it will take a moment so make sure to follow each step carefully. <br />
Firstly, we need to make sure you have python3 and pip3 already installed on your windows machine

1) Open your command prompt on windows as administrator
2) Type "python3". If you don't have it installed, Microsoft Store will open automatically and you can download it from there. If you do have it installed, type "quit()" to quit from the python environment and carry on
3) Download tesseract <a href="https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe" download>here</a> and install it
4) Next, download the zip file for the Among Us Discord Bot <a href="https://bit.ly/3mbCzTx" download>here</a> and unzip it
5) Navigate to the Among Us folder in the command prompt using cd (e.g. cd Downloads\AmongUsBot-master\)
6) Copy and paste the text below into your command prompt and wait for them all to install
``` 
python3 -m pip install -r requirements.txt
```
7) Run "python3 test.py" and see if it runs without any errors. You can test by fullscreening the EXAMPLE IMAGE (not the test.py window) and see the screen ratios. Make sure the "IMPOSTER" fits nicely inside the window. If by chance it doesn't, you can adjust settings in the config.py in the modules folder. Press "q" to quit the window.
8) Okay finally, watch this tutorial to finish this one time setup! 

# Set up discord server

Currently the bot wont respond if you don't assign it a server. Follow these steps to connect the bot

1) Make a new voice channel with a name that has no spaces e.g. AmongUs or Among_Us
2) Type in the chat .channel CHANNEL_NAME e.g. .channel AmongUs
3) Every member in the lobby has to type .join CHANNEL_NAME e.g. .join AmongUs
4) Also check .commands for more commands
5) type in .mute and .unmute to check if its working

NOTE: When a member dies, they must type .dead in discord so they will be muted until the end of the game

[![IMAGE ALT TEXT](https://i.imgur.com/VgEd7qa.jpg)](https://www.youtube.com/watch?v=TrBBLbwmQic "AMONG US Discord Mute Bot [Download and Setup Tutorial]")
