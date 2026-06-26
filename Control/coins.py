##############################################
# Name: Rehan Jetha
# Course: ICS3U
# File: coins.py
# Description: Contains coin related functions
# History:
# 2023.5.27 - Creation
# 2023.5.28 - Completion
##############################################

from datetime import datetime
import inspect
import json
import os

#########################################################
# FCN NAME: getCoins
# DESCRIPTION: Finds up-to-date coins value
# INPUTS: usr
# OUTPUTS: cur_coins
# ALGORITHM:
#           WITH OPEN("Database/users.json" in read mode) as users_file:
#               LOAD JSON users_file as data
#           ENDWITH
#
#           FOR user in data['users']:
#               IF (user['username'] == usr):
#                   DEFINE cur_coins as current coins
#                   RETURN cur_coins
#               ENDIF
#           ENDFOR 
# HISTORY: 
# 2023.5.28 - Creation
# 2023.5.28 - Completion
########################################################

def getCoins(usr):
    with open("Database/users.json", 'r') as users_file:
        data = json.load(users_file)  # load JSON file as data

    for user in data['users']:
        if (user['username'] == usr):
            cur_coins = user['coins']  # find current coins
            return cur_coins  # return updated coins

#########################################################
# FCN NAME: updateCoins
# DESCRIPTION: Writes new coins to JSON file, updates display
# INPUTS: usr, coins, display
# OUTPUTS: writing coins
# ALGORITHM:
#           DEFINE log file path
#           FIND which file is calling fnc
#           WITH OPEN("Database/users.json" in read mode) as users_file:
#               LOAD JSON users_file as data
#           ENDWITH
#
#           FOR user in data['users']:
#               IF (user['username'] == usr):
#                   STORE previous_coins
#                   REDEFINE coins to current coins
#                   UPDATE display with new coins
#                   FIND coin difference
#                   
#                   IF (coin_diff is greater than or equal to 0):
#                       DEFINE result as "gained"
#                   ELSE:
#                       DEFINE result as "lost"
#                   ENDIF
#
#                   MAKE log entry with date, call file, username, result, coin diff
#                   
#                   WITH OPEN(log_file in append mode):
#                       WRITE log entry to log file
#                   ENDWITH
#                   BREAK
#               ENDIF
#           ENDFOR
#
#           WITH OPEN("Database/users.json" in write mode) as users_file:
#               DUMP new JSON data
#           ENDWITH
# HISTORY: 
# 2023.5.27 - Creation
# 2023.5.28 - Completion
########################################################

def updateCoins(usr, coins, display):

    log_file = f"Database/rpg_{usr}.txt"  # define path for rpg file

    calling_file = os.path.basename(inspect.stack()[1].filename)  # figure out which file called this fnc

    with open("Database/users.json", 'r') as users_file:
        data = json.load(users_file)  # load JSON file as data

    for user in data['users']:
        if (user['username'] == usr):
            previous_coins = user['coins']  # calculate previous coins
            user['coins'] = coins  # update current user coins
            display.config(text=f"{coins: ,}")  # update coins value on label

            coin_diff = coins - previous_coins  # find gain/loss from coins

            if (coin_diff >= 0):
                result = "gained"  # figure out user action, gained
            else:
                result = "lost"  # figure out user action, lost

            log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M')} - {calling_file}: {usr} {result} {abs(coin_diff): ,} coins.\n"
            # print time, calling file, username, result, magnitude of coin difference

            with open(log_file, 'a') as log:
                log.write(log_entry)  # append log entry to file
            break  # end loop

    with open("Database/users.json", "w") as users_file:
        json.dump(data, users_file, indent=4)  # dump updated data back


#########################################################
# FCN NAME: coinsPriceMet
# DESCRIPTION: Ensures buttons are useable
# INPUTS: usr, display
# OUTPUTS: updated coins display
# ALGORITHM:
#           GET current coins
#           IF (coins are greater than or equal to 8000):
#               SUBTRACT 8000 from coins
#               updateCoins(usr, coins, display)
#           ELIF (coins are equal to 8000):
#               REDEFINE coins to 1000
#               updateCoins(usr, coins, display)
#           ELSE:
#               RETURN False
#           ENDIF                        
# HISTORY: 
# 2023.5.27 - Creation
# 2023.5.27 - Completion
########################################################

def coinsPriceMet(usr, display):
    coins = getCoins(usr)  # get current coins
    if (coins > 8000):
        coins -= 8000  # subtract 8000 coins
        updateCoins(usr, coins, display)  # update coins
    elif (coins == 8000):
        coins = 1000  # subtract 8000 coins
        updateCoins(usr, coins, display)  # update coins
    else:
        return False  # return False for coins met 