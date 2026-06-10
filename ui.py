import ctypes
from tkinter import Tk,Frame, Label, ttk
import logging


logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class App(Tk):
    def __init__(self,windowname : str,WIDTH : int, HEIGHT : int):
        super().__init__()
        self.title(windowname)
        self.update()
        
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.resizable(True, True)
        self.menu = Menu(self)
        self.workspace = Workspace(self)


        self.mainloop()








class Menu(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.place(x=0,y=0,relwidth=1,relheight = 0.05)

        self.config(relief='flat', borderwidth=1, background="lightgrey")

        self.grid_anchor(anchor="nw")
        self.grid_propagate(False)

        file_menu = ttk.Button(self, text='Add File',command=self.file_read)
        file_menu.grid(row=0,column=0,sticky='n', padx=2,pady=2)


    def file_read(self):
        logging.info("User clicked the 'Add File' button. Ready to open file dialog...")
        

class Workspace(Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.place(relx=0,rely=0.05,relwidth=1,relheight=0.95)
        self.config(bg="darkgrey")

        for i in range(4):
            self.rowconfigure(i,weight=1)
            self.columnconfigure(i,weight=1)
        
        self.grid_slots = {}

        for row in range(4):
            for col in range(4):
                slot = Frame(self,bg="grey",highlightbackground="black",highlightthickness=1)
                slot.grid(row=row,column=col,sticky="nsew",padx=2,pady=2)

                lbl = Label(slot,text =f"Row: {row}\nCol=f{col}", bg="white")
                self.grid_slots[(row,col)] = slot




if __name__ == '__main__':
    app = App("My GUI Components", 800, 600)
    app.mainloop()
