from tkinter import * 
from tkinter import RIDGE, TOP, Label, Tk, ttk
import random
import datetime
from tkinter import messagebox
#import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.nameoftablets = StringVar()
        self.ref= StringVar()
        self.dose = StringVar()

        lbltitle = Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGMENT SYSTEM",fg="red",bg="white",font=("times new romsn",50,"bold"))
        lbltitle.pack(side=TOP,fill="x")

        #-------Data Frame--------

        DataFrame=Frame(self.root,bd=20,padx=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1500,height=400)

        DataFrameLeft =  LabelFrame(DataFrame,bd=10,padx=20,relief=RIDGE,
                            font=("arial",12,"bold"),text="Paitent Information")
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        DataFrameRight =  LabelFrame(DataFrame,bd=10,padx=20,relief=RIDGE,
                            font=("arial",12,"bold"),text="Prescription")
        DataFrameRight.place(x=910,y=5,width=400,height=350)

        #============Button Frame============
        ButtonFrame=Frame(self.root,bd=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=530,width=1350,height=70)

        #============Details Frame============
        DetailsFrame=Frame(self.root,bd=20,relief=RIDGE)
        DetailsFrame.place(x=0,y=600,width=1350,height=190)

        #-------DataFrameLeft------------
        lblNameTablet=Label(DataFrameLeft,textvariable=self.nameoftablets,text="Names Of Tablets",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        conNameTablet=ttk.Combobox(DataFrameLeft,font=("arial",12,"bold"),width=33)
        conNameTablet["values"] = ("hug","kiss","hold hand","smile")
        conNameTablet.current(0)
        conNameTablet.grid(row=0,column=1)

        lblref=Label(DataFrameLeft,text="Ref no: ",font=("arial",12,"bold"),padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txref=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.ref,width=35)
        txref.grid(row=1,column=1)

        lblDose=Label(DataFrameLeft,text="Dose: ",font=("arial",12,"bold"),padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dose,width=35)
        txtDose.grid(row=2,column=1)

        lblNoOftablets=Label(DataFrameLeft,text="No Of Tablets: ",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNo=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35)
        txtNo.grid(row=3,column=1)

        lblLot=Label(DataFrameLeft,text="Lot : ",font=("arial",12,"bold"),padx=2,pady=5)
        lblLot.grid(row=4,column=0,sticky=W)
        txtlot=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35)
        txtlot.grid(row=4,column=1)

        lblDailyD=Label(DataFrameLeft,text="Daily Dose: ",font=("arial",12,"bold"),padx=4,pady=2)
        lblDailyD.grid(row=5,column=0,sticky=W)
        txtDaily=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35)
        txtDaily.grid(row=5,column=1)

        lblSide=Label(DataFrameLeft,text="Side Eff: ",font=("arial",12,"bold"),padx=2,pady=2)
        lblSide.grid(row=6,column=0,sticky=W)
        txSide=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35)
        txSide.grid(row=6,column=1)

        lblMadicine=Label(DataFrameLeft,text="Medicine: ",font=("arial",12,"bold"),padx=2,pady=2)
        lblMadicine.grid(row=1,column=0,sticky=W)
        txmed=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35)
        txmed.grid(row=1,column=1)

        lblBlood=Label(DataFrameLeft,text="Blood Pre: ",font=("arial",12,"bold"),padx=2,pady=2)
        lblBlood.grid(row=7,column=0,sticky=W)
        txBlood=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35)
        txBlood.grid(row=7,column=1)


        #============Dataframeright=================
        self.txtPrescription=Text(DataFrameRight,font=("arial",12,"bold"),height=16,width=39,padx=2,pady=2)
        self.txtPrescription.grid(row=0,column=0)

        #========Buttons=================
        btnPresButton = Button(ButtonFrame,text="prescription",bg="green",fg="white",font=("arial",12,"bold"),width=20,padx=2,pady=2)
        btnPresButton.grid(row=0,column=0)

        btnData = Button(ButtonFrame,text="Data",bg="green",fg="white",font=("arial",12,"bold"),width=20,padx=2,pady=2)
        btnData.grid(row=0,column=1)

        btnUpdate = Button(ButtonFrame,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=20,padx=2,pady=2)
        btnUpdate.grid(row=0,column=2)

        btnDelete = Button(ButtonFrame,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=20,padx=2,pady=2)
        btnDelete.grid(row=0,column=2)

        btnClear = Button(ButtonFrame,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=20,padx=2,pady=2)
        btnClear.grid(row=0,column=4)

        btnExit = Button(ButtonFrame,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),width=20,padx=2,pady=2)
        btnExit.grid(row=0,column=5)


        #================Table================
        #===============Scrollbar===============
        




        




       
















root=Tk()
obj=Hospital(root)
root.mainloop()
