from tkinter import *


root = Tk()

root.configure(bg="black")
root.geometry("1240x620")
root.title("Minesweeper Game")
root.resizable(False,False)

top_frame = Frame(
    root,
    bg = "red",
    width =  1240,
    height = 130 
    
)

top_frame.place(x=0,y=0)

left_frame = Frame(
    root,
    bg = "blue",
    width=360,
    height=550
)

left_frame.place(x=0,y=200)

center_frame = Frame(
    root,
    bg = "green",
    width= 1204,
    height = 550
)

center_frame.place(x=150,y=150)

class Cell:
    def __init__(self,is_mine= False):
        self.is_mine = is_mine
        self.cell_btn_object = None

    def create_btn_object(self,location):
        btn = Button(
            location,
            text= "Text"
        )
        self.cell_btn_object = btn

"""
c1 = Cell()
c1.create_btn_object(center_frame)
c1.cell_btn_object.grid(column=0,row=0)

c2 = Cell()
c2.create_btn_object(center_frame)
c2.cell_btn_object.grid(column=0,row=1)
"""

for x in range(6):
    for y in range(6):
        c = Cell()
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column=x,row=y)

root.mainloop()