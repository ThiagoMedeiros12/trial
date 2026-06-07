from ast import main
from tkinter import Tk,Frame, Label



class App:
    def __init__(self,windowname : str):
        self.WINDOW_NAME = windowname
        self.WIDTH = 800
        self.HEIGHT = 600
        
    def get_WINDOW_NAME(self):
        return self.WINDOW_NAME

    def run(self):
        WINDOW_NAME = self.get_WINDOW_NAME()
        self.root = Tk()

        self.root.title(WINDOW_NAME)
        self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.root.resizable(True, True)


        main_frame = self.MainFrame(color="lightgrey", border=1, relief="ridge", pady=3, padx=3)
        main_frame.pack(fill='both',expand = True)

        left_section,middle_section,right_section = self.Create_three_sections(PARENT_FRAME=main_frame)

        self.Left_label(PARENT_FRAME=left_section)
        self.Middle_label(PARENT_FRAME=middle_section)
        self.Right_label(PARENT_FRAME=right_section)

        self.root.mainloop()


    def MainFrame(self,color: str, border: int, relief: str, pady : int, padx : int):
        main_frame = Frame(self.root)
        main_frame.config(bg=color, borderwidth=border, relief=relief, pady=pady, padx=padx)
        return main_frame

    def Create_three_sections(self,PARENT_FRAME):

        left_section =  Frame(PARENT_FRAME)
        left_section.pack(side="left", fill="both", expand=True)

        middle_section = Frame(PARENT_FRAME)
        middle_section.pack(side="left", fill="both", expand=True)

        right_section = Frame(PARENT_FRAME)
        right_section.pack(side="left", fill="both", expand=True)


        return left_section,middle_section,right_section

    def Left_label(self,PARENT_FRAME : Frame):
        left_label = Label(PARENT_FRAME)
        left_label.config(text="Left", bg="grey", fg="white", font=("Arial", 12))
        left_label.pack(side="left", fill="both", expand=True)
        return left_label

    def Middle_label(self,PARENT_FRAME : Frame):
        Middle_label = Label(PARENT_FRAME)
        Middle_label.config(text="Middle", bg="snow", fg="Black", font=("Arial", 12))
        Middle_label.pack(side="left", fill="both", expand=True)
        return Middle_label

    def Right_label(self,PARENT_FRAME : Frame):
        Right_label = Label(PARENT_FRAME)
        Right_label.config(text="Right", bg="blue", fg="white", font=("Arial", 12))
        Right_label.pack(side="left", fill="both", expand=True)
        return Right_label


if __name__ == '__main__':
    app = App("Main Window")
    app.run()

