#!/usr/bin/python3
import socket, threading, ssl

class IRC(threading.Thread):
    #sock = socket.socket()

    def __init__(self):
        self.running = True
        self.nick = ""
        self.host = ""
        self.port = 0
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = ssl.wrap_socket(self.s)
        
    def connect(self, host, port, nick, channel):
        self.host = host
        self.port = int(port) 
        self.nick = nick
        self.channel = channel
        try:
            self.sock.connect((host, port))
            threading.Thread(target=self.listener).start()
            self.sock.send(bytes("USER "+self.nick+" "+self.nick+" "+self.nick+" nick\r\n", 'utf-8'))
            self.sock.send(bytes("NICK "+self.nick + "\r\n",'utf-8'))
            self.sock.send(bytes("JOIN "+self.channel +"\r\n",'utf-8'))
        except socket.error:
            print('Socket Error %s' % (socket.error))
            sys.exit()

    def listener(self):
        while(self.running):
            try:
                data = self.sock.recv(2048)
                if data:
                    msg = data.decode('utf-8')
                    print(msg)
                    if msg.find("PING :") != -1:
                        self.ping()
            except:
                return
        return

    def disconnect(self):
        self.running = False
        self.sock.close()
    
    def send(self, channel, msg):
        self.sock.send(bytes("privmsg "+ channel + " :" + msg + "\n",'utf-8'))

    def recv_data(self):
        data = self.sock.recv(2048)
        return data.decode('utf-8')
        #if data.find('PING') != -1:
        #     self.sock.send('PONG ' + data.split() [1] + 'rn')
    
    def ping(self):
        self.sock.send(bytes("PONG :pings\n", "utf-8"))
        print("reply to ping")
        return
