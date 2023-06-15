# hello_psg.py

import PySimpleGUI as sg

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")],[sg.Text("Choose a file: "), sg.FileBrowse()]]

# # Create the window
# window = sg.Window("Demo", layout)
window = sg.Window('My File Browser', layout, size=(300,200))
# sg.Input()

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
