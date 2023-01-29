from tkinter import ttk 
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
from PIL import Image, ImageTk
from adress.query_search_by import QuerySearchBy
import sqlite3
from adress.gui_query import MainWinQuery

#load the image
Profile = {1: ""}

class MainWinDelete(QuerySearchBy):

    def __init__(self):
        """Initialize the database Connection and define Settings for the Window like color, geometry or Title"""
        self.connection = sqlite3.connect("database/adress_cat.db")
        self.win = Tk()
        self.win.title=("Adress-Management")
        self.win.geometry('800x600')
        self.co0 = "#ffffff"
        self.co1 = "#000000"
        self.co2 = "#20214f"
        self.win.configure(background=self.co0)
        self.win.resizable(width=False, height=False)
    
    def delete_contact(self):
        """Delete the Contact by selecting of Record"""
        self.idSelect = self.tree.item(self.tree.selection())['values'][0]
        self.get_id_ = self.get_name_id(self.name, self.lname)
        con = self.connection
        cur = con.cursor()
        cur.execute("delete from Contact where ID = {}".format(self.idSelect))
        cur.execute("Delete from Adress where Contact_ID = %s" %(self.get_id_)) 
        cur.execute("Delete from PhoneNumber where Contact_ID = %s" %(self.get_id_)) 
        cur.execute("Delete from Kategorie where Contact_ID = %s" %(self.get_id_)) 
        con.commit()
        self.tree.delete(self.tree.selection())


    def get_name_id(self, first_name, last_name):
        """Get the ID from the Contact by first and last name"""
        cur = self.connection.cursor()
        query = """
            SELECT 
	            c.ID 
            from Contact c
            join PhoneNumber a
                on c.ID=a.ID
            join Adress b
                on b.ID = c.ID
            join Kategorie d
                on c.ID = d.ID
            where First_Name like "%s" and LastName like "%s"
        """ %(first_name, last_name)
        cur.execute(query)
        ID = cur.fetchall()
        tup = ID[0]
        self.name_id  = int(tup[0])
        self.connection.commit()
        return self.name_id
    

    def query_contact(self):
        """Insert founded Records in treeview"""
        for x in self.tree.get_children():
            self.tree.delete(x)
        self.askin_all_query()
        for row in self.contact:
            self.tree.insert('', END, values=row)


    def SearchByName(self, event):
        """Search for records by name"""
        for x in self.tree.get_children():
            self.tree.delete(x)
        self.name = self.entrySearchByName.get()
        self.lname = self.entrySearchByLName.get()
        self.askin_query(self.name, self.lname)
        if not self.contact:
            messagebox.showinfo("Error", "Eintrag nicht vorhanden!")
        for row in self.contact:
            self.tree.insert('', END, values=row)


    def Add_Win(self):
        """Switch to Add Window"""
        self.win.withdraw()#destroy actual window
        from add_contact_gui import MainWin
        win = MainWin()
        win.Window_Main()
        win.win.mainloop()

    def Query_Win(self):
        """Switch to Query Window"""
        self.win.withdraw()#destroy actual window
        from gui_query import MainWinQuery
        win = MainWinQuery()
        win.Window()
        win.win.mainloop()

    def Update_Win(self):
        """Switch to Update Window"""
        self.win.withdraw()#destroy actual window
        from gui_update_record import MainWinUpdate
        wind = MainWinUpdate()
        wind.MainWinUpdate()
        wind.wind.mainloop()


    def Window(self):
        """Create the main window for the Delete Window Option"""
        top = Frame(self.win, width=800, height=50, bg=self.co2)
        top.grid(row=0, column=0, padx=0, pady=1)

        bottom = Frame(self.win, width=800, height=140, bg=self.co2)
        bottom.place(x=0, y=540)

        header = Label(top, text="Adress-Management ✆", height=1, font=("Bahnschrift 22 bold"), bg= self.co2, fg=self.co0)
        header.place(x=280, y=2)


        self.lbSearchByName = Label(self.win, text="Suche nach Name:", font=("Calibri 16 bold"), bg=self.co0, fg=self.co1)
        self.lbSearchByName.place(x=200, y=60, width=200)
        self.entrySearchByName = Entry(self.win)
        self.entrySearchByName.insert(0, "Vorname")
        self.entrySearchByName.bind("<Return>", self.SearchByName)
        self.entrySearchByName.place(x=400, y=60, width=160, height=30) #search for a record by First Name


        self.lbSearchByLName = Label(self.win, text="Suche nach Name:", font=("Calibri 16 bold"), bg=self.co0, fg=self.co1)
        self.lbSearchByLName.place(x=200, y=60, width=200)
        self.entrySearchByLName = Entry(self.win)
        self.entrySearchByLName.insert(0, "Nachname")
        self.entrySearchByLName.bind("<Return>", self.SearchByName)
        self.entrySearchByLName.place(x=580, y=60, width=160, height=30) #search for a record by Last Name
        
        #Delete Contact Button
        self.bAdd = Button(self.win, text="Kontakt löschen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.delete_contact)
        self.bAdd.place(x = 480, y = 370, width=255, height=40)

        #Update
        self.bAdd = Button(self.win, text="Kontakt aktualisieren", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.Update_Win)
        self.bAdd.place(x = 20, y = 128, width=190, height=40)

        #Add
        self.bAdd = Button(self.win, text="Kontakt hinzufügen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.Add_Win)
        self.bAdd.place(x = 20, y = 228, width=190, height=40)

        #query
        self.bquery = Button(self.win, text="Kontakt abfragen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.Query_Win)
        self.bquery.place(x = 20, y = 328, width=190, height=40)

        self.tree = ttk.Treeview(self.win, columns=(1,2,3,4,5,6,7,8,9,), height= 5, show="headings") #treeview
        self.tree.place(x=220, y=140, width=520, height=220)

        #Add headings
        self.tree.heading(1, text="ID")
        self.tree.heading(2, text="Vorname")
        self.tree.heading(3, text="Nachname")
        self.tree.heading(4, text="PLZ")
        self.tree.heading(5, text="Ort")
        self.tree.heading(6, text="Straße")
        self.tree.heading(7, text="Haus-Nr.")
        self.tree.heading(8, text="Tel.-Nr.")
        self.tree.heading(9, text="Kategorie")


        #define column width
        self.tree.column(1, width=2)
        self.tree.column(2, width=40)
        self.tree.column(3, width=48)
        self.tree.column(4, width=2)
        self.tree.column(5, width=20)
        self.tree.column(6, width=20)
        self.tree.column(7, width=20)
        self.tree.column(8, width=20)
        self.tree.column(9, width=20)


def main():
    win = MainWinDelete()
    win.Window()
    win.win.mainloop()

if __name__ == "__main__":
    main()

