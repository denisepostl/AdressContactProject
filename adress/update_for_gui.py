import sqlite3

class Updating():

    def __init__(self):
        self.connection = sqlite3.connect("database/adress_cat.db")


    def get_id(self, first_name, last_name):
        """This method is used to return the id from record when the user wants to update a record."""
        cur = self.connection.cursor()
        get_id = """
            SELECT
	            a.ID
            from Contact a
            where a.First_Name like "%s"
            and a.LastName like "%s";
        """ %(first_name, last_name)

        cur.execute(get_id)
        
        ID = cur.fetchall()
        tup = ID[0]
        self.My_ID = int(tup[0])
        self.connection.commit()

        return self.My_ID
        

    def update_FName(self, new_name, id):
        cur = self.connection.cursor()
        cur.execute("UPDATE Contact SET First_Name = ? WHERE ID = ?" , (new_name, id))
        self.connection.commit()

    def update_LName(self, newLName, id):
        cur = self.connection.cursor()
        cur.execute("UPDATE Contact SET LastName = ? WHERE ID = ?" , (newLName, id))
        self.connection.commit()

    def update_PostCode(self, NewPLZ, contact_id):
        cur = self.connection.cursor()
        cur.execute("UPDATE Adress SET PostCode = ? WHERE Contact_ID = ?" , (NewPLZ, contact_id))
        self.connection.commit()
    
    def update_City(self, NewCity, contact_id):
        cur = self.connection.cursor()
        cur.execute("UPDATE Adress SET City = ? WHERE Contact_ID = ?" , (NewCity, contact_id))
        self.connection.commit()

    def update_Street(self, NewStreet, contact_id):
        cur = self.connection.cursor()
        cur.execute("UPDATE Adress SET Street = ? WHERE Contact_ID = ?" , (NewStreet, contact_id))
        self.connection.commit()

    def update_HNR(self, newhnr, contact_id):
        cur = self.connection.cursor()
        cur.execute("UPDATE Adress SET HouseNumber = ? WHERE Contact_ID = ?"  , (newhnr, contact_id))
        self.connection.commit()

    def update_Tel(self, newtel, contact_id):
        cur = self.connection.cursor()
        cur.execute("UPDATE PhoneNumber SET PhoneNumber = ? WHERE Contact_ID = ?"  , (newtel, contact_id))
        self.connection.commit()

    def update_Category(self, Cat, contact_id):
        cur = self.connection.cursor()
        cur.execute("UPDATE Kategorie SET Kategorie = ? WHERE Contact_ID = ?" , (Cat, contact_id))
        self.connection.commit()
