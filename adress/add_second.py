import sqlite3

class AddSecondRecord():

    def __init__(self):
        self.connection = sqlite3.connect("database/adress.db")


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
    
    def add_adress_(self, post_code, street, city, house_number):
       cur = self.connection.cursor()
       cur.execute("INSERT INTO Adress ('PostCode', 'Street', 'City', 'Housenumber', 'Contact_ID') values(?,?,?,?,?)", (post_code, street, city, house_number, self.name_id))
       self.connection.commit()

    def add_phone(self, phone_number):
        cur = self.connection.cursor()
        cur.execute("INSERT INTO PhoneNumber ('PhoneNumber', 'Contact_ID') values(?,?)", (phone_number, self.name_id))
        self.connection.commit()



