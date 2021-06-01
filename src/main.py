

from config import CONFIG
from IRC_BOT import IRC_BOT



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


def main() -> int:
    # Creating IRC bot instance
    irc = IRC_BOT(CONFIG['BOT_USERNAME'], CONFIG['OAUTH_TOKEN'])

    # Main Loop
    while True:
        try:
            user_choice = menu()
               
        except KeyboardInterrupt:
            break

        # View Chat from channel
        if user_choice == 0:
            channel = input('enter the twitch channel: ')
            irc.view_chat(channel.lower())

        elif user_choice == 1:
            channel = input('enter the twitch channel: ')
            irc.view_chat(channel.lower(), True)


        if user_choice == 3:
            break

    return 0


if __name__ == '__main__':
    exit(main())


    
