import PySimpleGUI as sg
import cv2 #Image resizing
from time import time


# Define create_window() to create the stopwatch window
def create_window():
    sg.theme('Black')
    button_color = ('#FFFFFF', '#FF0000')
    button_size = (5,1)
    
    #Resize the close icon image and save it
    im = cv2.imread('Media\cross.png')
    im = cv2.resize(im, [20,20])
    cv2.imwrite('Media\close_icon.png', im)

    # Create the layout of the window
    layout = [
        [sg.Push(),sg.Image('Media\close_icon.png', enable_events = True, k = '-EXIT-', pad = 0)],
        [sg.VPush()], # Vertical spacer
        [sg.Text('00.00', k = '-TIME-', font = 'Young 50', text_color = 'White')],
        [   # Buttons for START/STOP and LAP
            sg.Button('Start', k = '-STARTSTOP-', button_color = button_color, border_width = 0, size = button_size),
            sg.Button('lap', k = '-LAP-', button_color = button_color, border_width = 0, size = button_size, visible = False)
        ],
        [sg.Column([[]], key = '-LAPS-')], # Column for displaying lap times
        [sg.VPush()] # Vertical spacer 
    ]

    return sg.Window(
    'Stopwatch',
    layout,
    size = (300,300),
    no_titlebar = True,
    element_justification = 'center',
)

# Initialize variables
start_time = 0
running = False
lap_times = []
lap_amount = 1

# Event loop
window = create_window() # Create the initial window
while True:
    event, values = window.read(timeout=5) # Read events from the window

	# Exit program if thewindow is closed
    if event in [sg.WIN_CLOSED, '-EXIT-']:
        break

	# Handle the Starrt/Stop button events
    if event == '-STARTSTOP-':
        if running:
            # From active to stop
            running = False
            window['-STARTSTOP-'].update('Reset') # Change button text to 'Reset'
            window['-LAP-'].update(visible = False) # Hide the Lap button
        else:
            # From stop to reset
            if start_time > 0:
                window.close() # Close the current window
                window = create_window() # Create a new window
                start_time = 0 # Reset start_time
                lap_amount = 1 # Reset lap_amount
                lap_times = [] # Reset lap_times

            # From start to active
            else:
                start_time = time() # Start the timer
                running = True
                window['-STARTSTOP-'].update('Stop') # Change button text to 'Stop'
                window['-LAP-'].update(visible = True) # Show the Lap button

	# Update the timer display if the stopwatch is running
    if running:
        elapsed_time = round(time() - start_time,1)
        window['-TIME-'].update(elapsed_time)

	# Handle the Lap button event
    if event == '-LAP-':
        lap_time = round(elapsed_time - sum(lap_times),1) # Calculate lap time
        # Display lap time in the Lap column 
        window.extend_layout(window['-LAPS-'], [[sg.Text(lap_amount), sg.VSeperator(), sg.Text(elapsed_time), sg.VSeperator(), sg.Text(lap_time)]])
        lap_amount += 1 # Increment lap number
        lap_times.append(lap_time) # Add lap time to the list


# Close windowg
window.close()