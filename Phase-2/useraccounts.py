from tfa import Check
import hashlib
import re
import maskpass
import sqlite3

global Password

def Menu():
    print("""
         ________________________
        |                        |
        |   User Account Menu:   |
        |                        |
        | 1. Login               |
        | 2. Sign-Up             |
        |                        |
        |________________________|
          """)
    User_Choice = input("What would you like to do: ")
    if User_Choice == "1":
        User_Login()
    elif User_Choice == "2":
        User_Sign_Up()
    else:
        print("Please only enter a 1 or a 2")
        Menu()

def User_Login():
    print("Login")

def User_Sign_Up():
    First_Name = str(input("Enter your first name: "))
    Last_Name = str(input("Enter your last name: "))
    Email = str(input("Enter your email: "))
    if Validate_Email(Email):
        Password = maskpass.askpass(mask=".")
        Confirm_Password = maskpass.askpass(mask=".")
    else:
        print("Please enter a valid email")
        User_Sign_Up()
    if Validate_Password(Password):
        if Password == Confirm_Password:
            Hash = hashlib.sha256(Password.encode()).hexdigest()
            print(Hash)
        else:
            print("Passwords do not match please try again.")
            User_Sign_Up()
    else:
        print("Password is not strong enough please try again")
        User_Sign_Up()
    if FA_Code(Email):
        Add_User(First_Name, Last_Name, Email, Hash)

def Validate_Password(Password):
    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
    match = re.match(pattern, Password)
    return bool(match)

def Validate_Email(Email):
    pattern = r"^[^@ ]+@[^@ ]+\.[^@ \.]{2,}$"
    match = re.match(pattern, Email)
    return bool(match)

def FA_Code(Email):
    Code = Check(Email)

    User_Input = int(input("What is your 2fa code: "))
    if User_Input == Code:
        return True
    else: 
        print("That code is incorrect please try again")
        FA_Code(Email)

def Add_User(First_Name, Last_Name, Email, Hash):
    conn = sqlite3.connect('userdata.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT,
            lastname TEXT,
            email TEXT,
            password TEXT
        )
    ''')

    user_data = (First_Name, Last_Name, Email, Hash)
    print(user_data)
    cursor.execute('''
        INSERT INTO users (firstname, lastname, email, password)
        VALUES (?, ?, ?, ?)
    ''', user_data)

Menu()
