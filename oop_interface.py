from Tkinter import *

class Demo1:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)

        yPos = 0
        xPos = 0

        for x in range(0, 100):
            if(xPos == 2000):
                yPos = yPos + 180
                xPos = 0
            self.new_window(xPos, yPos)
            xPos = xPos + 200

    def new_window(self, xPos, yPos):
        self.newWindow = Toplevel(self.master)
        self.newWindow.title('SPAM')
        self.newWindow.iconbitmap(r'c:/Users/Romano/PycharmProjects/rs_profit_calc/icon.ico')
        self.newWindow.geometry('{}x{}+{}+{}'.format(200, 150, xPos, yPos))

def main(): 
    root = Tk()
    app = Demo1(root)
    root.withdraw()
    root.mainloop()

if __name__ == '__main__':
    main()