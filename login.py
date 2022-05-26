import PySimpleGUI as pg
from cryptography.fernet import Fernet

from utils import *
from signup import *
from main_screen import *


def login():
    layout = [[pg.Text("Username"), pg.InputText()],
              [pg.Text("Password"), pg.InputText()],
              [pg.Button("Log-in"), pg.Button("Sign-up")],
              [pg.Button("Cancel")]]
    window = pg.Window('Log-in Screen', layout)

    while True:
        event, values = window.read()
        if event == "Cancel" or event == pg.WIN_CLOSED:
            break
        if event == "Sign-up":
            signup()
            break
        if event == "Log-in":
            username = values[0]
            password = values[1]
            data = decrypt_data(username)
            if data != None:
                if data["Password"] == password:
                    print('log-in success!')
                    window.close()
                    main_screen()
                else:
                    print('Password invalid')
            else:
                print("Username not found")
    window.close()
