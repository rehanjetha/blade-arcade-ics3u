##############################################
# Name: Rehan Jetha
# Course: ICS3U
# File: gameboy.py
# Description: GameBoy emulator game using PyBoy
# History: 	
# 2023.5.27 - Creation
# 2023.5.29 - Completion
##############################################

import os
from pyboy import PyBoy
import tkinter
from tkinter import messagebox
import time

from Control.coins import getCoins, updateCoins

try:
    from pyboy import logger
except ImportError:
    logger = None

#########################################################
# FCN NAME: gameboyEmulator
# DESCRIPTION: Makes a gameboy emulator window
# INPUTS: usr, buttons, game, display
# OUTPUTS: 
# ALGORITHM:
#           DISABLE logging from PyBoy
#           SHOWINFO "10 min to play, controls are in shell."
#           DEFINE constant "KEY_DATA" with controls
#           PRINT formatted KEY_DATA using prints & for loop
#
#           def saveGame():
#               WITH OPEN(f"Saves/{game}.state" in binary writing mode):
#                   SAVE game state to file
#               ENDWITH
#           END saveGame()
#
#           def closeGame():
#               saveGame()
#               STOP pyboy
#               FOR button in buttons:
#                   REENABLE all buttons
#               ENDFOR
#               SHOWINFO "progress saved"
#           END closeGame()
#
#           SET start_time to current time
#           SET total_time to 600 seconds (10 min)
#           DEFINE save path for games
#
#           START game
#           
#           IF (path to save file exists):
#               WITH OPEN(f"Saves/{game}.state" in binary read mode):
#                   LOAD save file
#               ENDWITH
#           ENDIF
#
#           WHILE not advance pyboy frame by 1:
#               SET time_remainder to current time - start_time
#               IF (timer_remainder is greater than or equal to total_time):
#                   break
#               ENDIF
#           ENDWHILE
#
#           IF (game == "mario"):
#               GET coins in ones
#               GET coins in tens
#               ADD coins in ones and tens, multiply result by 100, add current coins
#               UPDATE current coins with new coins
#           
#           closeGame()   
# HISTORY: 
# 2023.5.27 - Creation
# 2023.5.28 - Completion
########################################################

def gameboyEmulator(usr, buttons, game, display):
    
    if logger:
        logger.log_level("DISABLE")  # disable logging

    messagebox.showinfo("Time Limit", "You will have 10 minutes to play. Controls are found in the shell.")  # show time limit message

    KEY_DATA = {
        "Up": "Up",
        "Down": "Down",
        "Left": "Left",
        "Right": "Right",
        "A": "A",
        "S": "B",
        "Return": "Start",
        "Backspace": "Select"
    }  # dictionary showing keyboard keys vs gameboy

    print("{:<12s}{:<17s}".format("Keyboard Key | ", "GameBoy"))  # make table header
    print("-" * 30)  # make seperator

    for key, value in KEY_DATA.items():
        print("{:<12s} {:<17s}".format(key, value))  # place data on table

    def saveGame():
        with open(f"Saves/{game}_{usr}.state", "wb") as save_file:
            pyboy.save_state(save_file)  # save game to folder

    def closeGame():
        saveGame()  # save game
        pyboy.stop()  # close pyboy
        for button in buttons:
            button.config(state=tkinter.NORMAL)  # reenable buttons on home
        messagebox.showinfo("Game Closed", "Your progress has been saved.")  # show game close msg

    start_time = time.time()  # get start time
    total_time = 600  # time in seconds
    save_path = f"Saves/{game}.state"  # save file path

    pyboy = PyBoy(f"ROMs/{game}.gb")  # open gameboy rom based on selection

    if (os.path.exists(save_path)):
        with open(f"Saves/{game}_{usr}.state", "rb") as save_file:
            pyboy.load_state(save_file)  # save game to folder

    while not pyboy.tick():

        time_remainder = time.time() - start_time  # find remainder for timer

        if (time_remainder >= total_time):
            break  # close program

    if (game == "mario"):
        coins_ones = pyboy.get_memory_value(0x982A)  # get coins value in ones
        coins_tens = pyboy.get_memory_value(0x9829)  # get coins value in tens
        coins_total = (((coins_tens * 10) + (coins_ones)) * 10) + getCoins(usr)  # give coins to user
        updateCoins(usr, coins_total, display)  # update coins total with new values

    closeGame()  # close game
