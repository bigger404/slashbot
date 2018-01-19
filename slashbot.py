#!/usr/bin/python3
import bigbot

from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import subprocess
import time,re

host = 'irc.2600.net'
port = 6667
user = 'name'
nick = 'luser'
channel = '#words'
Url = "http://slashdot.org"

#html = urlopen(Url)
stories = list()

def say_title(title):
    try:
        if title:
            bot.send(channel,title)
    except Exception as e:
        print(e)

bot = bigbot.IRC()
bot.connect(host,port, nick, channel)


while(True):
    html = urlopen(Url)
    bsObj=BeautifulSoup(html,"lxml")
    for story in bsObj.findAll("span",{"class":"story-title"}):
        try:
            if story not in stories:
                stories.append(story)
                title = story.find("a").text
                print(title)
                safe_title= re.sub(r'[^\w\s]','',title)
                say_title(str(safe_title))
        except Exception as e:
            print(e)
    time.sleep(360)
 
    
bot.disconnect() 
