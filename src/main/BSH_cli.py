# Main command-line UI for Buy Sell Hold

from technical_indicators import moving_averages

'''
Displays a menu depending on type

type: The type of menu to display (main, ticker, strategy choosing)
'''
def display_menu(type):
    if type == "main":
        # Display Menu
        print('##########################')
        print('######## Main Menu #######')
        print('##########################\n')

        # Menu Options
        print('1. Begin Strategy')
        print('2. Quit')

        # prompt for input
        #print('\nEnter a number to make a choice...')

'''
Prompts the user for menu input and returns appropriate value
after type casting if necessary

type: type of input to accept from user (menu option, ticker)
'''
def get_input(type):
    if type == "menu option":
        # accept menu input (always a number)
        # Try/Except to verify input is convertible to an integer
        try:
            return int(input("Enter a menu option: "))
        except ValueError:
            print("Error: Menu option must be a number")
            return get_input(type)
    elif type == "ticker":
        # accept ticker; always a string
        return input("Enter a valid ticker symbol: ")
    else:
        # Do sometihng else; throw an error?
        return "NA"

'''
Processes menu input from user

user_input: 
'''
def process_menu_input(user_input):
    return
'''
Process ticker input from user

user_input:
'''
def process_ticker_input(user_input):
    return
'''
Sends user input to the proper processing function

user_input: either an int or str depending on type of input
'''
def process_input(user_input):
    if type(user_input) is int:
        # process menu input
        process_menu_input(user_input)
    elif type(user_input) is str:
        # process ticker input
        process_ticker_input(user_input)
    else:
        # Do something else; throw an error?
        return "NA"

# Display welcome message
print('Welcome to Buy Sell Hold!')

# Display main menu and prompt for user input
display_menu("main")

# process input and go to sub-menu
user_input = get_input("menu option")
process_input(user_input)

# Beep Boop Do Compute
# Display results