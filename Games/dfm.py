##############################################
# Name: Rehan Jetha
# Course: ICS3U
# File: dfm.py
# Description: Play a spinoff of rock, paper, scissors!
# History:
# 2023.3.21 - Creation
# 2023.3.22 - Completion
# 2023.5.26 - Began Arcade Revision
# 2023.5.28 - Completed Arcade Revision
##############################################

import random
import time

from Control.buttons import enableButtons
from Control.coins import updateCoins, getCoins

#########################################################
# FCN NAME: game_logic
# DESCRIPTION: Crunches user input in relation to randomly generated #
# INPUTS: user's choice
# OUTPUTS: end result, win or loss + what computer & player chose
# ALGORITHM:
#   GENERATE random int from 1-3, inclusive
#   REPLACE any lingering spaces in user choice with strip()
#   IF choice is to exit:
#       RETURN exit
#   ENDIF
#   TRY:
#       CONVERT user choice to integer
#       DECREMENT player choice by 1
#       DECREMENT computer choice by 1
#   EXCEPT:
#       RETURN not_num
#   ENDTRYEXCEPT
#   IF player choice is equal to computer choice:
#       RETURN draw
#   ELIF player choice equals 0 (duck):
#       IF computer choice equals 1 (fish):
#           RETURN user win, computer's selection, and player's selection
#       ELSE:
#           RETURN computer win and selections
#       ENDIF
#   ELIF player choice equals 1 (fish):
#       IF computer choice equals 2 (mosquito):
#           RETURN user win, computer's selection, and player's selection
#       ELSE:
#           RETURN computer win and selections
#       ENDIF
#   ELIF player choice equals 2 (mosquito):
#       IF computer choice equals 0 (duck):
#           RETURN user win, computer's selection, and player's selection
#       ELSE:
#           RETURN computer win and selections
#       ENDIF
#   ELSE:
#       RETURN out of range
#   ENDIF
#       
# HISTORY: 
#          2023.3.21 - Creation
#          2023.3.22 - Finished Pseudocode + game_logic
#          2023.5.28 - Completed Arcade Revision
########################################################

# 1 beats 2, 2 beats 3, 3 beats 1 ---- note that this will be decremented by 1 in the actual code to account for zero based numbering
def game_logic(player_choice):

    comp_choice = random.randint(1, 3) - 1  # generate computer's random int (1,3) inclusive, subtract 1 to account for tuple index (instead of generating from 0,2)
    player_choice = player_choice.strip()  # remove any accidental user spaces

    if (player_choice.lower() == "exit"):
        return "exit" # return exit
    
    try:
        player_choice = int(player_choice)  # convert choice to int
        player_choice -= 1  # decrement player choice for use with tuple
    except:
        return "not_num"  # return not_num
    
    if (player_choice == comp_choice):  # same move
        return "draw", comp_choice, player_choice # return draw, comp_choice, and player_choice
    elif (player_choice == 0):  # player chooses duck
        if (comp_choice == 1):  # comp chooses fish
            return "usr_win", comp_choice, player_choice  # return usr_win, comp_choice, and player_choice
        else:  # comp chooses mosquito
            return "comp_win", comp_choice, player_choice  # return comp_win, comp_choice, and player_choice
    elif (player_choice == 1):  # player chooses fish
        if (comp_choice == 2):  # comp chooses mosquito
            return "usr_win", comp_choice, player_choice  # return usr_win, comp_choice, and player_choice
        else:  # comp chooses duck
            return "comp_win", comp_choice, player_choice  # return comp_win, comp_choice, and player_choice
    elif (player_choice == 2):  # player chooses mosquito
        if (comp_choice == 0):  # comp chooses duck
            return "usr_win", comp_choice, player_choice  # return usr_win, comp_choice, and player_choice
        else:  # comp chooses fish
            return "comp_win", comp_choice, player_choice  # return comp_win, comp_choice, and player_choice
    else:
        return "out_of_range"  # return out_of_range   

#########################################################
# FCN NAME: duckFishMosquitoGame
# DESCRIPTION: Play duck, fish, mosquito
# INPUTS: usr, buttons, display
# OUTPUTS: game, new coins
# ALGORITHM:
#           GET current coins
#           DEFINE GAME_INSTRUCTIONS as constant for game instructions
#           DEFINE GAME_OPTIONS as constant tuple for options
#           PRINT exit instructions
#           PRINT rules
#           PRINT possible coin rewards
#           PRINT personal aesthetic touch + name of usr
#           DEFINE end_game as a variable set to False
#           WHILE end_game remains False:
#
#           IF (coins are less than or equal to 0):
#               PRINT out of coins
#               REDEFINE coins to 1000
#               enableButtons(buttons)
#               updateCoins(usr, coins)
#               RETURN
#           ENDIF
#
#           PRINT game instructions constant
#           INPUT user's selection
#           CALL game_logic() and define as ret value var
#           SLEEP program for 0.5 seconds for anticipation
#           IF ret value says to exit:
#               PRINT "Thanks for playing!"
#               enableButtons(buttons)
#               updateCoins(usr, coins)
#               RETURN
#           ELIF ret_value says not_num:
#               PRINT not valid integer
#           ELIF ret_value says draw:
#               PRINT draw
#               PRINT user selection
#               PRINT comp selection
#           ELIF ret_value says user wins:
#               PRINT user win
#               ADD 200 to coins
#               PRINT user selection
#               PRINT comp selection
#               PRINT coin victory + current purse
#           ELIF ret_value says computer wins:
#               PRINT computer win
#               SUBTRACT 100 from coins
#               PRINT user selection
#               PRINT comp selection
#               PRINT coin loss + current purse
#           ELIF ret_value says out of range:
#               PRINT not integer error msg
#           ENDIF
#   
# HISTORY: 2023.3.21 - Creation
#          2023.3.22 - Completion
#          2023.5.28 - Finished Arcade Revision
########################################################

def duckFishMosquitoGame(usr, buttons, display):

    coins = getCoins(usr)  # get current coins 

    GAME_INSTRUCT = "\n|========== Duck (1), Fish (2), Mosquito (3), exit ==========|\n"  # set constant instructions variable
    GAME_OPTIONS = ("Duck", "Fish", "Mosquito")  # set constant options variable, note that to access you must subtract 1 from user choice

    print("At any time in the game, type \"exit\" to quit the game.\n")  # game instructions
    print("The rules are simple:\nduck eats fish, fish eats mosquito, mosquito stings duck and kills duck by infecting it with West Nile disease.")  # rules
    print("Win = +200, Loss = -100, Draw = 0")  # print coin rewards
    print(f"Alright {usr} here are your choices:")  # added personal touch for aesthetics

    end_game = False  # declare end_game variable to allow for the subsequent loop to end

    while not(end_game):
        if (coins <= 0):
            print("Game over, you're out of coins!")  # game over
            coins = 1000  # reset coins to 1000
            enableButtons(buttons)  # enable buttons
            updateCoins(usr, coins, display)  # write new coins to JSON
            return  # close fnc
        print(GAME_INSTRUCT)  # print game options
        usr_choice = input("Enter your # of choice: ")  # look for user's choice
        ret_value = game_logic(usr_choice)  # call game_logic function with the user's choice as an input
        time.sleep(0.5)  # slight delay for anticipation
        if (ret_value == "exit"):
            print("Thank you for playing!")  # print end message
            enableButtons(buttons)  # enable buttons
            updateCoins(usr, coins, display)  # write new coins to JSON
            return  # close fnc
        elif (ret_value == "not_num"):
            print("That is not a valid integer.")  # print user error
        elif (ret_value[0] == "draw"):
            print("It's a draw!")  # print draw message
            print(f"You chose {GAME_OPTIONS[ret_value[2]]}")  # print user choice
            print(f"I chose {GAME_OPTIONS[ret_value[1]]}")  # print computer choice
        elif (ret_value[0] == "usr_win"):
            print("You WIN!")  # print user wins
            coins += 200  # add 200 coins
            print(f"You chose {GAME_OPTIONS[ret_value[2]]}")  # print user choice
            print(f"I chose {GAME_OPTIONS[ret_value[1]]}")  # print computer choice
            print(f"+200 Coins. Your current purse is {coins}.")  # indicate coins won & current coins
        elif (ret_value[0] == "comp_win"):
            print("You lose.")  # print user loses
            coins -= 100  # remove 100 coins
            print(f"You chose {GAME_OPTIONS[ret_value[2]]}")  # print user choice
            print(f"I chose {GAME_OPTIONS[ret_value[1]]}")  # print computer choice
            print(f"-100 Coins. Your current purse is {coins}.")  # indicate coins won & current coins
        elif (ret_value == "out_of_range"):
            print("That is not an integer from 1-3.")  # print user error