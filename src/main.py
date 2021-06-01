
import socket

from dotenv import dotenv_values

config = dotenv_values(".env") # Loading enviornment vars form .env file



HOST = 'irc.twitch.tv'
PORT = 6667
CHANNEL = '#soursweet'


#ircbot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IRC CLIENT irc://irc.chat.twitch.tv:6697

#server='irc://irc.chat.twitch.tv'
server='irc-ws.chat.twitch.tv'
port='6697'


ircbot = socket.socket()
ircbot.connect((server,int(port)))
ircbot.send(f"PASS {config['OAUTH_TOKEN']}\n".encode('utf-8'))
ircbot.send(f"NICK {config['BOT_USERNAME']}\n".encode('utf-8'))
ircbot.send(f"JOIN #soursweet\n".encode('utf-8'))


resp = ircbot.recv(2048).decode('utf-8')
print(resp)

'''
ircbot.send(f'PASS {config["OAUTH_TOKEN"]}')
ircbot.send(f'NICK {config["BOT_USERNAME"]}')
'''
