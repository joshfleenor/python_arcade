'''
Fleenor Arcade -
I have built the Fleenor Arcade to dempinstrate my knowlidge with basic python
programing.
I am adding gmes as I write them in there seprate modules.
Name Game added 9/3/18
Ask Fortune Teller 9/5/18
Coin Flip 9/17/18
I plan to add a "User" function that tracks
tokins,
tickets,
and a ticket redemption shop that is stored in txt files for easy recall
'''
#Game Module Imports
import name_game
import ask_fortune
import coin_flip


def main():
    print('''
    Welcome to The Fleenor Arcade

    Chose your game
    [1] - Name Game
    [2] - Ask fortune teller
    [3] - Dice
    [4] - Coin Flip
    [5] - Exit
    ''')

    action = input("What would you like ot play?(Enter a Number): ")

    if action == '1':
        name_game.Name_Game()
        main()
    elif action == '2':
        ask_fortune.AskFortune()
        main()
    elif action == '3':
        print('Coming Soon')
        main()
    elif action == '4':
        coin_flip.Coin_Flip()
        main()
    elif action == '5':
        print('''Thank you for your time. We hope to see you again at the Fleenor
              Arcade''')
        exit
    else:
        print('No Valid choice was made please try again')
        main()

main()
