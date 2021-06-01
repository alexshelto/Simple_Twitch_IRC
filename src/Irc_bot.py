
import socket
import time
from datetime import datetime


# IRC CLIENT irc://irc.chat.twitch.tv:6667
server='irc.chat.twitch.tv'
port=6667


def parse_chat_msg(msg) -> str:
    # Ex message
    # :matikss321!matikss321@matikss321.tmi.twitch.tv PRIVMSG #shroud :how do you like it shroud?
    username = msg.split('!')[0][1:]
    message = msg.split(':',3)[2]

    return username, message


class IRC_BOT:
    def __init__(self, uname, oauth):
        self.username = uname
        self.oauth = oauth
        #self.channel = ''
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
            self.irc.send(f'JOIN {channel}\n'.encode('utf-8'))

            return True

        except ConnectionResetError:
            print(f'Could not connect, trying again in {retry_time} seconds')
            print('Check that you entered a valid channel name')

            time.sleep(retry_time)
            retry_time = retry_time ** 2
            retry_count += 1

            if retry_count == 8:
                return False

    def view_chat(self,channel, log=False):
        print(f'Attempting to join: {channel}')
        did_connect = self.connect_irc(channel)
        if did_connect != True:
            print('failed to connect')
            return 

        while True:
            try:
                resp = self.irc.recv(2048).decode('utf-8')

                # Twitch IRC occasionally sends ping to check you are still active
                if resp.startswith('PING'):
                    self.irc.send("PONG\n".encode('utf-8'))

                else:
                    if 'PRIVMSG' in resp:
                        now = datetime.now()
                        date = now.strftime("%m/%d/%Y")
                        time = now.strftime("%H:%M:%S")

                        username, message = parse_chat_msg(resp)
                        print(f'{time} | {username} | {message}')

            except KeyboardInterrupt:
                print('\n\nExiting Chat View\n\n')
                self.irc = None
                break


    


