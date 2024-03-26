import PySimpleGUI as sg

# STEP 1 define the layout 
layout = [
    [
        sg.Input(key = '-INPUT-'),
        sg.Spin(['km to mile', 'kg to pound', 'sec to min'], key = '-UNITS-'),
        sg.Button('Convert', key = '-CONVERT-')
    ],
    [sg.Text('Output', key = '-OUTPUT-')]
]

# STEP 2 - Create the window
window = sg.Window('Converter', layout)

# STEP 3 - The event loop
while True:
    event, values = window.read() # Read the event that happened and the values dictionary
    print(event, values) 

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':

        input_value = values['-INPUT-']

        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'km to mile':
                    output = float(input_value) * 0.6214
                    output_string = f'{input_value} km are {output} miles.'
                case 'kg to pound':
                    output = float(input_value) * 2.205
                    output_string = f'{input_value} kg are {output} pounds.'
                case 'sec to min':
                    output = float(input_value) / 60
                    output_string = f'{input_value} sec are {output} minutes.'
            window['-OUTPUT-'].update(output_string)

        else: 
            window['-OUTPUT-'].update('Please enter a number')

window.close()
