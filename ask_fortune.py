'''
I have built a simple fortune teller game based off of the "kissing frog" folded
paper toy from gradeschool. At this point it is returning a place holder fortune
I would like to make it dynamic based on a list obtained from a text doc that
can be updated easily. 
'''
#This function will determin what color group to display
def af_num_action():
    action1 = input('Now...Choose a number - 1, 2, 3, 4: ')
    if action1 == '1':
        print('Now Counting 1 ...')
        af_odd_color()
    elif action1 == '2':
        print('Now Counting 2...')
        af_even_color()
    elif action1 == '3':
        print('Now Counting 3...')
        af_odd_color()
    elif action1 == '4':
        print('Now Counting 4...')
        af_even_color()
    else:
        print('Enter a valid number')
        AskFortune()

#This function returns a "fortune" depending on the color chosen
def af_odd_color():
    action_1 = input('Choose a Color - Blue, Indigo, Violate, Pink: ')
    if action_1 == 'Blue':
        print('You are a Blue')
    elif action_1 == 'Indigo':
        print('You are a Indigo')
    elif action_1 == 'Violate':
        print('You are a Violate')
    elif action_1 == 'Pink':
        print('You are a Pink')
    else:
        print('Please chose a valid color')
        af_odd_color()
    
#This function returns a "fortune" depending on the color chosen
def af_even_color():
    action_2 = input('Choose a Color - Red, Orange, Yellow, Green: ')
    if action_2 == 'Red':
        print('You are a Red')
    elif action_2 == 'Orange':
        print('You are a Orange')
    elif action_2 == 'Yellow':
        print('You are a Yellow')
    elif action_2 == 'Green':
        print('You are a Green')
    else:
        print('Please chose a valid color')
        af_even_color()

#Play again or exit back to main menu
def af_play_again():
    action = input('Do you want to play again? y or n: ')
    Yes = 'y'
    No = 'n'
    if action == Yes:
        print("\n")
        AskFortune()
    elif action == No:
        print('Returning to main menu')
        exit
    else:
        print('I do not understand? Please Type a Y or N')
        af_play_again()


def AskFortune():
    print("\n")
    print('********** This is the Fortune Teller **********')
    print("\n")
    action = input('Lets Begin ... Chose a number - 1, 2, 3, 4: ')
    if action == '1':
        print('Counting 1...')
        af_num_action()
        af_play_again()          
    elif action == '2':
        print('Counting 2...')
        af_num_action()
        af_play_again()
    elif action == '3':
        print('Counting 3...')
        af_num_action()
        af_play_again()
    elif action == '4':
        print('Counting 4...')
        af_num_action()
        af_play_again()
    elif action == 'Exit':
        exit            
    else:
        print('Please Enter a Valid Number')
        AskFortune()


    

