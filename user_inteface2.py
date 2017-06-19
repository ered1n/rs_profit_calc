from Tkinter import *

global row
row = 1

def generateLabel(master):
    Label(master, text='Item: ').grid(row=row, sticky=W)

def generateInput(master):
    Entry(master).grid(row=row, column=1)

def generateButton(master, command):
    Button(master, text='Buy item', command=command).grid(row=row, column=2, padx=10)

def buyItem():
    print('Item bought')
    row = row + 1
    generateLabel(buyFrame)
    generateInput(buyFrame)
    generateButton(buyFrame, buyItem)


root = Tk()
root.geometry('600x400')
root.title('RuneScape Profit Calculator')

# ~~~~~~~~~~~~~~~~~~~~~~~~ BUY ~~~~~~~~~~~~~~~~~~~~~~~~
buyLabel = Label(root, text='Buy', bd=2, relief=SUNKEN, anchor=W).pack(fill=X)

buyFrame = Frame(root)

generateLabel(buyFrame)
generateInput(buyFrame)
generateButton(buyFrame, buyItem)

buyFrame.pack()

# Label(root, text="First").grid(row=0, sticky=W)
# Label(root, text="Second").grid(row=1, sticky=W)
#
# e1 = Entry(root)
# e2 = Entry(root)
#
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)

root.mainloop()