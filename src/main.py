
import argparse

from config import CONFIG
from IRC_BOT import IRC_BOT



'''


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



options = ['View Chat From Channel', 'View & Log Chat From Channel', 'Exit']
def menu():
    print('#'* 15 + ' MENU ' + '#' * 15)
    for idx, option in enumerate(options):
        print(f'[{idx}] : {option}')
    print('#'* 18  + '#' * 18)

    try:
        choice = input('Select what you would like to do: ')

        if not 0 <= int(choice) < len(options):
            print('not a valid option')
            menu()

    except ValueError:
        print('not a valid option')
        menu()


    return int(choice)


def get_channel_name() -> str:
    channel_name = input('enter the twitch channel to join: ')
    return f'#{channel_name.lower()}'


def main() -> int:
    # Command Line arguments
    parser = argparse.ArgumentParser()
    # parser.add_argument('channel', help='Channel To Join') 
    parser.add_argument(
            '-l', '--log', '--logging', default=False, help='Enableing logging will log each chat sent to channel in txt file'
            )

    args = parser.parse_args() # parsing arguments

    if args.log != False:
        args.log = True
    
    #def __init__(self, uname, oauth, logging):
    irc = IRC_BOT(CONFIG['BOT_USERNAME'], CONFIG['OAUTH_TOKEN'])


    # Main Loop
    while True:
        try:
            user_choice = menu()
               
        except KeyboardInterrupt:
            break

        # View Chat from channel
        if user_choice == 0:
            channel = get_channel_name()
            irc.view_chat(channel)

        if user_choice == 3:
            break


    return 0


if __name__ == '__main__':
    exit(main())


    
