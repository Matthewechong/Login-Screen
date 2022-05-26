import PySimpleGUI as pg
from cryptography.fernet import Fernet

from utils2 import decrypt_data
from signup import signup

# username, password, button(log-in), button(cancel)
def login():
    layout = [[pg.Text("Username"),pg.InputText()],
            [pg.Text("Password"),pg.InputText()],
            [pg.Button("Log-in"),pg.Button("Sign-up")],
            [pg.Button("Cancel")] ]  
    window = pg.Window('Log-in Screen', layout)

    while True:
        event, values = window.read()
        if event == "Cancel" or event == pg.WIN_CLOSED:
            break
        if event == "Sign-up":
            signup()
            break
        if event == "Log-in":
            # take text file of decrypted credentials
            # decrypt each line to the original message
            # compare the decrypted message of username & passwords to  values[0] and values[1]
            username = values[0]
            password = values[1]
            data = decrypt_data(username)
            if data != None:
                if data["Password"] == password:
                    print('log-in success!')
                else:
                    print('Password invalid')
            else:
                print("Username not found")
    window.close()
login()
