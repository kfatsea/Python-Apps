
import PySimpleGUI as sg

# Define the layout
layout = [
    [sg.Text('Enter your name:'), sg.Input(key='-NAME-')],
    [sg.Button('Submit')]
]

# Create the window
window = sg.Window('Simple Window', layout)

# Event loop
while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    
    # Accessing the input element object using its key
    input_element = window['-NAME-']
    
    # Check if the input element is found in the window dictionary
    if input_element:
        # Accessing the value of the input element using its key
        name = values['-NAME-']
        sg.popup(f'Hello, {name}!')

# Close the window
window.close()