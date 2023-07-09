class Menu:
    '''
    The menu base class for BSH.

    Responsible for menu display and processing user input
    '''
    def display():
        '''
        Displays menu options and prompts

        THIS MEHTOD IS INTENDED TO BE OVERRIDDEN IN SUBCLASSES
        '''
        raise NotImplemented
    def get_input():
        '''
        Recieve and validate user input

        THIS MEHTOD IS INTENDED TO BE OVERRIDDEN IN SUBCLASSES
        '''
        raise NotImplemented
    def process_input():
        '''
        Call apropriate functionality depending on input

        THIS MEHTOD IS INTENDED TO BE OVERRIDDEN IN SUBCLASSES
        '''
        raise NotImplemented
    
class Main_Menu(Menu):
    def display():
        # Display Menu
        print('##########################')
        print('######## Main Menu #######')
        print('##########################\n')

        # Menu Options
        print('1. Begin Strategy')
        print('2. Quit')

    def get_input(self):
        try:
            return int(input("Enter a menu option: "))
        except ValueError:
            print("Error: Menu option must be a number")
            return self.get_input()
        
    def process_input(self, user_input):
        if self.user_input is 1:
            # process begin strategy select
        else:
            # quit