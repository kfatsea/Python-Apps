import PySimpleGUI as sg

# STEP 1 define the layout 
layout = [
    [sg.Input(s = 15, key='-INPUT-'), sg.Button('Convert', key='-BUTTON1-')],
    [sg.Text('Result', key='-RESULT-')]
]


# STEP 2 - create the window
window = sg.Window('Converter', layout)

# STEP 3 - the event loop
while True:
    event, values = window.read() # Read the event that happened and the values dictionary
    print(event, values) 

    if event == sg.WIN_CLOSED:
        break

    if event == '-BUTTON1-':
        window['-RESULT-'].update(values['-INPUT-'])

window.close()
