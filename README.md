# Among Us Discord Bot (beta)

This is an Among Us Discord bot that auto mutes players in certain situations, without *anyone in the game needing to mute manually*. This will make Among Us way more intense and doesn't break the immersion of the game having to mute all the time.

## Installation PLEASE READ BEFORE DOING ANYTHING

Please bare with the setup of this process, it will take a moment so make sure to follow each step carefully. <br />
Firstly, we need to make sure you have python3 and pip3 already installed on your windows machine

1) Open your command prompt on windows as administrator
2) Type "python3". If you don't have it installed, Microsoft Store will open automatically and you can download it from there. If you do have it installed, type "quit()" to quit from the python environment and carry on
3) Download tesseract <a href="https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe" download>here</a> and install it
3) Copy and paste the text below into your command prompt and wait for them all to install

``` 
python3 -m pip install pytesseract
python3 -m pip install selenium
python3 -m pip install Pillow
python3 -m pip install -U --user mss
python3 -m pip install opencv-python
python3 -m pip install discord
```

4) Next, download the zip file for the Among Us Discord Bot <a href="https://bit.ly/3mbCzTx" download>here</a> and unzip it
5) Navigate to the Among Us folder in the command prompt using cd (e.g. cd Downloads\AmongUsBot-master\)
6) Run "python3 test.py" and see if it runs without any errors. You can test by fullscreening the example image and see the screen ratios. Make sure the "IMPOSTER" fits nicely inside the window. If by chance it doesn't, you can adjust settings in the config.py in the modules folder. Press "q" to quit the window.
5) Okay finally, watch this tutorial to finish this one time setup! 


[![IMAGE ALT TEXT](https://i.imgur.com/VgEd7qa.jpg)](https://www.youtube.com/watch?v=TrBBLbwmQic "AMONG US Discord Mute Bot [Download and Setup Tutorial]")

Note: I am aware of the bug that doesn't let you mute yourself during rounds (If you died). Working on a fix.<br />
Note: I have an idea and I'm working on a way to implement this on phones
