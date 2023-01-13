import sqlite3
from calculate_id import CalculateID

class Add(CalculateID):

    def __init__(self):
        self.connection = sqlite3.connect("contacts.db")

    def add_Name(self, ID, first_name, last_name):
        """This method is used for inserting a first- and last name in contact table."""
        cur = self.connection.cursor()
        query = """
            INSERT INTO Contact(ID, First_Name, LastName)
            VALUES(%d, "%s", "%s"); """ %(ID, first_name, last_name)
        
        cur.execute(query)
        self.connection.commit()


    def add_Address(self, street, post_code, city, house_number, Contact_ID):
        """This method is used for inserting a adress in adress table."""
        cur = self.connection.cursor()
        self.calculate_adress_id()

        query = """
            INSERT INTO Adress(ID, Street, PostCode, City, Housenumber, Contact_ID)
            VALUES(%d, "%s", %d, "%s", %d, %d); """ %(self.New_ID, street, post_code, city, house_number, Contact_ID)
        
        cur.execute(query)
        self.connection.commit()


    def add_PhoneNumber(self, phone_number, Contact_ID):
        """This method is used for add a phonenumber in phonennumber table."""
        cur = self.connection.cursor()
        self.calculate_phone_id()
        query = """
            INSERT INTO PhoneNumber(ID, PhoneNumber, Contact_ID)
            VALUES(%d, "%s", %d); """ %(self.New_ID, phone_number, Contact_ID)
        
        cur.execute(query)
        self.connection.commit()