import PySimpleGUI as sg

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font = 'Franklin 14', button_element_size = (6,3))
    button_size = (6,3)
    layout = [
        [sg.Text(
            '', 
            key = '-OUTPUT-',
            font = 'Franklin 26',
            expand_x = True,
            justification = 'right', 
            pad = (10,20),
            right_click_menu = theme_menu)
        ],
        [sg.Button('Clear', expand_x = True), sg.Button('Enter',expand_x = True)],
        [sg.Button(7, size = button_size), sg.Button(8, size = button_size),sg.Button(9, size = button_size),sg.Button('*', size = button_size)],
        [sg.Button(4, size = button_size), sg.Button(5, size = button_size),sg.Button(6, size = button_size),sg.Button('/', size = button_size)],
        [sg.Button(1, size = button_size), sg.Button(2, size = button_size),sg.Button(3, size = button_size),sg.Button('-', size = button_size)],
        [sg.Button(0, expand_x = True), sg.Button('.', size = button_size),sg.Button('+', size = button_size)] 
    ]

    return sg.Window('Calculator', layout)

# Menu definition
theme_menu = ['menu', ['DarkBlue5', 'DarkGrey15', 'DarkGrey14', 'random']]
window = create_window('DarkGrey14')

current_num = []
full_operation = []

while True:
    event, values = window.read()
    #print(event, values)

    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in ['0','1','2','3','4','5','6','7','8','9','.']:
        current_num.append(event)
        num_string = ''.join(current_num)
        window['-OUTPUT-'].update(num_string)

    if event in ['+','-','*','/']:
        full_operation.append(''.join(current_num))
        current_num = []
        full_operation.append(event)
        print(full_operation)
        window['-OUTPUT-'].update('')

    if event == 'Enter':
        full_operation.append(''.join(current_num))
        print(full_operation)
        result = eval(''.join(full_operation))
        window['-OUTPUT-'].update(result)
        full_operation = []

    if event == 'Clear':
        full_operation = []
        current_num = []
        window['-OUTPUT-'].update('')





window.close()

    