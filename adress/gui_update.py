from tkinter import ttk 
from tkinter import *

from tkinter import filedialog
from PIL import Image, ImageTk
import sqlite3
from calculate_id import CalculateID
from query_search_by import QuerySearchBy
from query import Ask

class MainWin(Ask, QuerySearchBy):

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


    def add_contact(self):
        cur = self.connection.cursor()
        self.FName = self.entryFName.get()
        self.LName = self.entryName.get()
        self.Ort = self.entryOrt.get()
        self.PLZ = self.entryPLZ.get()
        self.HNR = self.entryHNR.get()
        self.Str = self.entryStr.get()
        self.Phone = self.entryPhone.get()

        self.FName = self.entryFName.get()
        self.LName = self.entryName.get()
        self.Ort = self.entryOrt.get()
        self.PLZ = self.entryPLZ.get()
        self.HNR = self.entryHNR.get()
        self.Str = self.entryStr.get()
        self.Phone = self.entryPhone.get()

        cur.execute("INSERT INTO Contact ('First_Name', 'LastName') values(?,?)", (self.FName, self.LName))
        contact_id = cur.lastrowid
        cur.execute("INSERT INTO Adress ('Street', 'PostCode', 'City', 'Housenumber', 'Contact_ID') values(?,?,?,?,?)", (self.Str, self.Ort, self.PLZ, self.HNR, contact_id))
        cur.execute("INSERT INTO PhoneNumber ('PhoneNumber', 'Contact_ID') values(?,?)", (self.Phone, contact_id))
        self.connection.commit()

        select = cur.execute("SELECT * FROM Contact order by id desc")
        select = list(select)
        id = select[0][0]
        filename = self.entryPhoto.get()
        im = Image.open(filename)
        rgb_im = im.convert('RGB')
        rgb_im.save(("img/profile_" + str(id) + "." + "jpg"))
   

    def BrowsePhoto(self):
        self.entryPhoto.delete(0, END)
        filename = filedialog.askopenfilename(initialdir="/", title="Select File")
        return self.entryPhoto.insert(END, filename)

    
    def SearchByName(self, event):
        for x in self.tree.get_children():
            self.tree.delete(x)
        name = self.entrySearchByName.get()
        lname = self.entrySearchByLName.get()
        self.askin_query(name, lname)
        for row in self.contact:
            self.tree.insert('', END, values=row)
        

    def Window_Main(self):
        top = Frame(self.win, width=800, height=50, bg=self.co2)
        top.grid(row=0, column=0, padx=0, pady=1)

        bottom = Frame(self.win, width=800, height=150, bg=self.co2)
        bottom.place(x=0, y=480)

        header = Label(top, text="Adress-Management ✆", height=1, font=("Bahnschrift 22 bold"), bg= self.co2, fg=self.co0)
        header.place(x=280, y=2)

        #First Name
        self.lblFName = Label(self.win, text="Vorname: ", font=("Calibri 14 bold"), bg=self.co0, fg=self.co1)
        self.lblFName.place(x=240, y=70, width=125)
        self.entryFName = Entry(self.win)
        self.entryFName.place(x=263, y=100, width=200, height=30)

        #Last Name
        self.lblName = Label(self.win, text="Nachname: ", font=("Calibri 14 bold"), bg=self.co0, fg=self.co1)
        self.lblName.place(x=480, y=70, width=125)
        self.entryName = Entry(self.win)
        self.entryName.place(x=496, y=100, width=200, height=30)

        #PLZ
        self.lblPLZ = Label(self.win, text="PLZ: ", font=("Calibri 14 bold"), bg=self.co0, fg=self.co1)
        self.lblPLZ.place(x=220, y=140, width=125)
        self.entryPLZ = Entry(self.win)
        self.entryPLZ.place(x=263, y=170, width=200, height=30)

        #Street
        self.lblStr = Label(self.win, text="Straße: ", font=("Calibri 14 bold"), bg=self.co0, fg=self.co1)
        self.lblStr.place(x=464, y=140, width=125)
        self.entryStr = Entry(self.win)
        self.entryStr.place(x=496, y=170, width=200, height=30)


        self.lbSearchByName = Label(self.win, text="Suche nach Name:", font=("Calibri 16 bold"), bg=self.co0, fg=self.co1)
        self.lbSearchByName.place(x=10, y=370, width=200)
        self.entrySearchByName = Entry(self.win)
        self.entrySearchByName.insert(0, "Vorname")
        self.entrySearchByName.bind("<Return>", self.SearchByName)
        self.entrySearchByName.place(x=220, y=380, width=160, height=30)


        self.lbSearchByLName = Label(self.win, text="Suche nach Name:", font=("Calibri 16 bold"), bg=self.co0, fg=self.co1)
        self.lbSearchByLName.place(x=10, y=370, width=200)
        self.entrySearchByLName = Entry(self.win)
        self.entrySearchByLName.insert(0, "Nachname")
        self.entrySearchByLName.bind("<Return>", self.SearchByName)
        self.entrySearchByLName.place(x=220, y=420, width=160, height=30)


        #City
        self.lblOrt = Label(self.win, text="Ort: ", font=("Calibri 14 bold"), bg=self.co0, fg=self.co1)
        self.lblOrt.place(x=220, y=210, width=125)
        self.entryOrt = Entry(self.win)
        self.entryOrt.place(x=263, y=240, width=200, height=30)

        #Housenumber
        self.lblHNR = Label(self.win, text="Haus-Nr.: ", font=("Calibri 14 bold"), bg=self.co0, fg=self.co1)
        self.lblHNR.place(x=472, y=210, width=125)
        self.entryHNR = Entry(self.win)
        self.entryHNR.place(x=496, y=240, width=200, height=30)

        #Phone
        self.lblPhone = Label(self.win, text="Tel.: ", font=("Calibri 14 bold"), bg=self.co0, fg=self.co1)
        self.lblPhone.place(x=222, y=280, width=125, height=30)
        self.entryPhone = Entry(self.win)
        self.entryPhone.place(x=263, y=310, width=200, height=30)

        #Photo
        self.lblPhoto = Label(self.win, text="Photo: ",  font=("Calibri 14 bold"), bg=self.co0, fg=self.co1)
        self.lblPhoto.place(x=462, y=280, width=125, height=30)
        self.bPhoto = Button(self.win, text="Browse", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.BrowsePhoto)
        self.bPhoto.place(x=620, y=350, height=30)
        self.entryPhoto = Entry(self.win)
        self.entryPhoto.place(x=496, y=310, width=200, height=30)

        # Add Contact Button
        self.bAdd = Button(self.win, text="Update Kontakt", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.add_contact)
        self.bAdd.place(x = 480, y = 410, width=255, height=40)

        # Update Button
        self.bUpdate = Button(self.win, text="Update Contact", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0)
        self.bUpdate.place(x = 20, y = 100, width=180, height=40)

        # Query Button
        self.bQuery = Button(self.win, text="Query Contact", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0)
        self.bQuery.place(x = 20, y = 200, width=180, height=40)

        #Delete Button
        self.bDelete = Button(self.win, text="Delete Contact", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0)
        self.bDelete.place(x = 20, y = 300, width=180, height=40)

        self.tree = ttk.Treeview(self.win, columns=(1,2,3,4,5,6,7,8,), height= 5, show="headings")
        self.tree.place(x=40, y=500, width=690, height=80)

        #Add headings
        self.tree.heading(1, text="ID")
        self.tree.heading(2, text="Vorname")
        self.tree.heading(3, text="Nachname")
        self.tree.heading(4, text="PLZ")
        self.tree.heading(5, text="Ort")
        self.tree.heading(6, text="Straße")
        self.tree.heading(7, text="Haus-Nr.")
        self.tree.heading(8, text="Tel.-Nr.")

        #define column width
        self.tree.column(1, width=2)
        self.tree.column(2, width=40)
        self.tree.column(3, width=48)
        self.tree.column(4, width=2)
        self.tree.column(5, width=20)
        self.tree.column(6, width=20)
        self.tree.column(7, width=20)
        self.tree.column(8, width=20)


       
def Delete():
    pass

def main():
    win = MainWin()
    win.Window_Main()
    win.win.mainloop()

if __name__ == "__main__":
    main()

