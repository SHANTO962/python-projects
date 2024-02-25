from tkinter import *
from PyMultiDictionary import MultiDictionary

dictionary = MultiDictionary()
root = Tk()
root.title("Word Dictionary ")
root.geometry("1000x700")

def dict():
    meaning.config(text=dictionary.meaning("en",word.get())[1])
    synonym.config(text=dictionary.synonym("en",word.get()))
    antonym.config(text=dictionary.antonym("en",word.get()))


Label(root,text="Word Dictionary",font=("Arial"),fg="Purple").pack(pady=10)
frame = Frame(root)
Label(frame,text="Type Word:",font=("Arial")).pack(side=LEFT)
word = Entry(frame,font=("Arial"))
word.pack()
frame.pack(pady=10)

frame1 = Frame(root)
Label(frame1,text="Meaning:",font=("Arial")).pack(side=LEFT)
meaning = Label(frame1,text="",font=("Arial"),wraplength=600)
meaning.pack()
frame1.pack(pady=15)

frame2 = Frame(root)
Label(frame2,text="Synonym:",font=("Arial")).pack(side=LEFT)
synonym = Label(frame2,text="",font=("Arial"),wraplength=600)
synonym.pack()
frame2.pack(pady=15)

frame3 = Frame(root)
Label(frame3,text="Antonym:",font=("Arial")).pack(side=LEFT)
antonym = Label(frame3,text="",font=("Arial"),wraplength=600)
antonym.pack(side=LEFT)
frame3.pack(pady=20)






Button(root,text="Submit",font=("Arial"),command= dict).pack()

root.mainloop()