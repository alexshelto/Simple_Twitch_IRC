
import socket
import time
from datetime import datetime

from Logger import Logger

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
        self.irc = None 
        self.logger = None


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


    def view_chat(self,channel, log):
        print(f'Attempting to join: {channel}')

        need_reconnect = False # Made True if disconnected unintentionally 

        did_connect = self.connect_irc(f'#{channel}')
        if did_connect != True:
            print('failed to connect')
            return 
        
        self.logger = Logger(channel)


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

                        message = message.replace("\n", "")

                        #print(f'{time} | {username} | {message}')
                        color = '\033[1m\033[3m\033[38;5;21m'
                        print(f'<{color}{username}\033[m> {message}')

                        if log == True:
                            self.logger.data.append({'date': date, 'time': time, 'channel': channel, 'username': username, 'message': message})
                        
            # Socket disconnection
            except socket.error:
                print('lost connection, reconnecting')
                need_reconnect = True
                break

            # Keyboard interrupt to exit chat
            except KeyboardInterrupt:
                print('\n\nExiting Chat View\n\n')
                break
                
        #killing irc
        self.irc.close()
        self.irc = None                 

        #killing logger and saving data 
        if log == True:
            self.logger.write_to_file()
            self.logger = None

        if need_reconnect == True:
            self.view_chat(channel, log)
