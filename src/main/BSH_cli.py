# Main command-line UI for Buy Sell Hold

from technical_indicators import moving_averages

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
        print('\nEnter a number to make a choice...')

def get_input(type):
    if type == "menu option":
        # accept menu input (always a number)
        return int("")
    elif type == "ticker":
        # accept ticker; always a string
        return ""
    else:
        # Do sometihng else; throw an error?
        return ""

def process_input(user_input):
    if type(user_input) is int:
        # process menu input
    elif type(user_input) is str:
        # process ticker input
    else:
        # Do something else; throw an error?
# Display welcome message
print('Welcome to Buy Sell Hold!')

# Display main menu and prompt for user input
display_menu("main")

# process input and go to sub-menu
user_input = get_input("menu option")

# Beep Boop Do Compute
# Display results