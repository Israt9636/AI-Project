import random                                # For random suggestions

import sys

from random import sample

import os           # For clearing Terminal

from time import sleep      # Default time = 3 Seconds



font_list = ['big']
random_font = random.sample(font_list, 1)

try:    # Optional for style, importing pyfiglet module
    from pyfiglet import Figlet
    f = Figlet(font='{}'.format(*random_font))
    print(f.renderText('Merryweather Cheesecake'))
except ImportError or ModuleNotFoundError:
    pass



random_choice = ["Bread cheesecakes", "No egg cheesecakes", "Low amount cheese cheesecakes", 'Egg cheesecakes', 'Cappucino']     # If something is unavailable orfor suggesting random things

cart = []


new_list = []


def limit():             # If order exceeds the 10 item limit
    cls()
    print('Sorry you cannot order more than 10 items.')
    sleep(3)


def cls():

    if sys.platform.startswith('win32' or 'win64' or 'win86'):
        os.system('cls')
    else:
        os.system('clear')




    
def limit_reached():        # When you cannot order more items
    cls()
    print('Sorry it looks like you have reached the maximum limit of ordering this item. Maybe you can try something else. \n')
    order()


    
def get_name(shop_name = 'Coffee Express'):
    name = input("Can I have your name please?\n\n> ")
    name1 = name.title()
    cls()
    
    if len(name1) > 0 and not name1.isdigit():
        print("Hello {}, welcome to {}." .format(name1, shop_name))
        print('')

        
    elif len(name1) == 0:
        print('Error, name empty.')
        get_name()

        
    elif name1.isdigit():
        print('Please enter only Alphabets.')
        print('')
        get_name()

        
    else:
        print('')
        print('Sorry, I do not understand.')
        print('')
        get_name()

 