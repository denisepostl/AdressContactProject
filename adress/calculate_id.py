import sqlite3

class CalculateID:

    def __init__(self):
        self.connection = sqlite3.connect("database/adress.db")
    
    def calculate_phone_id(self): 
        """This method calculates the phone_id that the user can add contacts comfortable."""
        cur = self.connection.cursor()
        id = """
            SELECT 
                Max(ID)
            from PhoneNumber
        """
        cur.execute(id)
        ID = cur.fetchall()
        tup = ID[0]
        self.New_ID = int(tup[0]) + int(1)
        self.connection.commit()

    def calculate_contact_id(self): 
        """This method calculates the contact_id that the user can add contacts comfortable."""
        cur = self.connection.cursor()
        id = """
            SELECT 
                Max(ID)
            from Contact
        """
        cur.execute(id)
        ID = cur.fetchall()
        tup = ID[0]
        self.My_ID = int(tup[0]) + int(1)
        self.connection.commit()

    def calculate_adress_id(self): 
        """This method calculates the adress_id that the user can add contacts comfortable."""
        cur = self.connection.cursor()
        id = """
            SELECT 
                Max(ID)
            from Adress
        """
        cur.execute(id)
        ID = cur.fetchall()
        tup = ID[0]
        self.New_ID = int(tup[0]) + int(1)
        self.connection.commit()

    def get_name_id(self, first_name, last_name):
        cur = self.connection.cursor()
        query = """
            SELECT 
	            c.ID 
            from Contact c
            join PhoneNumber a
                on c.ID=a.ID
            join Adress b
                on b.ID = c.ID
            where First_Name like "%s" and LastName like "%s"
        """ %(first_name, last_name)
        cur.execute(query)
        ID = cur.fetchall()
        tup = ID[0]
        self.name_id  = int(tup[0])
        self.connection.commit()
        return self.name_id
    
