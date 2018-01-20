#!/usr/bin/python3
import bigbot_ssl

host = 'irc.2600.net'
port = 6697
user = 'name'
nick = 'luser'
channel = '#words'

bot = bigbot_ssl.IRC()
bot.connect(host,port, nick, channel)

while(True):
    msg=input("Msg: ")
    if msg=='quit':
        break
    bot.send(channel,msg)
    
bot.disconnect() 
