# Cruzeiro

This is the same old bot for the Discord Server of CSUL, but i've changed the code. 

[Discord.py](https://discordpy.readthedocs.io/en/stable/index.html)

# How i did

The bot is now running on Heroku servers, using only free features. There are some new commands on Heroku CLI that can be a problem if you don't pay attention.
I'll list some steps i miss on the first attempt to host this bot. 

#### → Setting Procfile and requirements -

  * These two files must be created at the same directory as the *.py* script. The _Procfile_ can't have a extension, and will contain the _web/worker_ dynos to 
  actually connect the app to Heroku.
  * I downloaded _gunicorn_ to use these dynos properly, but i don't really needed it at all. All i had to do was run the dynos with the **python** parameter. 
  
  ![Procfile](https://user-images.githubusercontent.com/61850743/120256302-35333a80-c264-11eb-9d37-3a3027a4016f.png)

  
