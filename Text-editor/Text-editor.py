import PySimpleGUI as sg 


smileys = [
    'happy', [':)','xD',':D','<3'],
    'sad', [':(','T_T'],
    'other', [':3']
]

smiley_events = smileys[1] + smileys[3] + smileys[5] #to make events accessilble

menu_layout = [ 
    ['File', ['Open', 'Save', '---', 'Exit']],
    ['Tools', ['Word Count']],
    ['Add', smileys]
]

# Create layout 
layout = [
    [sg.Menu(menu_layout, k = '-MENU-')],
    [sg.Text("Unsaved"), sg.Button('Popup Button')],
    [sg.Multiline(size = (40,20), key = '-TEXTBOX-', no_scrollbar = True)]
]


# Create window
window = sg.Window('Text Editor', layout)

# Event loop
while True:
    event, values = window.read()
    print(event, values)

    if event == sg.WIN_CLOSED:
        break

    if event == 'Word Count':
        full_text = values['-TEXTBOX-']
        clean_text = full_text.replace('\n',' ').split(' ')
        clean_text = [word for word in clean_text if word != '']
        word_count = len(clean_text)
        print(f'full text:{full_text}\nclean text:{clean_text}\nword count:{word_count}')
        char_count = len(''.join(clean_text))
        sg.Popup(f'words:{word_count}\ncharacters: {char_count}')

    if event == 'Open':
        file_path = sg.popup_get_file("Text not shown", no_window = True)
        if file_path:
            print("File Selected", file_path)
            with open(file_path, 'r') as file:
                file_contents = file.read()
                window['-TEXTBOX-'].update(file_contents)
        else:
            print("No file selected or operation cancelled.")

    if event in smiley_events:
        full_text =  values['-TEXTBOX-']
        emoji = event 
        updated_text = full_text + ' ' + emoji
        window['-TEXTBOX-'].update(updated_text)
    
    # if event == 'Save':

      






window.close()