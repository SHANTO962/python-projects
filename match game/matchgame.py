from tkinter import *
import random

root = Tk()
root.title("Match Game")
root.geometry("500x500")

matches = [1,1,2,2,3,3,4,4,5,5,6,6]

random.shuffle(matches)

my_frame = Frame(root)
my_frame.pack(pady=10)

count = 0
answer_list = []
answer_dict = {}

def button_click(b, number):
    global count,answer_list,answer_dict

    if b["text"] == " " and count < 2:
        b["text"] = matches[number]
        answer_list.append(number)
        answer_dict[b] = matches[number]

        count += 1
        print(answer_list)

    if len(answer_list) == 2:
        pass



b0 = Button(my_frame,text="",font=("Cosmic Sans",20),height=3,width=6,command=lambda: button_click(b0,0))
b1 = Button(my_frame,text="",font=("Cosmic Sans",20),height=3,width=6,command=lambda: button_click(b1,1))
b2 = Button(my_frame,text="",font=("Cosmic Sans",20),height=3,width=6,command=lambda: button_click(b2,2))
b3 = Button(my_frame,text="",font=("Cosmic Sans",20),height=3,width=6,command=lambda: button_click(b3,3))
b4 = Button(my_frame,text="",font=("Cosmic Sans",20),height=3,width=6,command=lambda: button_click(b4,4))
b5 = Button(my_frame,text="",font=("Cosmic Sans",20),height=3,width=6,command=lambda: button_click(b5,5))
b6 = Button(my_frame,text="",font=("Cosmic Sans",20),height=3,width=6,command=lambda: button_click(b6,6))
b7 = Button(my_frame,text="",font=("Cosmic Sans",20),height=3,width=6,command=lambda: button_click(b7,7))
b8 = Button(my_frame,text="",font=("Cosmic Sans",20),height=3,width=6,command=lambda: button_click(b8,8))
b9 = Button(my_frame,text="",font=("Cosmic Sans",20),height=3,width=6,command=lambda: button_click(b9,9))
b10 = Button(my_frame,text="",font=("Cosmic Sans",20),height=3,width=6,command=lambda: button_click(b10,10))
b11 = Button(my_frame,text="",font=("Arial",20),height=3,width=6,command=lambda: button_click(b11,11))

b0.grid(row=0,column=0)
b1.grid(row=0,column=1)
b2.grid(row=0,column=2)
b3.grid(row=0,column=3)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=1,column=3)

b8.grid(row=2,column=0)
b9.grid(row=2,column=1)
b10.grid(row=2,column=2)
b11.grid(row=2,column=3)

root.mainloop()