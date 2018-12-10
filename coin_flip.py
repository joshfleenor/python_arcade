import random

def cf_Action2():
    Yes = 'y'
    No = 'n'
    action = input('Do you want to play again? y or n: ')
    if action == Yes:
        print("\n")
        Coin_Flip()
    elif action == No:
        print('Returning to main menu')
        exit
    else:
        print('I do not understand? Please Type a Y or N')
        cf_Action2()

def comment():
    print('\n''...',random.choice(['interesting','I did not expect that','how odd','really?...ok then','I see']),'...')


def head_choice():
    comment()
    coin_flip = random.choice(['heads','tails'])
    print('\n')
    print('it is...',coin_flip)
    if coin_flip == 'heads':
        print('It is heads! You got that right!')
        cf_Action2()
    elif coin_flip == 'tails':
        print('I am sorry you chose heads you loose!')
        cf_Action2()
    else:
        print('please enter a 1 or 2')
        Coin_Flip()

def tail_choice():
    comment()
    coin_flip = random.choice(['heads','tails'])
    print('\n')
    print('it is...',coin_flip)
    if coin_flip == 'tails':
        print('It is tails! You got that right!')
        cf_Action2()
    elif coin_flip == 'heads':
        print('I am sorry you chose tails you loose!')
        cf_Action2()
    else:
        print('please enter a 1 or 2')
        Coin_Flip()


def Coin_Flip():
    print('************ Welcome ************')
    print('****** How Lucky Are You? ******')
    print('\nHeads or Tails the choise is yours...')
    
    action = input('\nChoose 1 for heads or 2 for tails ')
    
    if action == '1':
        head_choice()
        
    elif action == '2':
        tail_choice()
        
    else:
        print('please enter a 1 or 2')
        Coin_Flip()
        
