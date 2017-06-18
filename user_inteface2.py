from Tkinter import *

def generateInput(master):
    input = Entry(master)
    input.pack(side=LEFT, pady=10)

def generateButton(master, command):
    button = Button(master, text='Buy item', command=command)
    button.pack(side=LEFT, padx=10)

def buyItem():
    print('Item bought')


root = Tk()
root.geometry('600x400')

# ~~~~~~~~~~~~~~~~~~~~~~~~ BUY ~~~~~~~~~~~~~~~~~~~~~~~~
buyFrame = Frame(root, bd=1, relief=SUNKEN)

buyLabel = Label(buyFrame, text='Buy', bd=2, relief=SUNKEN, anchor=W)
buyLabel.pack(fill=X)

buyInputLabel = Label(buyFrame, text='Item: ')
buyInputLabel.pack(side=LEFT)

generateInput(buyFrame)
generateButton(buyFrame, buyItem)

buyFrame.pack(side=TOP, fill=X)


# ~~~~~~~~~~~~~~~~~~~~~~~~ SELL ~~~~~~~~~~~~~~~~~~~~~~~~
sellFrame = Frame(root, bd=1, relief=SUNKEN)

sellLabel = Label(sellFrame, text='Sell', bd=2, relief=SUNKEN, anchor=W)
sellLabel.pack(fill=X)

sellInputLabel = Label(sellFrame, text='Item: ')
sellInputLabel.pack(side=LEFT)

generateInput(sellFrame)

sellFrame.pack(side=TOP, fill=X)

root.mainloop()