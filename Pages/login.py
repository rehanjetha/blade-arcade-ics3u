##############################################
# Name: Rehan Jetha
# Course: ICS3U
# File: login.py
# Description: Login Page of Arcade System
# History: 	
# 2023.5.24 - Creation
# 2023.5.29 - Completion
##############################################

import json
from PIL import ImageTk, Image
import tkinter
from tkinter import messagebox

#########################################################
# FCN NAME: forgotPw
# DESCRIPTION: Prompts a messagebox to email admin
# INPUTS: N/A
# OUTPUTS: messagebox
# ALGORITHM:
#           SHOWINFO "Please make a new account."
# HISTORY: 
# 2023.5.24 - Creation
# 2023.5.24 - Completion
########################################################

def forgotPw():
    messagebox.showinfo("Forgot Password", "Please make a new account.")  # send messagebox prompt

#########################################################
# FCN NAME: signIn
# DESCRIPTION: Checks credentials based on JSON file
# INPUTS: username, password, root
# OUTPUTS: messagebox
# ALGORITHM:
#           GLOBAL signed_coins
#           GLOBAL signed_username
#
#           IF (username.strip() is blank) or (password.strip() is blank):
#               SHOWERROR "Username or Password not given."
#               RETURN
#           ENDIF
#
#           WITH OPEN("Database/users.json" in read+ mode) as users_file:
#               LOAD JSON users_file as data
#               GET 'users' from data as usr_data
#               FOR entry in usr_data:
#                   IF (entry['username'] is username):
#                       IF (entry['password'] is password):
#                           DEFINE entry['coins'] as signed_coins
#                           DEFINE username as signed_username
#                           DESTROY root
#                           RETURN
#                       ELSE:
#                           SHOWERROR "Password is incorrect!"
#                           RETURN
#                       ENDIF
#
#               ENDFOR
#               
#               SHOWERROR "Account not found! Use Sign Up to create account."
# HISTORY: 
# 2023.5.24 - Creation
# 2023.5.26 - Completion
########################################################

def signIn(username, password, root):  
    global signed_coins  # declare global signed coins
    global signed_username  # declare global signed username

    if (username.strip() == "") or (password.strip() == ""):
        messagebox.showerror("Missing Fields", "Username or Password not given.")  # missing username/pw error
        return  # close function
    
    with open("Database/users.json", "r") as users_file:
        data = json.load(users_file)  # load the json data

        usr_data = data.get('users')  # get user data

        for entry in usr_data:
            if (entry['username'] == username):
                if (entry['password'] == password):
                    signed_coins = entry['coins']  # assign coins variable
                    signed_username = username  # make signed username to send
                    root.destroy()  # close the login page
                    return  # close the function
                else:
                    messagebox.showerror("Incorrect Password", "Password is incorrect!")  # wrong password
                    return  # close fnc

        messagebox.showerror("No Account", "Account not found! Use \"Sign Up\" to create account.")  # display acc made

#########################################################
# FCN NAME: signUp
# DESCRIPTION: Allows the user to create an account.
# INPUTS: username, password
# OUTPUTS: messagebox
# ALGORITHM:
#           IF (username.strip() is blank) or (password.strip() is blank):
#               SHOWERROR "Username or Password not given."
#               RETURN
#           ENDIF
#
#           IF (length of username is greater than 16 chars):
#               SHOWERROR "Username is too long"
#               RETURN
#           ENDIF
#
#           WITH OPEN("Database/users.json" in read+ mode) as users_file:
#               LOAD JSON users_file as data
#               GET 'users' from data as usr_data
#               FOR entry in usr_data:
#                   IF (entry['username'] is username):
#                       SHOWERROR "Username is already taken."
#                       RETURN
#                   ENDIF
# 
#               APPEND username, password, 1000 coins to usr_data
#               MOVE cursor to top of file
#               DUMP new data back to file
#               RESIZE file & strip file using TRUNCATE
#
#               SHOWINFO "Account Created, username, password"
# HISTORY: 
# 2023.5.24 - Creation
# 2023.5.26 - Completion
########################################################

def signUp(username, password):

    if (username.strip() == "") or (password.strip() == ""):
        messagebox.showerror("Missing Fields", "Username or Password not given.")  # missing username/pw error
        return  # close function
    
    if (len(username) > 16):
        messagebox.showerror("Too Long", "Username is more than 16 characters.")  # username too long
        return  # close function
    
    with open("Database/users.json", "r+") as users_file:
        data = json.load(users_file)  # load the json data

        usr_data = data.get('users')  # get user data

        for entry in usr_data:
            if (entry['username'] == username):
                messagebox.showerror("Taken", "Username is already taken.")  # username taken error
                return  # close function
        
        usr_data.append({
            "username": username,
            "password": password,
            "coins": 1000
        })  # create new user account with default coins

        users_file.seek(0)  # move cursor back to top of file
        json.dump(data, users_file, indent=4)  # write new data back to file
        users_file.truncate()  # resize file by stripping it

        messagebox.showinfo("Account Made", f"Account created!\nUsername: {username}\nPassword: {password}\nLogin using these credentials.")  # display acc made

#########################################################
# FCN NAME: loginPage
# DESCRIPTION: Makes a Login Page with various options
# INPUTS: widgets
# OUTPUTS: app
# ALGORITHM:
#           GLOBAL signed_coins
#           GLOBAL signed_username
#
#           CREATE root tkinter
#           TITLE root as "Blade Arcade Login"
#           SIZE root to 300x350
#           CREATE log_frame with tkinter, connect to root
#           PACK log_frame
#
#           DEFINE lock_icon using ImageTk to open lock_icon.ico
#           SET signed_coins to None for placeholder
#           SET signed_username to None for placeholder
#           
#           CREATE login header label
#           CREATE login label
#           PLACE login header at row 0, col 0, sticky "w"
#           PLACE login label at row 1, col 0, sticky "w", pady 20 down
#           
#           CREATE usr_name_label 
#           CREATE user name entry 
#           PLACE usr_name_label at row 2, col 0, sticky "w"
#           PLACE user name entry at row 3, col 0, sticky "w"
#
#           CREATE password label
#           CREATE password entry
#           PLACE password label at row 4, col 0, sticky "w"
#           PLACE password entry at row 5, col 0, sticky "w", pady 20 down
#           BIND signIn function to clicking enter when in password label
#           
#           CONFIG usr_name_label to add lock_icon to right side
#           CONFIG pw_label to add lock_icon to right side
#
#           CREATE forgot button, command=forgotPw
#           PLACE forgot button at row 4, col 0, sticky "e"
#
#           CREATE login button, command=lambda: signIn(user name entry, password entry, root)
#           PLACE login button at row 6, col 0, pady 20 down
#
#           CREATE sign up button, command=lambda: signUp(user name entry, password entry)
#           PLACE sign up button at row 8, col 0
#
#           RUN mainloop
# HISTORY: 
# 2023.5.24 - Creation
# 2023.5.27 - Completion
########################################################

def loginPage():
    global signed_coins  # declare global signed coins
    global signed_username  # declare global signed username

    root = tkinter.Tk()  # open instance of tkinter
    root.title("Blade Arcade Login")  # title root window
    root.geometry("300x350")  # set window to 300x350
    log_frame = tkinter.Frame(root)  # make home page, connect to window
    log_frame.pack()  # pack home page

    lock_icon = ImageTk.PhotoImage(Image.open("Resources/lock_icon.ico"))  # open lock icon image
    signed_coins = None  # set placeholder coins to 0
    signed_username = None  # set placeholder username to John Doe

    login_header = tkinter.Label(log_frame, text="Sign In", font=("Open Sans", 24, "bold"))  # make login header
    login_label = tkinter.Label(log_frame, text="Welcome to Blade Arcade! Please login below.")  # make login label
    login_header.grid(row=0, column=0, sticky="w")  # place login header 
    login_label.grid(row=1, column=0, sticky="w", pady=(0, 20))  # place login label 

    usr_name_label = tkinter.Label(log_frame, text="Username")  # make username label
    usr_name_entry = tkinter.Entry(log_frame)  # make user name entry
    usr_name_label.grid(row=2, column=0, sticky="w")  # place username label 
    usr_name_entry.grid(row=3, column=0, sticky="w")  # place usr_name entry 

    pw_label = tkinter.Label(log_frame, text="Password")  # make password label
    pw_entry = tkinter.Entry(log_frame, show="*")  # make password entry
    pw_label.grid(row=4, column=0, sticky="w")  # place password label 
    pw_entry.grid(row=5, column=0, sticky="w", pady=(0, 20))  # place password entry 
    pw_entry.bind("<Return>", lambda event: signIn(usr_name_entry.get(), pw_entry.get(), root))  # attempt sign in if enter clicked

    usr_name_label.config(image=lock_icon, compound="right")  # add lock icon to right of user name label
    pw_label.config(image=lock_icon, compound="right")  # add lock icon to right of pw label

    forgot_button = tkinter.Button(log_frame, text="Forgot password?", command=forgotPw)  # make a forgot password button
    forgot_button.grid(row=4, column=0, sticky="e")  # place forgot button 

    login_button = tkinter.Button(log_frame, text="Sign In", fg="white", bg="#24a0ed", width=35, height=2, command=lambda: signIn(usr_name_entry.get(), pw_entry.get(), root))  # make sign in button
    login_button.grid(row=6, column=0, pady=(0, 20))  # place login button 

    signup_button = tkinter.Button(log_frame, text="Sign Up", width=35, height=2, command=lambda: signUp(usr_name_entry.get(), pw_entry.get()))  # make signup button
    signup_button.grid(row=8, column=0)  # place sign up button

    root.mainloop()  # start mainloop