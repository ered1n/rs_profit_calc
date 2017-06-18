from Tkinter import *

def executeOption():
    print('Test')

root = Tk()

# main menu

menu = Menu(root)
root.config(menu=menu)
root.geometry("500x300")

subMenu = Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='New Project...', command=executeOption)
subMenu.add_command(label='New...', command=executeOption)
subMenu.add_separator()
subMenu.add_command(label='Exit', command=root.quit)

editMenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Redo', command=executeOption)

# toolbar

toolbar = Frame(root, bg='blue')
insertButton = Button(toolbar, text='Insert Image', command=executeOption)
insertButton.pack(side=LEFT, padx=2, pady=2)
printButton = Button(toolbar, text='Print', command=executeOption)
printButton.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# status bar

status = Label(root, text='Preparing to do nothing...', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()