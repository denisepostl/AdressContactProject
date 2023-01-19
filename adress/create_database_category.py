import sqlite3

class Create():

    def __init__(self):
        self.connection = sqlite3.connect("database/adress_category.db")


    def create_Contact(self):
        """This method is used to create Table Contact"""
        cur = self.connection.cursor()
        query = """
            CREATE TABLE Contact(
            ID INT PRIMARY KEY,
            First_Name VARCHAR,
            LastName VARCHAR,
            Kategorie_ID INTEGER,
            FOREIGN KEY(Kategorie_ID) REFERENCES Kategorie(ID));
        """ 
        cur.execute(query)
        self.connection.commit()

    def create_Phonenumber(self):
        """This method is used to create Table Phonennumber"""
        cur = self.connection.cursor()
        query = """
            CREATE TABLE PhoneNumber(
            ID INT PRIMARY KEY,
            PhoneNumber VARCHAR,
            Contact_ID INT,
            FOREIGN KEY(Contact_ID) REFERENCES Contact(ID));
        """ 
        cur.execute(query)
        self.connection.commit()

    def create_Adress(self):
        """This method is used to create Table Adress"""
        cur = self.connection.cursor()
        query = """
            CREATE TABLE Adress(
            ID INT PRIMARY KEY,
            Street VARCHAR,
            PostCode INT,
            City VARCHAR,
            HouseNumber INT,
            Contact_ID INT,
            FOREIGN KEY(Contact_ID) REFERENCES Contact(ID));
        """ 
        cur.execute(query)
        self.connection.commit()

    def create_Category(self):
        """This method is used to create Table Category"""
        cur = self.connection.cursor()
        query = """
            CREATE TABLE Kategorie(
            ID INT PRIMARY KEY,
            Kategorie VARCHAR);
        """ 
        cur.execute(query)
        self.connection.commit()

def main():
    db = Create()
    db.create_Phonenumber()
    db.create_Contact()
    db.create_Adress()
    db.create_Category()

if __name__ == "__main__":
    main()