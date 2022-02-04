import random
import signal

signal.signal(signal.SIGINT, signal.SIG_IGN) # teehee

### Crude welcome screen
def welcome():
    print('welcome to hackman')
    print('my shift key is broken, but let\'s just call it an aesthetic')
    print()

### Crude help menu
def help():
    print('help          bring up the help menu')
    print('start         start game of hangman')
    print('              --strikes X  number of "lives" that you have, default=7')
    print('              --length X   length of word to be guessed, default=random')
    print('quit          if you really want to...')
    print()

### Validate input
def input_val(cmd):
    try:
        strikes_index = cmd.index('--strikes')
    except:
        strikes_index = -1

    if strikes_index >= 0:
        try:
            strikes = int(cmd[strikes_index + 1])
        except:
            print('Error parsing strikes')
            raise Exception()
    else:
        strikes = 7 # this could be a config item

    # Parse out length of word
    try:
        length_index = cmd.index('--length')
    except:
        length_index = -1

    if length_index >= 0:
        try:
            length = int(cmd[length_index + 1])
        except:
            print('Error parsing length')
            raise Exception()
    else:
        length = random.randint(3, 12) # this could be a config item?

    return strikes, length

### Make API call using API defined in .config[api] (make it yourself)
def get_word(length):
    return None

### Game logic
def play_game(strikes, length):
    print(f"you tried to play agaim with {strikes} strikes and {length} letter word")
    print('not implemented yet but thanks for your interest')

def main():
    # Config file validation

    # Welcome menu
    welcome()
    help()

    # Start CLI
    while True:
        try:
            cmd = input('MENU > ').lower().split()
        except:
            cmd = ['<Ctrl + C>']

        if cmd[0] == 'help':
            help()
        elif cmd[0] == 'quit':
            exit()
        elif cmd[0] == 'start':
            # Parse out number of strikes/lives
            try:
                strikes, length = input_val(cmd)
            except:
                continue

            # Initiate game
            play_game(strikes, length)

            # Done
            print('Thanks for playing! Feel free to select a game again or type `quit` to leave the program.')

        else:
            print(f'invalid command: {cmd[0]}, type `help` for the help menu')


if __name__ == '__main__':
    main()