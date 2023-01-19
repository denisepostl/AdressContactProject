import sqlite3

class Ask():

    def __init__(self):
        self.connection = sqlite3.connect("database/adress.db")


    def askin(self, first_name, last_name):
        cur = self.connection.cursor()
        query = """
            SELECT
	            a.First_Name,
	            a.LastName,
	            b.Street,
	            b.PostCode,
	            b.City,
	            b.HouseNumber,
	            c.PhoneNumber
            from Contact a
            join Adress b
	            on a.ID = b.Contact_ID
            join PhoneNumber c
	            on a.ID = c.Contact_ID
            where First_Name like "%s"
            and LastName like "%s"; """ %(first_name, last_name)
        
        cur.execute(query)
        contacts = cur.fetchall()
        self.connection.commit()
        for self.contact in contacts:
            return self.contact
        

    def askin_all(self):
        print("Vorname | Nachname |    Straße    |    PLZ    |    Ort    |   Haus-Nr.   |  Tel.:  |")
        cur = self.connection.cursor()
        query = """
            SELECT
	            a.First_Name,
	            a.LastName,
	            b.Street,
	            b.PostCode,
	            b.City,
	            b.HouseNumber,
	            c.PhoneNumber
            from Contact a
            join Adress b
	            on a.ID = b.Contact_ID
            join PhoneNumber c
	            on a.ID = c.Contact_ID """ 
        
        cur.execute(query)
        contacts = cur.fetchall()
        self.connection.commit()
        
        for contact in contacts:
            print(contact)
        
        return "--------------------------------------------------------"
