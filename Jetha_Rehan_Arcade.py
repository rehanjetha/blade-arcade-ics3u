##############################################
# Name: Rehan Jetha
# Course: ICS3U
# File: Jetha_Rehan_Arcade.py
# Description: Main PGM of Arcade System
# History: 	
# 2023.5.25 - Creation
# 2023.5.29 - Completion (birthday!)
##############################################

import os
import sys

from Pages.home import homePage
from Pages.login import loginPage

#########################################################
# FCN NAME: main
# DESCRIPTION: Control center for entire program
# INPUTS: signed_coins, signed_username
# OUTPUTS: N/A
# ALGORITHM:
#           CHANGE directory to parent directory
#           
#           START login page
#
#           from Pages.login import signed_coins, signed_username
#       
#           IF (signed_coins or signed_username is None):
#               CLOSE program
#           ENDIF
#
#           homePage(signed_username, signed_coins)
#
# HISTORY: 
# 2023.5.24 - Creation
# 2023.5.27 - Added crash handling
# 2023.5.29 - Completion
########################################################

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # change file directory to parent

loginPage()  # start login page

from Pages.login import signed_username, signed_coins  # must break convention as vars don't gain meaning until fnc runs

if (signed_coins == None) or (signed_username == None):
    sys.exit()  # close program if login was closed

homePage(signed_username, signed_coins)  # start home page