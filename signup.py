import PySimpleGUI as pg
from numpy import sign
import pandas as pd
from utils import*


def signup():
    layout = [[pg.Text("First Name"), pg.InputText()],
              [pg.Text("Last Name"), pg.InputText()],
              [pg.Text("Username"), pg.InputText()],
              [pg.Text("Password"), pg.InputText()],
              [pg.Text("Re-enter Password"), pg.InputText()],
              [pg.Button("Create")],
              [pg.Button("Cancel")]]
    window = pg.Window('Sign up Screen', layout)
    while True:
        event, values = window.read()
        if event == "Cancel" or event == pg.WIN_CLOSED:
            break
        if event == "Create":
            if(check_password(values[3], values[4]) == True):
                encrypt_data(values)
                print('Account Created')
