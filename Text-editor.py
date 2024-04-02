import PySimpleGUI as sg 


menu_layout = [ 
    ['File', ['Open', 'Save']],
    ['Tools', ['Add']]
]

# Create layout 
layout = [
    [sg.Menu(menu_layout)],
    [sg.Text("Unsaved")],
    [sg.Multiline(size = (50,30), key = '-CONTENT-', no_scrollbar = True)]
]


# Create window
window = sg.Window('Text Editor', layout)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Open':
        file_path = sg.popup_get_file("Choose a file: ")
        if file_path:
            print("File Selected", file_path)
            with open(file_path, 'r') as file:
                file_contents = file.read()
                window['-CONTENT-'].update(file_contents)
        else:
            print("No file selected or operation cancellled.")





window.close()