from tkinter import ttk 
import tkinter as tk
from tkinter import *

from tkinter import filedialog
import os
from PIL import Image, ImageTk
from query_search_by import QuerySearchBy
import sqlite3
from delete_contact_gui import MainWinDel
from add_contact_gui import MainWin

class MainWinQuery(MainWin, MainWinDel, QuerySearchBy):
    def __init__(self):
        self.connection = sqlite3.connect("database/adress.db")
        self.win = Tk()
        self.win.title=("Adress-Management")
        self.win.geometry('800x600')
        self.co0 = "#ffffff"
        self.co1 = "#000000"
        self.co2 = "#20214f"
        self.win.configure(background=self.co0)
        self.win.resizable(width=False, height=False)


    def SearchByPhone(self, event):
        for x in self.tree.get_children():
            self.tree.delete(x)
        phone = self.entrySearchByPhone.get()
        self.askin_phone_query(phone,)       
        for row in self.contact:
            self.tree.insert('', END, values=row)

    def query_contact(self):
        for x in self.tree.get_children():
            self.tree.delete(x)
        self.askin_all_query()
        for row in self.contact:
            self.tree.insert('', END, values=row)


    def SearchByName(self, event):
        for x in self.tree.get_children():
            self.tree.delete(x)
        name = self.entrySearchByName.get()
        lname = self.entrySearchByLName.get()
        self.askin_query(name, lname)
        for row in self.contact:
            self.tree.insert('', END, values=row)


    def Window(self):
        top = Frame(self.win, width=800, height=50, bg=self.co2)
        top.grid(row=0, column=0, padx=0, pady=1)

        bottom = Frame(self.win, width=800, height=150, bg=self.co2)
        bottom.place(x=0, y=480)

        header = Label(top, text="Adress-Management ✆", height=1, font=("Bahnschrift 22 bold"), bg= self.co2, fg=self.co0)
        header.place(x=280, y=2)


        self.lbSearchByName = Label(self.win, text="Suche nach Name:", font=("Calibri 16 bold"), bg=self.co0, fg=self.co1)
        self.lbSearchByName.place(x=200, y=60, width=200)
        self.entrySearchByName = Entry(self.win)
        self.entrySearchByName.insert(0, "Vorname")
        self.entrySearchByName.bind("<Return>", self.SearchByName)
        self.entrySearchByName.place(x=400, y=60, width=160, height=30)


        self.lbSearchByLName = Label(self.win, text="Suche nach Name:", font=("Calibri 16 bold"), bg=self.co0, fg=self.co1)
        self.lbSearchByLName.place(x=200, y=60, width=200)
        self.entrySearchByLName = Entry(self.win)
        self.entrySearchByLName.insert(0, "Nachname")
        self.entrySearchByLName.bind("<Return>", self.SearchByName)
        self.entrySearchByLName.place(x=580, y=60, width=160, height=30)

        self.lbSearchByPhone = Label(self.win, text="Suche nach Tel.:", font=("Calibri 16 bold"), bg=self.co0, fg=self.co1)
        self.lbSearchByPhone.place(x=190, y=90, width=200)
        self.entrySearchByPhone = Entry(self.win)
        self.entrySearchByPhone.insert(0, "Tel.-Nr.")
        self.entrySearchByPhone.bind("<Return>", self.SearchByPhone)
        self.entrySearchByPhone.place(x=400, y=90, width=160, height=30)

        
        # Add Contact Button
        self.bAdd = Button(self.win, text="Alle Kontakte abfragen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.query_contact)
        self.bAdd.place(x = 480, y = 370, width=255, height=40)

        #Update
        self.bAdd = Button(self.win, text="Kontakt aktualisieren", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0)
        self.bAdd.place(x = 20, y = 128, width=190, height=40)

        #Add
        self.bAdd = Button(self.win, text="Kontakt hinzufügen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0)
        self.bAdd.place(x = 20, y = 228, width=190, height=40)

        def mainwin_del(self):
            self.win.withdraw()
            win = MainWinDel()
            win.Window()
            win.win.mainloop()

        #delete
        self.bdelete = Button(self.win, text="Kontakt löschen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=mainwin_del)
        self.bdelete.place(x = 20, y = 328, width=190, height=40)

        self.tree = ttk.Treeview(self.win, columns=(1,2,3,4,5,6,7,), height= 5, show="headings")
        self.tree.place(x=220, y=140, width=520, height=220)

        #Add headings
        self.tree.heading(1, text="Vorname")
        self.tree.heading(2, text="Nachname")
        self.tree.heading(3, text="PLZ")
        self.tree.heading(4, text="Ort")
        self.tree.heading(5, text="Straße")
        self.tree.heading(6, text="Haus-Nr.")
        self.tree.heading(7, text="Tel.-Nr.")

        #define column width
        self.tree.column(1, width=40)
        self.tree.column(2, width=40)
        self.tree.column(3, width=20)
        self.tree.column(5, width=20)
        self.tree.column(5, width=20)
        self.tree.column(6, width=20)
        self.tree.column(7, width=20)


def main():
    win = MainWinQuery()
    win.Window()
    win.win.mainloop()

if __name__ == "__main__":
    main()

