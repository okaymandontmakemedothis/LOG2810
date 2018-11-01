# from PySimpleGUI import PySimpleGUI as sg

# layout = [[sg.Text('My one-shot window.')],      
#                  [sg.InputText(), sg.FileBrowse()],      
#                  [sg.Submit(), sg.Cancel()]]      

# window = sg.Window('Window Title').Layout(layout)    

# event, values = window.Read()    
# window.Close()

# source_filename = values[0] 




# import PySimpleGUI as sg      

# layout = [[sg.Text('Persistent window')],      
#           [sg.Input(do_not_clear=True)],      
#           [sg.Button('Read'), sg.Exit()]]      

# window = sg.Window('Window that stays open').Layout(layout)      

# while True:      
#     event, values = window.Read()      
#     if event is None or event == 'Exit':      
#         break      
#     print(event, values)    

# window.Close()




# import sys  
# if sys.version_info[0] >= 3:  
#     import PySimpleGUI as sg  
# else:  
#     import PySimpleGUI27 as sg  

# layout = [[sg.Text('Your typed chars appear here:'), sg.Text('', key='_OUTPUT_') ],  
#           [sg.Input(do_not_clear=True, key='_IN_')],  
#           [sg.Button('Show'), sg.Button('Exit')]]  

# window = sg.Window('Window Title').Layout(layout)  

# while True:                 # Event Loop  
#   event, values = window.Read()  
#   print(event, values)
#   if event is None or event == 'Exit':  
#       break  
#   if event == 'Show':  
#       # change the "output" element to be the value of "input" element  
#       window.FindElement('_OUTPUT_').Update(values['_IN_'])

# window.Close()



# import PySimpleGUI as sg

# # Very basic window.  Return values as a list

# layout = [
#           [sg.Text('')],
#           [sg.Text('Name', size=(0, 0)), sg.InputText('')],
#           [sg.Text('Address', size=(15, 1)), sg.InputText('')],
#           [sg.Text('Phone', size=(15, 1)), sg.InputText('')],
#           [sg.Submit(), sg.Cancel(), sg.Exit()]
#          ]

# window = sg.Window('Simple data entry window').Layout(layout)
# button, values = window.Read()

# print(button, values[0], values[1], values[2])


# import os
# print(os.path.expanduser("~/Desktop/pleasant/tp1_log2810/images/ambulance2.gif"))




# import sys
# if sys.version_info[0] >= 3:
#     import PySimpleGUI as sg
# else:
#     import PySimpleGUI27 as sg

# layout = [
#            [sg.Canvas(size=(150, 150), background_color='red', key='canvas')],
#            [sg.T('Change circle color to:'), sg.ReadButton('Red'), sg.ReadButton('Blue')]
#            ]

# window = sg.Window('Canvas test').Layout(layout).Finalize()

# cir = window.FindElement('canvas').TKCanvas.create_oval(50, 50, 100, 100)

# while True:
#     event, values = window.Read()
#     if event is None:
#         break
#     if event is 'Blue':
#         window.FindElement('canvas').TKCanvas.itemconfig(cir, fill = "Blue")
#     elif event is 'Red':
#         window.FindElement('canvas').TKCanvas.itemconfig(cir, fill = "Red")















import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

treedata = sg.TreeData()

treedata.Insert("", '_A_', 'A', [1,2,3])
treedata.Insert("", '_B_', 'B', [4,5,6])
treedata.Insert("_A_", '_A1_', 'A1', ['can','be','anything'])
treedata.Insert("", '_C_', 'C', [])
treedata.Insert("_C_", '_C1_', 'C1', ['or'])
treedata.Insert("_A_", '_A2_', 'A2', [None, None])
treedata.Insert("_A1_", '_A3_', 'A30', ['getting deep'])
treedata.Insert("_C_", '_C2_', 'C2', ['nothing', 'at', 'all'])

for i in range(100):
    treedata.Insert('_C_', i, i, [])

layout = [[ sg.Text('Tree Test') ],
          [ sg.Tree(data=treedata, headings=['col1', 'col2', 'col3'],change_submits=True, auto_size_columns=True, num_rows=10, col0_width=10, key='_TREE_', show_expanded=True),
            ],
          [ sg.Button('Read'), sg.Button('Update')]]

window = sg.Window('Tree Element Test').Layout(layout)

print(treedata)

while True:     # Event Loop
    event, values = window.Read()
    if event is None:
        break
    if event == 'Update':
        treedata = sg.TreeData()
        treedata.Insert("", '_A_', 'A', [1, 2, 3])
        treedata.Insert("", '_B_', 'B', [4, 5, 6])
        treedata.Insert("_A_", '_A1_', 'A1', ['can', 'be', 'anything'])
        treedata.Insert("", '_C_', 'C', [])
        treedata.Insert("_C_", '_C1_', 'C1', ['or'])
        treedata.Insert("_A_", '_A2_', 'A2', [None, None])
        window.FindElement('_TREE_').Update(treedata)
    elif event == 'Read':
        print(event, values)