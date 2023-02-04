from tkinter import *
from tkinter import ttk 
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
import re
from PIL import Image, ImageTk
from adress.query_search_by import QuerySearchBy
from adress.update_for_gui import Updating
from adress.add_second import AddSecondRecord
import os

Profile = {1: ""}


class MainWinUpdate(QuerySearchBy, Updating, AddSecondRecord):
    db_name = 'database/adress_cat.db'

    def __init__(self):
        self.connection = sqlite3.connect("database/adress_cat.db")  # connection to database 
        self.wind = Tk()  # create new Window
        self.co0 = "#ffffff"  # define colors
        self.co1 = "#000000"
        self.co2 = "#20214f"
        self.wind.geometry('800x600')  # define geometry
        self.wind.title ('Adress-Management')  # define title
        self.wind.configure(background=self.co0)  # define background
        self.wind.resizable(width=False, height=False)  # don't let the window resizing

    def MainWinUpdate(self):
        """Main Window of Update Adress"""
        top = Frame(self.wind, width=800, height=50, bg=self.co2)  # design top with blue box
        top.grid(row=0, column=0, padx=0, pady=1)

        bottom = Frame(self.wind, width=800, height=140, bg=self.co2)  # design button with blue box
        bottom.place(x=0, y=540)

        header = Label(top, text="Adress-Management ✆", height=1, font=("Bahnschrift 22 bold"), bg= self.co2, fg=self.co0)
        header.place(x=280, y=2)  # define header

        self.tree = ttk.Treeview(self.wind, height=10,columns=(1, 2, 3, 4, 5, 6, 7, 8, 9,),show="headings")  # treeview for records
        self.tree.place(x=220, y=140, width=574, height=220)  # place the treeview
        self.tree.heading(1, text="ID")  # define headers of treeview
        self.tree.heading(2, text="Vorname")
        self.tree.heading(3, text="Nachname")
        self.tree.heading(4, text="PLZ")
        self.tree.heading(5, text="Ort")
        self.tree.heading(6, text="Straße")
        self.tree.heading(7, text="Haus-Nr.")
        self.tree.heading(8, text="Tel.-Nr.")
        self.tree.heading(9, text="Kategorie")

        self.tree.column(1, width=2)
        self.tree.column(2, width=40)
        self.tree.column(3, width=48)
        self.tree.column(4, width=2)
        self.tree.column(5, width=20)
        self.tree.column(6, width=20)
        self.tree.column(7, width=20)
        self.tree.column(8, width=20)
        self.tree.column(9, width=20)

        # Update Contact Button
        self.bUpdate = Button(self.wind, text="Kontaktdaten aktualisieren", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.editing)
        self.bUpdate.place(x=538, y=370, width=255, height=40)

        # Query Button - switch to Query Win
        self.bQuery = Button(self.wind, text="Kontakt abfragen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.Query_Win)
        self.bQuery.place(x=20, y=128, width=190, height=40)

        # Add 2nd Tel.-Nr. Button
        self.bTel = Button(self.wind, text="Tel.-Nr. hinzufügen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.add_tel)
        self.bTel.place(x=20, y=428, width=174, height=40)

        # Add 2nd Adress Button
        self.bTel = Button(self.wind, text="Adresse hinzufügen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.add_adress)
        self.bTel.place(x=220, y=428, width=174, height=40)


        # Add Button - switch to Add Win
        self.bAdd = Button(self.wind, text="Kontakt hinzufügen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.Add_Win)
        self.bAdd.place(x=20, y=228, width=190, height=40)

        # Delete Button - switch to Delete Win
        self.bdelete = Button(self.wind, text="Kontakt löschen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.Delete_Win)
        self.bdelete.place(x=20, y=328, width=190, height=40)

        # Update Category
        self.bCategory = Button(self.wind, text="Kategorie ändern", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.combo_)
        self.bCategory.place(x=420, y=428, width=174, height=40)

        # Update Photo
        self.bPhoto = Button(self.wind, text="Photo ändern", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.photo_update)
        self.bPhoto.place(x=620, y=428, width=174, height=40)


        self.lbSearchByName = Label(self.wind, text="Suche nach Name:", font=("Calibri 16 bold"), bg=self.co0, fg=self.co1)  # Label for Name Searching (First Name)
        self.lbSearchByName.place(x=200, y=60, width=200)
        self.entrySearchByName = Entry(self.wind)
        self.entrySearchByName.insert(0, "Vorname")
        self.entrySearchByName.bind("<Return>", self.SearchByName)  # define function for the name searching
        self.entrySearchByName.place(x=400, y=60, width=160, height=30)

        self.lbSearchByLName = Label(self.wind, text="Suche nach Name:", font=("Calibri 16 bold"), bg=self.co0, fg=self.co1)  # Label for Name Searching (Last Name)
        self.lbSearchByLName.place(x=200, y=60, width=200)
        self.entrySearchByLName = Entry(self.wind)
        self.entrySearchByLName.insert(0, "Nachname")
        self.entrySearchByLName.bind("<Return>", self.SearchByName)  # define function for the name searching
        self.entrySearchByLName.place(x=580, y=60, width=160, height=30)

    def Delete_Win(self):
        """Switch to Delete Window"""
        self.wind.withdraw()
        from delete_contact_gui import MainWinDelete
        win = MainWinDelete()
        win.Window()
        win.win.mainloop()

    def Add_Win(self): 
        """Switch to Add Window"""
        self.wind.withdraw()
        from add_contact_gui import MainWin
        win = MainWin()
        win.Window_Main()
        win.win.mainloop()

    def Query_Win(self):
        """Switch to Query Window"""
        self.wind.withdraw()
        from gui_query import MainWinQuery
        win = MainWinQuery()
        win.Window()
        win.win.mainloop()

    def query_contact(self):
        """Ask for a contact and get the records"""
        for x in self.tree.get_children():
            self.tree.delete(x)
        self.askin_all_query()
        for row in self.contact:
            self.tree.insert('', END, values=row)

    def SearchByName(self, event):
        """Search for record by name"""
        for x in self.tree.get_children():
            self.tree.delete(x)
        name = self.entrySearchByName.get()
        lname = self.entrySearchByLName.get()
        if name == '' or lname == '':
            messagebox.showwarning("Warning", "Bitte Vor- und Nachname eingeben!")
        self.askin_query(name, lname)
        if not self.contact and not name == '' and not lname == '':
            messagebox.showinfo("Info", "Eintrag nicht vorhanden!")
        for row in self.contact:
            self.tree.insert('', END, values=row)

    def run_query(self, query, parameters=()):
        """Let the query run"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters)
            conn.commit()
        return query_result
    
    #------------------------------Edit-Photo--------------------------------------------------#

    def photo_update(self):
        """Update the Photo."""
        self.root = tk.Tk()  # new window
        self.root.configure(background=self.co0)
        self.root.resizable(False, False)
        self.lblPhoto = Label(self.root, text="Photo: ",  font=("Calibri 14 bold"), bg=self.co0, fg=self.co1)
        self.lblPhoto.place(x=10, y=20, width=60, height=20)
        self.l = Label(self.root, bg=self.co2)
        self.l.place(x=0, y=0, width=200, height=20)
        self.lb = Label(self.root, bg=self.co2)
        self.lb.place(x=0, y=180, width=200, height=40)
        self.lbl = Label(self.root, text="📸",  font=("Calibri 40"), bg=self.co0)
        self.lbl.place(x=66, y=80, width=60, height=48)
        self.entryPhoto = Entry(self.root)
        self.entryPhoto.place(x=10, y=40, width=170, height=22)
        button = Button(self.root, text="Browse", command=self.BrowsePhoto, bg=self.co2, fg=self.co0)
        button.place(x=10, y=128, width= 170, height=22)
        button1 = Button(self.root, text="Übernehmen", command=self.ok, bg=self.co2, fg=self.co0)
        button1.place(x=10, y=148, width= 170, height=22)
       

    def ok(self):
        self.idSelect =  self.tree.item(self.tree.selection())['values'][0] # let set the record
        self.GetFN = self.tree.item(self.tree.selection())['values'][1]  # get the name
        self.GetLN = self.tree.item(self.tree.selection())['values'][2]
        self.imgProfile="img/img_/profile_" + str(self.idSelect) + "." + "jpg"
        os.remove(self.imgProfile)
        id = self.get_name_id(self.GetFN, self.GetLN)
        filename = self.entryPhoto.get()
        im = Image.open(filename)
        rgb_im = im.convert('RGB')
        rgb_im.save(("img/img_/profile_" + str(id) + "." + "jpg"))  # save the selected image
        self.root.destroy()
        

    def BrowsePhoto(self):
        """Allows to search for a photo"""
        self.entryPhoto.delete(0, END)
        filename = filedialog.askopenfilename(initialdir="/", title="Select File")
        return self.entryPhoto.insert(END, filename)

    #------------------------------Edit-Category--------------------------------------------------#

    def combo_(self):
        """Define the combo box"""
        self.tree.item(self.tree.selection())['values'][0] # let set the record
        self.GetFName_ = self.tree.item(self.tree.selection())['values'][1]  # get the name
        self.GetLName_ = self.tree.item(self.tree.selection())['values'][2]

        self.root = tk.Tk()  # new window
        self.root.configure(background=self.co0)
        self.root.geometry("180x120")
        self.root.resizable(False, False)
        self.combo = ttk.Combobox(self.root, values=["Familie", "Freunde", "Schule", "Arbeit"])
        self.combo.place(x=20, y=20, width= 140, height=22)
        self.combo.current(0)  # setting default value
        ok_button = tk.Button(self.root, bg=self.co2, fg=self.co0, text="OK", command=self.save_close)
        ok_button.place(x=50, y=70, width= 70, height=22)
        self.l = Label(self.root, bg=self.co2)
        self.l.place(x=0, y=0, width=200, height=10)
        self.lbl = Label(self.root, bg=self.co2)
        self.lbl.place(x=0, y=110, width=200, height=10)
        self.root.mainloop()

    def save_close(self):
        """Save the updated category and close the window"""
        FirstName = self.GetFName_
        LastName = self.GetLName_

        self.selected = self.combo.get()
        self.get_name_id(FirstName, LastName)
        self.update_Category(self.selected, self.name_id)
        self.connection.commit()
        self.root.destroy()
        self.get_id(FirstName, LastName)
        self.viewing_records()


    #----------------------Add-Second-Adress------------------------------------------#

    def add_adress(self):
        """Window for adding another adress to Contact"""
        self.tree.item(self.tree.selection())['values'][0]#let set the contact
        self.GetFName = self.tree.item(self.tree.selection())['values'][1]#get the name
        self.GetLName = self.tree.item(self.tree.selection())['values'][2]

        self.new = Tk()
        self.new.title("Add-Second Tel.-Nr")
        self.new.geometry('220x180')
        self.new.configure(background=self.co0)
        self.new.resizable(width=False, height=False)

        # PLZ
        label = Label (self.new, text='PLZ: ', bg=self.co0, fg=self.co1)
        label.place(x=10, y=20, width= 40, height=22)
        self.postcode = Entry(self.new)
        self.postcode.place(x=60, y=20, width= 128, height=22)

        # House Nr
        l = Label (self.new, text='Haus-Nr: ', bg=self.co0, fg=self.co1)
        l.place(x=6, y=50, width= 60, height=22)
        self.housenumber = Entry(self.new)
        self.housenumber.place(x=60, y=50, width= 128, height=22)

        # City
        lb = Label (self.new, text='Ort: ', bg=self.co0, fg=self.co1)
        lb.place(x=10, y=80, width= 40, height=22)
        self.CITY = Entry(self.new)
        self.CITY.place(x=60, y=80, width= 128, height=22)

        # Straße
        lbl = Label (self.new, text='Straße: ', bg=self.co0, fg=self.co1)
        lbl.place(x=10, y=110, width= 40, height=22)
        self.STREET = Entry(self.new)
        self.STREET.place(x=60, y=110, width= 128, height=22)

        self.l = Label(self.new, bg=self.co2)
        self.l.place(x=0, y=0, width=280, height=10)
        self.lbl = Label(self.new, bg=self.co2)
        self.lbl.place(x=0, y=170, width=280, height=10)

        button = Button(self.new, text='Änderungen speichern', bg=self.co2, fg=self.co0, command=self.adding_adress)
        button.place(x=60, y=140, width= 128, height=22)

        self.new.mainloop()

    
    def adding_adress(self):
        """Add another Adress to Contact"""
        FirstName = self.GetFName
        LastName = self.GetLName

        plz = self.postcode.get()
        housenr = self.housenumber.get()
        city = self.CITY.get()
        street = self.STREET.get()

        if plz == '' or city == '' or street == '' or housenr == '':
            messagebox.showwarning("Warning", "Feld darf nicht leer sein")  # raise messagebox if entry is empty
        elif not re.search(r'^\d{4}$', plz):
            messagebox.showerror("Error", "Bitte geben Sie eine gültige PLZ ein.")  # raise messagebox if user uses wrong PostCode
        elif not city.strip().isalpha() or not street.isalpha():
            messagebox.showwarning("Warning", "Bitte Datentyp beachten!")
        elif not housenr.strip().isnumeric():
            messagebox.showwarning("Warning", "Bitte Datentyp beachten!")
        else: 
            self.get_name_id(FirstName, LastName)
            self.add_adress_(str(plz), str(street), str(city), str(housenr))
            self.new.destroy()

    #------------------------Add-Second-TelefoneNumber------------------------------------#    
    def add_tel(self):
        """Add another telefone to contact"""
        self.tree.item(self.tree.selection())['values'][0]#let the record select
        self.Get_FName = self.tree.item(self.tree.selection())['values'][1]#get the name
        self.Get_LName = self.tree.item(self.tree.selection())['values'][2]

        self.window = Tk()
        self.window.title("Add-Second Tel.-Nr")
        self.window.geometry('220x120')
        self.window.configure(background=self.co0)
        self.window.resizable(width=False, height=False)

        # Tel.:
        lb = Label (self.window, text='Tel.: ', bg=self.co0, fg=self.co1)
        lb.place(x=10, y=28, width= 28, height=22)
        self.get_phone = Entry(self.window)
        self.get_phone.place(x=40, y=28, width= 140, height=22)

        self.l = Label(self.window, bg=self.co2)
        self.l.place(x=0, y=0, width=280, height=10)
        self.lbl = Label(self.window, bg=self.co2)
        self.lbl.place(x=0, y=110, width=280, height=10)

        button = Button(self.window, text='Änderungen speichern', bg=self.co2, fg=self.co0, command=self.adding_tel)
        button.place(x=40, y=80, width= 138, height=22)
        self.window.mainloop()

        

    def adding_tel(self):
        Fname = self.Get_FName
        Lname = self.Get_LName
        phone = self.get_phone.get()
        if phone == '':
            messagebox.showwarning("Warning", "Feld darf nicht leer sein")  # raise messagebox if entry is empty
        elif not phone.strip().isnumeric():
            messagebox.showwarning("Warning", "Bitte Datentyp beachten!")
        else:
            self.get_name_id(Fname, Lname)
            self.add_phone(str(phone))
            self.window.destroy()

    #---------------------------------------------Edit-Entry----------------------------------------------------#

    def editing(self):
        """Edit records in database"""
        self.tree.item(self.tree.selection())['values'][0]  # let the record select

        # select records like Name, Adress, Telefone
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

        # FirstName
        Label (self.edit_wind, text='Vorname: ', bg=self.co2, fg=self.co0).grid(row=1, column=1)
        self.new_name = Entry(self.edit_wind)
        self.new_name.insert(0, "%s" % (self.F_Name))
        self.new_name.grid(row=1, column=2)

        # Nachname
        Label (self.edit_wind, text='Nachname: ', bg=self.co2, fg=self.co0).grid(row=2, column=1)
        self.lname = Entry(self.edit_wind)
        self.lname.insert(0, "%s" % (self.L_Name))
        self.lname.grid(row=2, column=2)

        # PLZ
        Label (self.edit_wind, text='PLZ: ', bg=self.co2, fg=self.co0).grid(row=3, column=1)
        self.plz_ = Entry(self.edit_wind)
        self.plz_.insert(0, "%s" % (self.PLZ))
        self.plz_.grid(row=3, column=2)

        # House Nr
        Label (self.edit_wind, text='Haus-Nr: ', bg=self.co2, fg=self.co0).grid(row=4, column=1)
        self.hNR = Entry(self.edit_wind)
        self.hNR.insert(0, "%s" % (self.house_nr))
        self.hNR.grid(row=4, column=2)

        # City
        Label (self.edit_wind, text='Ort: ', bg=self.co2, fg=self.co0).grid(row=5, column=1)
        self.city = Entry(self.edit_wind)
        self.city.insert(0, "%s" % (self.ort))
        self.city.grid(row=5, column=2)

        # Straße
        Label (self.edit_wind, text='Straße: ', bg=self.co2, fg=self.co0).grid(row=6, column=1)
        self.street_ = Entry(self.edit_wind)
        self.street_.insert(0, "%s" % (self.street))
        self.street_.grid(row=6, column=2)

        # Tel.:
        Label (self.edit_wind, text='Tel.: ', bg=self.co2, fg=self.co0).grid(row=7, column=1)
        self.phone_ = Entry(self.edit_wind)
        self.phone_.insert(0, "%s" % (self.telefone))
        self.phone_.grid(row=7, column=2)


        Button(self.edit_wind, text='Änderungen speichern', bg=self.co2, fg=self.co0, command=self.update_records).grid(row=8, column=2, sticky=W)
        self.edit_wind.mainloop()

    def update_records(self):  
        """Update the records"""   
        if self.new_name.get() == '' or self.lname.get() == '' or self.plz_.get() == '' or self.city.get() == '' or self.street_.get() == '' or self.hNR.get() == '' or self.phone_.get() == '':
            messagebox.showwarning("Warning", "Feld darf nicht leer sein")  # raise messagebox if entry is empty
            self.edit_wind.destroy()
        elif not re.search(r'^\d{4}$', self.plz_.get()):
            messagebox.showerror("Error", "Bitte geben Sie eine gültige PLZ ein.")  # raise messagebox if user uses wrong PostCode
            self.edit_wind.destroy()
        elif not self.new_name.get().strip().isalpha() or not self.lname.get().strip().isalpha() or not self.city.get().strip().isalpha() or not self.street_.get().isalpha():
            messagebox.showwarning("Warning", "Bitte Datentyp beachten!")
            self.edit_wind.destroy()
        elif not self.hNR.get().strip().isnumeric() or not self.phone_.get().strip().isnumeric():
            messagebox.showwarning("Warning", "Bitte Datentyp beachten!")
            self.edit_wind.destroy()
        else: 
            self.get_name_id(self.F_Name, self.L_Name) 
            self.get_id(self.F_Name, self.L_Name)
            self.update_FName(str(self.new_name.get()), self.My_ID)
            self.update_LName(str(self.lname.get()), self.My_ID)
            self.update_PostCode(str(self.plz_.get()), self.name_id, str(self.PLZ))
            self.update_City(str(self.city.get()), self.name_id, str(self.ort))
            self.update_Street(str(self.street_.get()), self.name_id, str(self.street))
            self.update_HNR(str(self.hNR.get()), self.name_id, str(self.house_nr))
            self.update_Tel(str(self.phone_.get()), self.name_id, str(self.telefone))
            self.edit_wind.destroy()
            self.viewing_records()

    def viewing_records(self):
        """Show the records"""
        for x in self.tree.get_children():
            self.tree.delete(x)
        self.askin_by_id(self.My_ID)
        for row in self.contact:
            self.tree.insert('', END, values=row)


if __name__ == '__main__':
    wind = MainWinUpdate()
    wind.MainWinUpdate()
    wind.wind.mainloop()
    