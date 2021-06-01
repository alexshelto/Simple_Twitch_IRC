
import socket
import time

# IRC CLIENT irc://irc.chat.twitch.tv:6667
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

        retry_time = 2 # seconds
        retry_count = 0
        try:
            self.irc = socket.socket()
            self.irc.connect((server, port))
            self.irc.send(f'PASS {self.oauth}\n'.encode('utf-8'))
            self.irc.send(f'NICK {self.username}\n'.encode('utf-8'))
            self.irc.send(f'JOIN {self.channel}\n'.encode('utf-8'))

            return True

        except ConnectionResetError:
            print(f'Could not connect, trying again in {retry_time} seconds')
            print('Check that you entered a valid channel name')

            time.sleep(retry_time)
            retry_time = retry_time ** 2
            retry_count += 1

            if retry_count == 8:
                return False

    def view_chat(self,channel):

        print(f'Attempting to join: {channel}')
        did_connect = self.connect_irc(channel)
        if did_connect != True:
            print('failed to connect')
            return 

        while True:
            try:
                resp = self.irc.recv(2048).decode('utf-8')
                if resp.startswith('PING'):
                    self.irc.send("PONG\n".encode('utf-8'))

                print(resp)

            except KeyboardInterrupt:
                print('\n\nExiting Chat View\n\n')
                self.irc = None
                break
        

    


