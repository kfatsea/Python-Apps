import PySimpleGUI as sg

# STEP 1 define the layout 
layout = [
    [sg.Text('Gender', enable_events=True, key='-TEXT-'),sg.Spin(['male','female'], key='-GENDER-')],
    [sg.Button('Button', key = '-BUTTON1-')],
    [sg.Input(key='-NAME-')],
    [sg.Text('Hello'), sg.Button('Print', key = '-BUTTON2-')]
]

# STEP 2 - create the window
window = sg.Window('Converter', layout)

# STEP 3 - the event loop
while True:
    event, values = window.read() # Read the event that happened and the values dictionary
    #print(event, values) 

    if event == sg.WIN_CLOSED:
        break

    if event == '-BUTTON1-':
        window['-TEXT-'].update(visible = False)

    if event == '-BUTTON2-':
        print(values['-NAME-'])
    
    if event == '-TEXT-': # Treat text as button
        print('text was pressed')

window.close()
