# Cruzeiro

This is the same old bot for the Discord Server of CSUL, but i've changed the code. It's better now.

[Discord.py](https://discordpy.readthedocs.io/en/stable/index.html)
[Heroku](https://devcenter.heroku.com/categories/python-support)

# How i did

The bot is now running on Heroku servers, using only free features. There are some new commands on Heroku CLI that can be a problem if you don't pay attention.
I'll list some things i almost miss while read the documentations, on the first attempt to host this bot.

#### → Create Python reference -

  * Heroku won't able the packages if they don't be referred. I used **heroku buildpacks:set heroku/python** to set the python package.

#### → Setting Procfile and requirements -

  * These two files must be created at the same directory as the *.py* script. The _Procfile_ can't have a extension, and will contain the _web/worker_ dynos to 
  actually connect the app to Heroku.
  * I downloaded _gunicorn_ to use these dynos properly, but i don't really needed it at all. All i had to do was run the dynos with the **python** parameter. 
  
  ![Procfile](https://user-images.githubusercontent.com/61850743/120256302-35333a80-c264-11eb-9d37-3a3027a4016f.png)
  
  * The _requirements.txt_ has to contain all the packages/versions that are being used on the application. I also forgot to put a "discord=" line to invoke the
  main discord package.
  * On Heroku CLI, i had to make a **heroku ps:scale web=1 worker=1** after update the Procfile. This line sets the amount of dynos that will be used. Also, i had
  to enable the options of web and worker (after commit) on Heroku dashboard resources page.
  
  ![Heroku Resources](https://user-images.githubusercontent.com/61850743/120257737-213d0800-c267-11eb-8128-563b8fc83ccf.png)

  
 #### → Changing branches -
 
 * Yes, i was in the remote branch master, which was used to be the default branch for Heroku. However, i had to change it to the **main** branch, using the
 command line **git checkout main**. After doing this, the code was able to actually being pushed.
 * The code i edit is on master branch (Github), i just change to main everytime i need to push it to Heroku.

  
