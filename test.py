# from PySimpleGUI import PySimpleGUI as sg

# layout = [[sg.Text('My one-shot window.')],      
#                  [sg.InputText(), sg.FileBrowse()],      
#                  [sg.Submit(), sg.Cancel()]]      

# window = sg.Window('Window Title').Layout(layout)    

# event, values = window.Read()    
# window.Close()

# source_filename = values[0] 

import PySimpleGUI as sg      

layout = [[sg.Text('Persistent window')],      
          [sg.Input(do_not_clear=True)],      
          [sg.Button('Read'), sg.Exit()]]      

window = sg.Window('Window that stays open').Layout(layout)      

while True:      
    event, values = window.Read()      
    if event is None or event == 'Exit':      
        break      
    print(event, values)    

window.Close()