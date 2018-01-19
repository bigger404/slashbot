#!/usr/bin/python3
import bigbot

host = 'irc.2600.net'
port = 6667
user = 'name'
nick = 'luser'
channel = '#words'

bot = bigbot.IRC()
bot.connect(host,port, nick, channel)

while(True):
    msg=input("Msg: ")
    if msg=='quit':
        break
    bot.send(channel,msg)
    
bot.disconnect() 
