import sqlite3

class QuerySearchBy():

    def __init__(self):
        self.connection = sqlite3.connect("database/adress.db")


    def askin_query(self, first_name, last_name):
        cur = self.connection.cursor()
        query = """
            SELECT
                a.ID,
	            a.First_Name,
	            a.LastName,
                b.PostCode,
                b.City,
	            b.Street,
	            b.HouseNumber,
	            c.PhoneNumber,
                d.Kategorie
            from Contact a
            join Adress b
	            on a.ID = b.Contact_ID
            join PhoneNumber c
	            on a.ID = c.Contact_ID
            join Kategorie d
                on d.ID = a.ID
            where First_Name like "%s" and LastName like "%s" """ %(first_name, last_name,)
        
        cur.execute(query)
        self.contact = cur.fetchall()
        self.connection.commit()

    def askin_phone_query(self, phone):
        cur = self.connection.cursor()
        query = """
            SELECT
                a.ID,
	            a.First_Name,
	            a.LastName,
                b.PostCode,
                b.City,
	            b.Street,
	            b.HouseNumber,
	            c.PhoneNumber,
                d.Kategorie
            from Contact a
            join Adress b
	            on a.ID = b.Contact_ID
            join PhoneNumber c
	            on a.ID = c.Contact_ID
            join Kategorie d
                on d.ID = a.ID
            where PhoneNumber like "%s" """ %(phone,)
        
        cur.execute(query)
        self.contact = cur.fetchall()
        self.connection.commit()
        
    
    def askin_all_query(self):
        cur = self.connection.cursor()
        query = """
            SELECT
                a.ID,
	            a.First_Name,
	            a.LastName,
                b.PostCode,
                b.City,
	            b.Street,
	            b.HouseNumber,
	            c.PhoneNumber,
                d.Kategorie
            from Contact a
            join Adress b
	            on a.ID = b.Contact_ID
            join PhoneNumber c
	            on a.ID = c.Contact_ID 
            join Kategorie d
                on d.ID = a.ID""" 
        
        cur.execute(query)
        self.contact = cur.fetchall()
        self.connection.commit()
