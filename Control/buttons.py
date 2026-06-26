##############################################
# Name: Rehan Jetha
# Course: ICS3U
# File: buttons.py
# Description: Contains button related functions
# History:
# 2023.5.26 - Creation
# 2023.5.27 - Completion
##############################################

import tkinter
from tkinter import messagebox

from Control.coins import coinsPriceMet, getCoins
from Games.gameboy import gameboyEmulator

#########################################################
# FCN NAME: enableButtons
# DESCRIPTION: Enables all buttons after game
# INPUTS: buttons
# OUTPUTS: enabled buttons
# ALGORITHM:
#           FOR button in buttons:
#               ENABLE tkinter in button
#           ENDFOR          
# HISTORY: 
# 2023.5.26 - Creation
# 2023.5.26 - Completion
########################################################

def enableButtons(buttons):
    for button in buttons:
        button.config(state=tkinter.NORMAL)  # enable all buttons

#########################################################
# FCN NAME: disableButtons
# DESCRIPTION: Disables all other buttons whilst playing game
# INPUTS: buttons
# OUTPUTS: disabled buttons
# ALGORITHM:
#           FOR button in buttons:
#               DISABLE tkinter in button
#           ENDFOR         
# HISTORY: 
# 2023.5.26 - Creation
# 2023.5.26 - Completion
########################################################

def disableButtons(buttons):
    for button in buttons:
        button.config(state=tkinter.DISABLED)  # disable all buttons

#########################################################
# FCN NAME: gameboyButton
# DESCRIPTION: Exercises various functions to get GameBoy working
# INPUTS: usr, buttons, display, game
# OUTPUTS: messagebox error
# ALGORITHM:
#           SAVE coinPriceMet(usr, coins, display) as coins_met
#           GET current coins
#           IF (coins_met is False):
#               SHOWERROR "Insufficient Coins"
#               RETURN 
#           ELSE:
#               disableButtons(buttons)
#               gameboyEmulator(buttons, game)
#           ENDIF             
# HISTORY: 
# 2023.5.27 - Creation
# 2023.5.27 - Completion
########################################################

def gameboyButton(usr, buttons, display, game):

    coins_met = coinsPriceMet(usr, display)  # check if coins amount is met
    coins = getCoins(usr)  # get current coins

    if (coins_met == False):
        messagebox.showerror("Insufficient Coins", f"You have {coins} coins, you need 8000 coins.")  # not enough coins error
        return  # close function
    else:
        disableButtons(buttons)  # disable all buttons
        gameboyEmulator(usr, buttons, game, display)  # run gameboy emulator with game title