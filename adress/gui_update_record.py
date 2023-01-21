from tkinter import *
from tkinter import ttk 
import sqlite3
from query_search_by import QuerySearchBy

class MainWinUpdate(QuerySearchBy):
    db_name = 'database/adress.db'
    def __init__(self, wind):
        self.connection = sqlite3.connect("database/adress.db")
        self.wind = wind
        self.co0 = "#ffffff"
        self.co1 = "#000000"
        self.co2 = "#20214f"
        self.wind.geometry('800x600')
        self.wind.title ('Adress-Management')
        self.wind.configure(background=self.co0)
        self.wind.resizable(width=False, height=False)
    
    

        top = Frame(self.wind, width=800, height=50, bg=self.co2)
        top.grid(row=0, column=0, padx=0, pady=1)

        bottom = Frame(self.wind, width=800, height=140, bg=self.co2)
        bottom.place(x=0, y=540)

        header = Label(top, text="Adress-Management ✆", height=1, font=("Bahnschrift 22 bold"), bg= self.co2, fg=self.co0)
        header.place(x=280, y=2)

        self.tree = ttk.Treeview(height=10,columns=(1,2,3,4,5,6,7,8,),show="headings")
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
        self.bAdd = Button(self.wind, text="Kontakt aktualisieren", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.editing)
        self.bAdd.place(x = 480, y = 370, width=255, height=40)

        #Update
        self.bAdd = Button(self.wind, text="Kontakt aktualisieren", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0)
        self.bAdd.place(x = 20, y = 128, width=190, height=40)

        #Add
        self.bAdd = Button(self.wind, text="Kontakt hinzufügen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0)
        self.bAdd.place(x = 20, y = 228, width=190, height=40)

        #delete
        self.bdelete = Button(self.wind, text="Kontakt löschen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0)
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

        self.edit_wind = Toplevel()
        self.edit_wind.title('Editing')
        
        #FirstName
        Label (self.edit_wind, text='Vorname: ').grid(row=1, column=1)
        self.new_name = Entry(self.edit_wind)
        self.new_name.grid(row=1, column=2)

        #Nachname
        Label (self.edit_wind, text='Nachname: ').grid(row=2, column=1)
        self.lname = Entry(self.edit_wind)
        self.lname.grid(row=2, column=2)

        #PLZ
        Label (self.edit_wind, text='PLZ: ').grid(row=3, column=1)
        self.plz_ = Entry(self.edit_wind)
        self.plz_.grid(row=3, column=2)

        #House Nr
        Label (self.edit_wind, text='Haus-Nr: ').grid(row=4, column=1)
        self.hNR = Entry(self.edit_wind)
        self.hNR.grid(row=4, column=2)

        #City
        Label (self.edit_wind, text='Ort: ').grid(row=5, column=1)
        self.city = Entry(self.edit_wind)
        self.city.grid(row=5, column=2)

        #Straße
        Label (self.edit_wind, text='Straße: ').grid(row=6, column=1)
        self.street_ = Entry(self.edit_wind)
        self.street_.grid(row=6, column=2)

        #Tel.:
        Label (self.edit_wind, text='Tel.: ').grid(row=7, column=1)
        self.phone_ = Entry(self.edit_wind)
        self.phone_.grid(row=7, column=2)


        Button(self.edit_wind, text='Änderungen speichern', command=self.update_records).grid(row=8, column=2, sticky=W)
        self.edit_wind.mainloop()

    def update_records(self):        
        cur = self.connection.cursor()
        cur.execute("UPDATE Contact SET First_Name = ? WHERE First_Name = ?" , (str(self.new_name.get()), str(self.F_Name)))
        cur.execute("UPDATE Contact SET LastName = ? WHERE LastName = ?" , (str(self.lname.get()), str(self.L_Name)))
        cur.execute("UPDATE Adress SET PostCode = ? WHERE PostCode = ?" , (str(self.plz_.get()), str(self.PLZ)))
        cur.execute("UPDATE Adress SET City = ? WHERE City = ?" , (str(self.city.get()), str(self.ort)))
        cur.execute("UPDATE Adress SET Street = ? WHERE Street = ?" , (str(self.street_.get()), str(self.street)))
        cur.execute("UPDATE Adress SET HouseNumber = ? WHERE HouseNumber = ?" , (str(self.hNR.get()), str(self.house_nr)))
        cur.execute("UPDATE PhoneNumber SET PhoneNumber = ? WHERE PhoneNumber = ?" , (str(self.phone_.get()), str(self.telefone)))

        self.connection.commit()
        self.edit_wind.destroy()
        self.viewing_records()
        
    def viewing_records(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete (element)
        query = """Select 
	            c.ID,
	            c.First_Name,
	            c.LastName,
	            a.PostCode,
	            a.City,
	            a.Street,
	            a.HouseNumber,
	            p.PhoneNumber
                from Contact c
                join adress a on a.ID = c.ID
                join PhoneNumber p on c.ID = p.ID""" 
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('', END, values=row)


if __name__ == '__main__':
    wind = Tk()
    application = MainWinUpdate (wind)
    wind.mainloop()



