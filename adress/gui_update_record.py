from tkinter import *
from tkinter import ttk 
import sqlite3
from adress.query_search_by import QuerySearchBy
from adress.update_for_gui import Updating

Profile = {1: ""}

class MainWinUpdate(QuerySearchBy, Updating):
    db_name = 'database/adress.db'
    def __init__(self):
        self.connection = sqlite3.connect("database/adress.db")
        self.wind = Tk()
        self.co0 = "#ffffff"
        self.co1 = "#000000"
        self.co2 = "#20214f"
        self.wind.geometry('800x600')
        self.wind.title ('Adress-Management')
        self.wind.configure(background=self.co0)
        self.wind.resizable(width=False, height=False)


    def MainWinUpdate(self):
        top = Frame(self.wind, width=800, height=50, bg=self.co2)
        top.grid(row=0, column=0, padx=0, pady=1)

        bottom = Frame(self.wind, width=800, height=140, bg=self.co2)
        bottom.place(x=0, y=540)

        header = Label(top, text="Adress-Management ✆", height=1, font=("Bahnschrift 22 bold"), bg= self.co2, fg=self.co0)
        header.place(x=280, y=2)

        self.tree = ttk.Treeview(self.wind, height=10,columns=(1,2,3,4,5,6,7,8,),show="headings")
        self.tree.place(x=220, y=140, width=520, height=220)
        self.tree.heading(1, text="ID")
        self.tree.heading(2, text="Vorname")
        self.tree.heading(3, text="Nachname")
        self.tree.heading(4, text="PLZ")
        self.tree.heading(5, text="Ort")
        self.tree.heading(6, text="Straße")
        self.tree.heading(7, text="Haus-Nr.")
        self.tree.heading(8, text="Tel.-Nr.")

        self.tree.column(1, width=2)
        self.tree.column(2, width=40)
        self.tree.column(3, width=48)
        self.tree.column(4, width=2)
        self.tree.column(5, width=20)
        self.tree.column(6, width=20)
        self.tree.column(7, width=20)
        self.tree.column(8, width=20)

        # Add Contact Button
        self.bAdd = Button(self.wind, text="Kontaktdaten aktualisieren", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.editing)
        self.bAdd.place(x = 480, y = 370, width=255, height=40)

        #Query
        self.bQuery = Button(self.wind, text="Kontakt abfragen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.Query_Win)
        self.bQuery.place(x = 20, y = 128, width=190, height=40)

        #Add
        self.bAdd = Button(self.wind, text="Kontakt hinzufügen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.Add_Win)
        self.bAdd.place(x = 20, y = 228, width=190, height=40)

        #delete
        self.bdelete = Button(self.wind, text="Kontakt löschen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.Delete_Win)
        self.bdelete.place(x = 20, y = 328, width=190, height=40)

        self.lbSearchByName = Label(self.wind, text="Suche nach Name:", font=("Calibri 16 bold"), bg=self.co0, fg=self.co1)
        self.lbSearchByName.place(x=200, y=60, width=200)
        self.entrySearchByName = Entry(self.wind)
        self.entrySearchByName.insert(0, "Vorname")
        self.entrySearchByName.bind("<Return>", self.SearchByName)
        self.entrySearchByName.place(x=400, y=60, width=160, height=30)


        self.lbSearchByLName = Label(self.wind, text="Suche nach Name:", font=("Calibri 16 bold"), bg=self.co0, fg=self.co1)
        self.lbSearchByLName.place(x=200, y=60, width=200)
        self.entrySearchByLName = Entry(self.wind)
        self.entrySearchByLName.insert(0, "Nachname")
        self.entrySearchByLName.bind("<Return>", self.SearchByName)
        self.entrySearchByLName.place(x=580, y=60, width=160, height=30)


    def Delete_Win(self):
        self.wind.withdraw()
        from delete_contact_gui import MainWinDelete
        win = MainWinDelete()
        win.Window()
        win.win.mainloop()

    def Add_Win(self):
        self.wind.withdraw()
        from add_contact_gui import MainWin
        win = MainWin()
        win.Window_Main()
        win.win.mainloop()


    def Query_Win(self):
        self.wind.withdraw()
        from gui_query import MainWinQuery
        win = MainWinQuery()
        win.Window()
        win.win.mainloop()


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


    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters)
            conn.commit()
        return query_result

    def editing(self):
        self.tree.item(self.tree.selection())['values'][0]

        self.F_Name = self.tree.item(self.tree.selection())['values'][1]
        self.L_Name = self.tree.item(self.tree.selection())['values'][2]
        self.PLZ = self.tree.item(self.tree.selection())['values'][3]
        self.ort = self.tree.item(self.tree.selection())['values'][4]
        self.street = self.tree.item(self.tree.selection())['values'][5]
        self.house_nr = self.tree.item(self.tree.selection())['values'][6]
        self.telefone = self.tree.item(self.tree.selection())['values'][7]

        self.edit_wind = Tk()
        self.edit_wind.title("EDIT-CONTACT")
        self.edit_wind.geometry('220x200')
        self.edit_wind.configure(background=self.co2)
        self.edit_wind.resizable(width=False, height=False)

        #FirstName
        Label (self.edit_wind, text='Vorname: ', bg=self.co2, fg=self.co0).grid(row=1, column=1)
        self.new_name = Entry(self.edit_wind)
        self.new_name.insert(0, "%s" %(self.F_Name))
        self.new_name.grid(row=1, column=2)

        #Nachname
        Label (self.edit_wind, text='Nachname: ', bg=self.co2, fg=self.co0).grid(row=2, column=1)
        self.lname = Entry(self.edit_wind)
        self.lname.insert(0, "%s" %(self.L_Name))
        self.lname.grid(row=2, column=2)

        #PLZ
        Label (self.edit_wind, text='PLZ: ', bg=self.co2, fg=self.co0).grid(row=3, column=1)
        self.plz_ = Entry(self.edit_wind)
        self.plz_.insert(0, "%s" %(self.PLZ))
        self.plz_.grid(row=3, column=2)

        #House Nr
        Label (self.edit_wind, text='Haus-Nr: ', bg=self.co2, fg=self.co0).grid(row=4, column=1)
        self.hNR = Entry(self.edit_wind)
        self.hNR.insert(0, "%s" %(self.house_nr))
        self.hNR.grid(row=4, column=2)

        #City
        Label (self.edit_wind, text='Ort: ', bg=self.co2, fg=self.co0).grid(row=5, column=1)
        self.city = Entry(self.edit_wind)
        self.city.insert(0, "%s" %(self.ort))
        self.city.grid(row=5, column=2)

        #Straße
        Label (self.edit_wind, text='Straße: ', bg=self.co2, fg=self.co0).grid(row=6, column=1)
        self.street_ = Entry(self.edit_wind)
        self.street_.insert(0, "%s" %(self.street))
        self.street_.grid(row=6, column=2)

        #Tel.:
        Label (self.edit_wind, text='Tel.: ', bg=self.co2, fg=self.co0).grid(row=7, column=1)
        self.phone_ = Entry(self.edit_wind)
        self.phone_.insert(0, "%s" %(self.telefone))
        self.phone_.grid(row=7, column=2)


        Button(self.edit_wind, text='Änderungen speichern', bg=self.co2, fg=self.co0, command=self.update_records).grid(row=8, column=2, sticky=W)
        self.edit_wind.mainloop()

    def update_records(self):        
        self.connection.cursor()
        self.update_FName(str(self.new_name.get()), str(self.F_Name))
        self.update_LName(str(self.lname.get()), str(self.L_Name))
        self.update_PostCode(str(self.plz_.get()), str(self.PLZ))
        self.update_City(str(self.city.get()), str(self.ort))
        self.update_Street(str(self.street_.get()), str(self.street))
        self.update_HNR(str(self.hNR.get()), str(self.house_nr))
        self.update_Tel(str(self.phone_.get()), str(self.telefone))
        self.connection.commit()
        self.edit_wind.destroy()
        self.viewing_records()

    def viewing_records(self):
        for x in self.tree.get_children():
            self.tree.delete(x)
        self.askin_all_query()
        for row in self.contact:
            self.tree.insert('', END, values=row)


if __name__ == '__main__':
    wind = MainWinUpdate()
    wind.MainWinUpdate()
    wind.wind.mainloop()
    