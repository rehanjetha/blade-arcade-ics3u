##############################################
# Name: Rehan Jetha
# Course: ICS3U
# File: highlow.py
# Description: Arcade Highlow Game
# History:
# 2023.4.11 - Creation
# 2023.4.15 - Completion
# 2023.5.26 - Began Arcade Revision
# 2023.5.27 - Finished Arcade Revision
##############################################

import random 
import time 

from Control.buttons import enableButtons
from Control.coins import updateCoins, getCoins

#########################################################
# FCN NAME: evaluateBet
# DESCRIPTION: Generates bet # and evaluates user win/loss
# INPUTS: user choice (high/low)
# OUTPUTS: win/loss
# ALGORITHM:
#           GENERATE random integer between 1-13 (inclusive) equal to "bet_num"
#
#           IF (choice == "h"):
#               REDEFINE choice to "high"
#           ELIF (choice == "l"):
#               REDEFINE choice to "low"
#           ENDIF
#
#           DEFINE constant "USR_LOSS" as comp win fstring
#
#           IF (bet_num equals 7):
#               PRINT usr_loss
#               RETURN "usr_loss", bet
#           ELIF (bet_num is less than 7 and user choice is "high"):
#               PRINT usr_loss
#               RETURN "usr_loss", bet
#           ELIF (bet_num is greater than 7 and user choice is "low"):
#               PRINT usr_loss
#               RETURN "usr_loss", bet
#           ELSE:
#               PRINT "You win with number {bet_num} since you chose {choice}"
#               RETURN "usr_win", bet times two
#           ENDIF
#
# HISTORY: 
# 2023.4.11 - Creation
# 2023.4.11 - Completion of Pseudocode
# 2023.4.11 - Completion of Python code + stub
# 2023.4.11 - Removed stub to integrate properly
# 2023.4.12 - Slightly edited msg for better aesthetics
# 2023.4.12 - Changed if condition to "h" and "l" for faster betting
# 2023.4.12 - Completion
# 2023.5.26 - Began Arcade Revision
# 2023.5.27 - Finished Arcade Revision
########################################################

def evaluateBet(choice):

    bet_num = random.randint(1, 13)  # generate random # between 1-13, inclusive

    if (choice == "h"):
        choice = "high"  # set choice to high
    elif (choice == "l"):
        choice = "low"  # set choice to low

    USR_LOSS = f"I win. I rolled the number {bet_num}, and you chose \"{choice}\" :(" # create constant string for usr_loss msg

    if (bet_num == 7):
        print(USR_LOSS)  # print loss msg
        return "usr_loss"  # return usr_loss and bet to main
    elif (bet_num < 7 and choice == "high"):
        print(USR_LOSS)  # print loss msg
        return "usr_loss"  # return usr_loss and bet to main
    elif (bet_num > 7 and choice == "low"):
        print(USR_LOSS.format(bet_num=bet_num, choice=choice))  # print loss msg
        return "usr_loss"  # return usr_loss and bet to main
    else:
        print(f"You win! I rolled the number {bet_num}, and you chose \"{choice}.\"")  # print win msg
        return "usr_win"  # return usr_win and bet times two to main

#########################################################
# FCN NAME: highlowGame
# DESCRIPTION: prompts for inputs to pass through to evaluateBet()
# INPUTS: usr, buttons, display
# OUTPUTS: 
# ALGORITHM:
#           DEFINE coins as getCoins(usr)
#           DEFINE constant GAME_OVER message with ASCII art
#           PRINT rules
#           
#           PRINT aesthetic opening msg
#
#           DEFINE end_game as flag for main loop, set to False
#           WHILE not(end_game):
#               DEFINE valid_bet as flag for bet loop, set to False
#               WHILE not (valid_bet):
#                   PROMPT for bet_amt
#                   TRY:
#                       CONVERT bet_amt to int
#                   EXCEPT:
#                       PRINT error, not whole bet
#                       CONTINUE to next iteration
#                   ENTRY
#                   IF (bet_amt is less than or equal to 0):
#                       PRINT error, must bet pos ints
#                   ELIF (bet_amt is greater than coins):
#                       PRINT error, not enough coins
#                   ELSE:
#                       REDEFINE valid_bet to True to end loop
#                   ENDIF
#               ENDWHILE
#               
#               DEFINE valid_choice as flag for Hi/Lo loop, set to False
#               WHILE not(valid_choice):
#                   PROMPT for usr_choice of Hi/Lo
#                   REMOVE spaces & CONVERT usr_choice to lowercase
#                   IF (usr_choice is high) or (usr_choice is low):
#                       REDEFINE valid_choice to True to end loop
#                   ELSE:
#                       PRINT error, choose Hi/Lo
#                   ENDIF
#               ENDWHILE
#               
#               DEFINE aesthetic dots as [".", "..", "...", " "]
#               DEFINE end_anim_counter at 0 to act as timer counter
#               
#               DEFINE end_animation as flag for animation loop, set to False
#               PRINT dealing, end on beginning of line
#               WHILE not(end_animation):
#                   FOR each dot in dots:
#                       PRINT blank line, end of beginning of line
#                       PRINT dealing{dot}
#                       SLEEP program for 0.2 sec
#                   ENDFOR
#                   INCREMENT end_anim_counter
#                   IF (end_anim_counter reaches 4):
#                       PRINT erase previous line, print new line
#                       PRINT number dealt statement
#                       REDEFINE end_animation flag to True
#                   ENDIF
#               ENDWHILE
#               PRINT new line and aesthetic header made of equal signs
#               
#               CALL evaluateBet and save as bet_result, pass usr_choice
#               
#               IF (bet_result returns usr_loss):
#                   SUBTRACT bet_amt from coins
#                   PRINT you lost, how much lost, and new coins msg
#               ELIF (bet_result returns usr_win):
#                   ADD bet_amt to coins
#                   PRINT you win, how much won, and new coins msg
#               ENDIF
#               PRINT aesthetic footer made of equal signs
#
#               IF (coins is less than or equal to 0):
#                   PRINT you've lost msg
#                   PRINT game over msg with usr's name
#                   REDEFINE coins to 1000
#                   enableButtons(buttons)
#                   updateCoins(usr, coins, display)
#                   RETURN
#               ENDIF
#               
#               DEFINE valid_end as flag for play again loop, set to False
#               WHILE not(valid_end):
#                   PROMPT for valid_end_resp of y/n
#                   REMOVE spaces & CONVERT valid_end_resp to lowercase
#                   
#                   IF (valid_end_resp says "n"):
#                       PRINT game over msg with usr's name
#                       REDEFINE coins to 1000
#                       enableButtons(buttons)
#                       updateCoins(usr, coins, display)
#                       RETURN
#                   ELIF (valid_end_resp says "y"):
#                       REDEFINE valid_end flag to True to end this loop
#                   ELSE:
#                       PRINT not valid response msg
#
# HISTORY: 
# 2023.4.11 - Creation
# 2023.4.12 - Added high_score counter + QOL's
# 2023.4.12 - Converted continue statements to nested loops
# 2023.4.12 - Added animation for "dealing..." aesthetics + others
# 2023.4.12 - Rigorously tested for bugs and conducted a beta test
# 2023.4.12 - Adjusted Pseudocode to reflect extra aesthetic changes
# 2023.4.15 - Added some cool ASCII art, fixed remaining bugs
# 2023.4.15 - Completion
# 2023.5.26 - Added to Summative
# 2023.5.26 - Removed high score functionality
# 2023.5.26 - Converted program into function
# 2023.5.27 - Finished Arcade Revision
########################################################

def highlowGame(usr, buttons, display):

    coins = getCoins(usr)  # get current coins

    GAME_OVER = '''
     ____                         ___                 _ 
    / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __| |
   | |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__| |
   | |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |  |_|
    \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|  (_) \n
                Thanks for playing, {user}!                                               
'''  # game over ascii art

    print("\nThe computer will roll between 1-13, inclusive. You win if you guess correctly whether the number is higher or lower than 7.\n")  # print rules

    print("\n~ Hello! Welcome to Blade Arcade High Low Casino ~ ")  # aesthetic opening


    end_game = False  # make loop's True/False flag

    while not(end_game):  # HiLo loop

        valid_bet = False  # set bet's True/False flag
        
        while not(valid_bet):
            bet_amt = input(f"Your current purse is {coins}.\n{usr}, how much would you like to wager: ")  # prompt for bet amt
            
            try:
                bet_amt = int(bet_amt)  # convert bet_amt to integer
            except:
                print("You didn't make a whole bet!")  # throw error, not int
                continue  # start next iteration  
            if (bet_amt <= 0):
                print("You must bet actual coins (positive integers)!")  # throw error, positive int needed
            elif (bet_amt > coins):
                print("You don't have that many coins to bet!")  # throw error, not enough coins
            else:
                valid_bet = True  # end loop by setting valid_bet to True

        valid_choice = False  # set choice's True/Flase flag

        while not(valid_choice):
            usr_choice = input(f"\n{usr}, would you like to choose \"high\" (h) or \"low\" (l)? ")  # user's choice of high or low
            usr_choice = usr_choice.strip().lower()  # remove lingering spaces from usr_choice and convert to lowercase

            if (usr_choice == "high") or (usr_choice == "low") or (usr_choice == "h") or (usr_choice == "l"):
                valid_choice = True  # end loop, valid choice given
            else:
                print("Please choose either \"high\" (h) or \"low\" (l)!")  # throw error, not high or low

        dots = [".", "..", "...", " "]  # make dots for dealing aesthetic
        end_anim_counter = 0  # make a counter to act as timer counter

        end_animation = False  # make active animation flag for dealing aesthetic

        print("⚄Dealing", end="\r")  # aesthetic anticipation inducing msg
        while not(end_animation):

            for dot in dots:
                print("               ", end="\r")  # use 9 spaces to completely clear previous line
                print(f"⚄Dealing{dot}", end="")  # print dots
                time.sleep(0.2)  # sleep for 0.2 sec

            end_anim_counter += 1  # increment end animation counter

            if (end_anim_counter == 4):
                print("\r                      ", end="\n")  # erase previous line, make new line
                print("Number has been dealt.")  # replace dealing statement at end of roll
                end_animation = True  # end loop by setting flag to True

        print("\n===================================================")  # aesthetic container opener for gambling results

        bet_result = evaluateBet(usr_choice)  # call evaluateBet() function, pass usr_choice
        
        if (bet_result == "usr_loss"):
            coins -= bet_amt  # subtract bet_amt from user's coins if loss
            print(f"-{bet_amt} coins\nYour new score is {coins}.")  # output current score

        elif (bet_result == "usr_win"):
            coins += bet_amt  # subtract initial bet from user's coins
            print(f"+{bet_amt * 2} coins\nYour new score is {coins}.")  # output current score

        print("===================================================")  # aesthetic container footer for gambling results

        if (coins <= 0):
            print("\nYou've been cleaned out.")  # not enough coins msg
            print(GAME_OVER.format(user=usr))  # print game over ascii with high score
            coins = 1000  # reset user coins to 1000
            enableButtons(buttons)  # enable tkinter buttons
            updateCoins(usr, coins, display)  # update coins to JSON
            return  # close fnc

        valid_end = False  # set end's True/False flag
        
        while not(valid_end):
            valid_end_resp = input("Would you like to continue? y/n ")  # prompt user to continue or not
            valid_end_resp = valid_end_resp.strip().lower()  # remove lingering spaces and convert everything to lowercase
        
            if (valid_end_resp == "n"):
                print(GAME_OVER.format(user=usr))  # print game over ascii with high score
                enableButtons(buttons)  # enable tkinter buttons
                updateCoins(usr, coins, display)  # update coins to JSON
                return  # close fnc
            elif (valid_end_resp == "y"):
                valid_end = True  # close valid end loop
            else:
                print("That is not a valid response! Please choose y/n.")  # not valid response msg
            
