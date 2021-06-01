<h1 allign="center"> Cruzeiro </h1>

This is the same old bot for the Discord Server of CSUL, but i've changed the code. It's better now.

[Discord.py](https://discordpy.readthedocs.io/en/stable/index.html)\
[Heroku](https://devcenter.heroku.com/categories/python-support)

<h2 allign="center"> How i did </h2>

The bot is now running on Heroku servers, using only free features. There are some new commands on Heroku CLI that can be a problem if you don't pay attention.
I'll list some things i almost miss while read the documentations, on the first attempt to host this bot.

### → Create Python reference -

  * Heroku won't able the buildpacks if they don't be referred. I used **heroku buildpacks:set heroku/python** to set it.
  * This can be configurated at the **heroku create** command, creating the app and setting the buildpack inside.

### → Set Procfile and requirements -

  * These two files must be created at the same directory as the *.py* script. The _Procfile_ can't have a extension, and will contain the _web/worker_ dynos to 
  actually connect the app to Heroku.
  * I downloaded _gunicorn_ to use these dynos properly, but i don't really needed it at all. All i had to do was run the dynos with the **python** parameter. 
  
  ![Procfile](https://user-images.githubusercontent.com/61850743/120256302-35333a80-c264-11eb-9d37-3a3027a4016f.png)
  
  * The _requirements.txt_ has to contain all the packages/versions that are being used on the application. I also forgot to put a "discord==1.0.1" line to invoke the
  main discord package.
  * On Heroku CLI, i had to make a **heroku ps:scale web=1 worker=1** after update the Procfile. This line sets the amount of dynos that will be used. Also, i had
  to enable the options of web and worker (after commit) on Heroku dashboard resources page.
  
  ![Heroku Resources](https://user-images.githubusercontent.com/61850743/120257737-213d0800-c267-11eb-8128-563b8fc83ccf.png)

### → Change branches and deploy -
 
  * Yes, i was in the remote branch master, which was used to be the default branch for Heroku. However, i had to change it to the **main** branch, using the
  command line **git checkout main**. After doing this, the code was able to actually being pushed.
  * The code i edit is on master branch (Github), i just change to main everytime i need to push it to Heroku. So, the first time i deployed, the bot was 
  pinging each 30 seconds. I've added the **worker** dyno, edited some lines of the code and pushed it. The bot is on, working fine.
 
  ![Bot](https://user-images.githubusercontent.com/61850743/120260002-5f3c2b00-c26b-11eb-9ee6-22d976f88bb7.png)
  
I'll update every change or issues on the application, this readme just tells the things i did to solve some problems. If there's something that can be changed or 
solved in a better way, i can edit it anytime, so it can be helpful to others.  
