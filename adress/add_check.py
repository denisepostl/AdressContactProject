import sqlite3
from tkinter import messagebox

class Checking():
    """Checking Class."""

    def __init__(self):
        """Initialize connection do database"""
        self.connection = sqlite3.connect("database/adress_cat.db")

    def check_for_same_tel(self, same_phone):
        """Method for searching for same phone"""
        cur = self.connection.cursor()
        query = """
                SELECT
	                a.PhoneNumber
                from PhoneNumber a 
                where a.PhoneNumber like %s
        """% (same_phone)
        cur.execute(query)
        self.same_phone_ = cur.fetchall()
        return self.same_phone_
       

    def check_for_same_name(self, first_name, last_name):
        """Method for searching for same name"""
        cur = self.connection.cursor()
        query = """
                SELECT
	                First_Name,
	                LastName
                from Contact 
                where First_Name like "%s" and LastName like "%s"
        """%(first_name, last_name,)
        cur.execute(query)
        self.name = cur.fetchall()
        self.connection.commit()
        return self.name
