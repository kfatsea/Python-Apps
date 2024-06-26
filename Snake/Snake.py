import PySimpleGUI as sg 

# Define layout
layout = [

]


# Create window
window = sg.Window('Snake', layout)

# Event Loop
while True:
    event, values = window.read() #Read the event that has happened and the values dictionary

    if event == sg.WIN_CLOSED:
        break


# Close window
window.close()