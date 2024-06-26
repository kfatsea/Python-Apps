import PySimpleGUI as sg 

# game constants
FIELD_SIZE = 400

# Define layout
sg.theme('Green')
field = sg.Graph(
   canvas_size = (FIELD_SIZE, FIELD_SIZE),
    graph_bottom_left = (0,0),
    graph_top_right = (FIELD_SIZE, FIELD_SIZE),
    background_color = 'black'
)

layout = [[field]]


# Create window
window = sg.Window('Snake', layout)

# Event Loop
while True:
    event, values = window.read() #Read the event that has happened and the values dictionary

    if event == sg.WIN_CLOSED:
        break


# Close window
window.close()