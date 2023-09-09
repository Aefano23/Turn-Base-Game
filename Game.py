"""
Application of OOP on Code

Study Case : Turn base gameplay system for game

Description : 
This program is a turn base game. The player will control four heroes
to defeat the monster called Digital Lord

Purpose : Applying OOP to a 4 vs 1 turn base game program

Author : Aditya Efano Putra

This is the main program. run this code to play the game
"""

import os
import Gamedata as Gamedata
import time

if __name__ == "__main__": 

    #matching the os for clearing the terminal
    operating_system = os.name
    while (True):
        match operating_system:
            case "posix" : os.system('clear')
            case "nt" : os.system('cls')

        #Game title
        Title = "DIGITAL REALM".center(23)
        print(" "+Title+" ")
        print('=========================')

        #List of available input.
        print('Are you brave enough to fight the Digital Lord?')
        print(f"1. Challenge!")
        print(f"2. Run!\n")

        user_option = input("Select action: ") #take input from user.

        #match the user's input to the available option
        match user_option:
            case '1': Gamedata.arena()
            case '2':
                exit = input("Are you sure want to run without trying? (y/n): ")
                if exit.lower() == 'y':
                    print("\nFAREWELL\n")
                    break
            case _:
                print('Invalid Input')
                time.sleep(1)
       
                    
   
