
import socket

# IRC CLIENT irc://irc.chat.twitch.tv:6697

server='irc.chat.twitch.tv'
port=6667


class IRC_BOT:
    def __init__(self, uname, oauth):
        self.username = uname
        self.oauth = oauth
        self.channel = ''
        #self.logging = logging
        self.irc = None 


    def connect_irc(self,channel):
        '''Function uses the passed in username, oauth, and channel to build a 
        connection to the twitch IRC to get the channel's chat feed'''

        self.irc = socket.socket()
        self.irc.connect((server, port))
        self.irc.send(f'PASS {self.oauth}\n'.encode('utf-8'))
        self.irc.send(f'NICK {self.username}\n'.encode('utf-8'))
        self.irc.send(f'JOIN {self.channel}\n'.encode('utf-8'))


    def view_chat(self,channel):

        print(f'Attempting to join: {channel}')
        self.connect_irc(channel)
        print(self.irc)

        while True:
            resp = self.irc.recv(2048).decode('utf-8')
            if resp.startswith('PING'):
                self.irc.send("PONG\n".encode('utf-8'))

            print(resp)
            '''
            try:
                resp = self.irc.recv(2048).decode('utf-8')
                if resp.startswith('PING'):
                    self.irc.send("PONG\n".encode('utf-8'))

                print(resp)

            except KeyboardInterrupt:
                print('\n\nExiting Chat View\n\n')
                self.irc = None
                break
            '''
        

    


