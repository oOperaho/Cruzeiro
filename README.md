# Cruzeiro

This is the same old bot for the Discord Server of CSUL, but i've changed the code. 

[Discord.py](https://discordpy.readthedocs.io/en/stable/index.html)

# How i did

The bot is now running on Heroku servers, using only free features. There are some new commands on Heroku CLI that can be a problem if you don't pay attention.
I'll list some steps i miss on the first attempt to host this bot. 

#### → Setting Procfile and requirements -

  * These two files must be created at the same directory as the *.py* script. The _Procfile_ can't have a extension, and will contain the _web/worker_ dynos to 
  actually connect the app to Heroku.
  * 

