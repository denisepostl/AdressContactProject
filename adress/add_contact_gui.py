from tkinter import ttk 
from tkinter import *

from tkinter import filedialog
from PIL import Image, ImageTk
import sqlite3
from calculate_id import CalculateID
from query import Ask

class MainWin(Ask):

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
   

    def BrowsePhoto(self):
        self.entryPhoto.delete(0, END)
        filename = filedialog.askopenfilename(initialdir="/", title="Select File")
        return self.entryPhoto.insert(END, filename)
        

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
        self.bAdd = Button(self.win, text="Add Contact", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.add_contact)
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

       
def Delete():
    pass

def main():
    win = MainWin()
    win.Window_Main()
    win.win.mainloop()

if __name__ == "__main__":
    main()

