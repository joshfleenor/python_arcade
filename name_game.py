'''
Name Game:
This game will genrate an alis. I am using the random number genraitor to
determin the name in the dictionary
'''

import random

#New Name Dictionarys
new_First_Name = {1:'Red',2:'Orange',3:'Yellow',4:'Green',5:'Blue',6:'Inidigo',
                  7:'Vilot',8:'Pink'}

new_Last_Name = {1:'Apple',2:'Banana',3:'Orange',4:'Lemon',5:'Lime',6:'Cherry',
                 7:'Blue Berry',8:'Pineapple'}

new_Month = {1:'Tart',2:'Pie',3:'Sauce',4:'Cake',5:'Cookie',6:'Pudding',
             7:'Toffy',8:'Candy'}

#Simple Name Genaration: User input does not effect outcome in this version
def ng_Action1():
    input('First Letter of First Name: ')
    ran_num_1 = random.randrange(9)
    if ran_num_1 in new_First_Name:
        x = ran_num_1
        New_f_Name = new_First_Name[x]
        input('First Letter of Last Name: ')
        ran_num_2 = random.randrange(9)
        if ran_num_2 in new_Last_Name:
            y = ran_num_2
            New_l_Name = new_Last_Name[y]
            input('First Letter of Birth Month: ')
            ran_num_3 = random.randrange(9)
            if ran_num_3 in new_Month:
                z = ran_num_3
                n_Month = new_Month[z]
                print("\n")
                print('Here is your new Name')
                print(New_f_Name, New_l_Name, n_Month)
                print("\n")
             
def ng_Action2():
    action = input('Do you want to play again? y or n: ')
    Yes = 'y'
    No = 'n'
    if action == Yes:
        print("\n")
        Name_Game()
    elif action == No:
        print('Returning to main menu')
        exit
    else:
        print('I do not understand? Please Type a Y or N')
        ng_Action2()

#Opening Text

#Name Game Program
def Name_Game():
    print("\n")
    print('********** This is the Name Game **********')
    print("\n")
    ng_Action1()
    ng_Action2()