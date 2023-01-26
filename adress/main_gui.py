from tkinter import ttk 
from tkinter import *

from tkinter import filedialog
from PIL import Image, ImageTk
import sqlite3
from calculate_id import CalculateID
from insert_query import Add
from query import Ask
from query_search_by import QuerySearchBy



class Win():

    def __init__(self):
        self.win = Tk()
        self.win.title=("Adress-Management")
        self.win.geometry('800x600')
        self.co0 = "#ffffff"
        self.co1 = "#000000"
        self.co2 = "#20214f"
        self.win.configure(background=self.co0)
        self.win.resizable(width=False, height=False)

    
    def Delete_Win(self):
        self.win.withdraw()
        from delete_contact_gui import MainWinDelete
        win = MainWinDelete()
        win.Window()
        win.win.mainloop()

    def Add_Win(self):
        self.win.withdraw()
        from add_contact_gui import MainWin
        win = MainWin()
        win.Window_Main()
        win.win.mainloop()


    def Query_Win(self):
        self.win.withdraw()
        from gui_query import MainWinQuery
        win = MainWinQuery()
        win.Window()
        win.win.mainloop()

    def Update_Win(self):
        self.win.withdraw()
        from gui_update_record import MainWinUpdate
        wind = MainWinUpdate()
        wind.MainWinUpdate()
        wind.wind.mainloop()


    def Window(self):
        #top
        top = Frame(self.win, width=800, height=50, bg=self.co2)
        top.grid(row=0, column=0, padx=0, pady=1)

        #bottom
        bottom = Frame(self.win, width=800, height=150, bg=self.co2)
        bottom.place(x=0, y=480)

        #header
        header = Label(top, text="Adress-Management ✆", height=1, font=("Bahnschrift 22 bold"), bg= self.co2, fg=self.co0)
        header.place(x=280, y=2)

        # Instruction
        center = Label(text="Bitte wählen Sie Ihre gewünschte Aktion", height=1, font=("Calibri 18 bold"), bg= self.co0, fg=self.co1)
        center.place(x=220, y=80)

        # Add Contact Button
        self.bAdd = Button(self.win, text="Kontakt Hinzufügen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.Add_Win)
        self.bAdd.place(x = 290, y = 140, width=260, height=40)

        # Update Button
        self.bUpdate = Button(self.win, text="Kontakt Aktualisieren", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.Update_Win)
        self.bUpdate.place(x = 290, y = 200, width=260, height=40)

        # Query Button
        self.bQuery = Button(self.win, text="Kontakt Abfragen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.Query_Win)
        self.bQuery.place(x = 290, y = 260, width=260, height=40)

        #Delete Button
        self.bDelete = Button(self.win, text="Kontakt Löschen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.Delete_Win)
        self.bDelete.place(x = 290, y = 320, width=260, height=40)

       
def main():
    win = Win()
    win.Window()
    win.win.mainloop()

if __name__ == "__main__":
    main()

