##############################################
# Name: Rehan Jetha
# Course: ICS3U
# File: home.py
# Description: Home Page of Arcade System
# History: 	
# 2023.5.26 - Creation
# 2023.5.29 - Completion
##############################################

import subprocess as sp
import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image

from Control.buttons import disableButtons, gameboyButton

from Games.highlow import highlowGame
from Games.dfm import duckFishMosquitoGame

#########################################################
# FCN NAME: gamePrep
# DESCRIPTION: Generic game message: "move to shell!"
# INPUTS: buttons
# OUTPUTS: messagebox
# ALGORITHM:
#           SHOWINFO "Navigate to shell to play the game!"
#           disableButtons(buttons)         
# HISTORY: 
# 2023.5.26 - Creation
# 2023.5.26 - Completion
########################################################

def gamePrep(buttons):
    messagebox.showinfo("Game Opened", "Navigate to shell to play the game!")  # messagebox, nav to term
    disableButtons(buttons)  # disable all buttons

#########################################################
# FCN NAME: openLog
# DESCRIPTION: Open log file on user request
# INPUTS: usr
# OUTPUTS: 
# ALGORITHM:
#           DECLARE notepad app
#           DECLARE file path
#           TRY:
#               OPEN file path using notepad
#           EXCEPT:
#               SHOWINFO invalid, only on windows
#
# HISTORY: 
# 2023.5.29 - Creation
# 2023.5.29 - Completion
########################################################

def openLog(usr):
    programName = "notepad.exe"  # notepad app
    fileName = f"Database/rpg_{usr}.txt"  # file path
    try:
        sp.Popen([programName, fileName])  # open file path using notepad
    except:
        messagebox.showinfo("Feature Unavailable", "This feature only works on Windows, open the file manually.")  # show msg box error

#########################################################
# FCN NAME: homePage
# DESCRIPTION: Game manager: bridge to all games.
# INPUTS: usr, coins
# OUTPUTS: app
# ALGORITHM:
#           MAKE root window
#           TITLE root window as "Blade Arcade"
#           CONFIGURE background of root window
#           MAKE button list for enabling and disabling later
#           MAKE free games header
#           MAKE free games label
#           PLACE free games header
#           PLACE free games label
#           MAKE highlow button
#           PLACE highlow button
#           APPEND highlow button to button list
#           MAKE dfm button
#           PLACE dfm button
#           APPEND dfm button to list
#           MAKE usr_name_label
#           PLACE usr_name_label
#           MAKE welcome header
#           PLACE welcome header
#           MAKE welcome label
#           PLACE welcome label
#           OPEN blade image
#           RESIZE blade image
#           USE blade image for tkinter
#           MAKE image label
#           PLACE image
#           MAKE log button
#           PLACE log button
#           MAKE paid games header
#           MAKE paid games label
#           PLACE paid games header
#           PLACE paid games label
#           MAKE separator line 1
#           PLACE separator line 1
#           MAKE separator line 2
#           PLACE separator line 2
#           MAKE coins label
#           MAKE coins display
#           PLACE coins display
#           MAKE mario button
#           PLACE mario button
#           ADD mario button to button list
#           MAKE tetris button
#           PLACE tetris button
#           APPEND tetris button to button list
#           
#           START tkinter root.mainloop()
# HISTORY: 
# 2023.5.26 - Creation
# 2023.5.29 - Completion
########################################################

def homePage(usr, coins):
    root = tkinter.Tk()  # make root window
    root.title("Blade Arcade")  # title root window

    root.configure(bg="#343541")  # change background to #343541

    buttons = []  # make buttons list for storing handles

    free_games_header = tkinter.Label(root, text="Free Games", font=("Open Sans", 18, "bold"), fg="#FFFFFF", bg="#343541")  # make free games header
    free_games_label = tkinter.Label(root, text="Win coins with free games!", fg="#FFFFFF", bg="#343541")  # make free games label
    free_games_header.grid(row=0, column=0, sticky="nw")  # place free games header
    free_games_label.grid(row=0, column=0, sticky="nw", pady=(40, 0))  # place free games label

    highlow_button = tkinter.Button(root, text="HighLow Gamble", command=lambda: [gamePrep(buttons), highlowGame(usr, buttons, coins_display)], bg="#FFD700")  # make hl button, color gold
    highlow_button.grid(row=2, column=0, sticky="w", padx=(0, 20), pady=50)  # place hl button
    buttons.append(highlow_button)  # add hl button to list

    dfm_button = tkinter.Button(root, text="DFM Game", command=lambda: [gamePrep(buttons), duckFishMosquitoGame(usr, buttons, coins_display)], bg="#FFD700")  # make dfm button, color gold
    dfm_button.grid(row=3, column=0, sticky="w", padx=(0, 20), pady=(0, 50))  # place dfm button
    buttons.append(dfm_button)  # add dfm button to list

    usr_name_label = tkinter.Label(root, text=usr, font=("Arial", 12, "bold"), fg="#05b8cc", bg="#343541")  # make usr name label
    usr_name_label.grid(row=5, column=0, sticky="w")  # place usr name label

    welcome_header = tkinter.Label(root, text="WELCOME", font=("Open Sans", 24, "bold"), fg="#FFFFFF", bg="#343541")  # make welcome header
    welcome_header.grid(row=0, column=4, sticky="n")  # place welcome header back
    welcome_label = tkinter.Label(root, text="Enjoy your stay.", fg="#FFFFFF", bg="#343541")  # make free games label
    welcome_label.grid(row=0, column=4, sticky="n", pady=(40, 0))  # place free games label

    blade_image = Image.open("Resources/blade_arcade.png")  # open blade arcade image
    blade_image = blade_image.resize((200, 200), Image.ANTIALIAS)  # enlarge image slightly
    blade_image = ImageTk.PhotoImage(blade_image)  # make useable for tkinter
    image_label = tkinter.Label(image=blade_image, bg="#343541")  # place image on label
    image_label.place(relx=0.5, rely=0.54, anchor="center")  # move image up to 0.55 on the rely

    log_button = tkinter.Button(root, text="Open Log", fg="#FFFFFF", bg="#ED76E3", font=("Arial", 10, "bold"), command= lambda: openLog(usr))  # make log button
    log_button.grid(row=5, column=4, pady=(0, 10))  # place log button

    paid_games_header = tkinter.Label(root, text="Paid Games", font=("Open Sans", 18, "bold"), fg="#FFFFFF", bg="#343541")  # make paid games header
    paid_games_label = tkinter.Label(root, text="Play premium games!", fg="#FFFFFF", bg="#343541")  # make paid games label
    paid_games_header.grid(row=0, column=6, sticky="ne")  # place free games header
    paid_games_label.grid(row=0, column=6, sticky="ne", pady=(40, 0))  # place paid games label

    separator_line1 = tkinter.Frame(root, bg="#FFFFFF", width=2)  # make sep line 1
    separator_line1.grid(row=0, column=3, rowspan=root.grid_size()[1], sticky="ns", padx=(10, 0))  # place sep line 1

    separator_line2 = tkinter.Frame(root, bg="#FFFFFF", width=2)  # make sep line 2
    separator_line2.grid(row=0, column=5, rowspan=root.grid_size()[1], sticky="ns", padx=(0, 10))  # place sep line 2

    coins_label = tkinter.Label(root, text="Coins:", fg="#FFFFFF", bg="#343541")  # make coins label
    coins_display = tkinter.Label(root, text=f"{coins:,}", font=("Arial", 10, "bold"), fg="#FFD700", bg="#343541")  # make coins display
    coins_label.grid(row=5, column=6)  # place coins label
    coins_display.grid(row=5, column=6, sticky="se", pady=(0, 8))  # place coins display

    mario_button = tkinter.Button(root, text="Mario (8k Coins)", command=lambda: gameboyButton(usr, buttons, coins_display, "mario"), bg="#FF7070")  # make mario button
    mario_button.grid(row=2, column=6, sticky="ne", padx=(20, 0), pady=50)  # place mario button
    buttons.append(mario_button)  # add mario button to list

    tetris_button = tkinter.Button(root, text="Tetris (8k coins)", command=lambda: gameboyButton(usr, buttons, coins_display, "tetris"), bg="#FF7070")  # make tetris button
    tetris_button.grid(row=3, column=6, sticky="ne", padx=(20, 0), pady=(0, 50))  # place tetris button
    buttons.append(tetris_button)  # add tetris button to list

    root.mainloop()  # start mainloop (tkinter)