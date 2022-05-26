import PySimpleGUI as pg


def main_screen():
    layout = [[pg.Text("New Window")],
              [pg.Button("Cancel")]]
    window = pg.Window("Main Page", layout)
    while True:
        event, values = window.read()
        if event == "Cancel" or event == pg.WIN_CLOSED:
            break
    window.close()
