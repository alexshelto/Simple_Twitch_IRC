
import socket



'''
HOST = 'irc.twitch.tv'
PORT = 6667
CHANNEL = '#soursweet'


#ircbot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IRC CLIENT irc://irc.chat.twitch.tv:6697

#server='irc://irc.chat.twitch.tv'
server='irc.chat.twitch.tv'
port=6667

BOT_USERNAME="be9ns"
OAUTH_TOKEN="oauth:xxycfz8i5f2dqav27mt9chngi705u7"


ircbot = socket.socket()
ircbot.connect((server,port))

ircbot.send(f"PASS {OAUTH_TOKEN}\n".encode('utf-8'))
ircbot.send(f"NICK {BOT_USERNAME}\n".encode('utf-8'))
ircbot.send(f"JOIN #nickmercs\n".encode('utf-8'))


while True:
    resp = ircbot.recv(2048).decode('utf-8')
    if resp.startswith('PING'):
        ircbot.send("PONG\n".encode('utf-8'))
    print(resp)
'''

if __name__ == '__main__':

