import sqlite3

class Updating():

    def __init__(self):
        self.connection = sqlite3.connect("database/adress_cat.db")


    def update_FName(self, new_name, old_name):
        cur = self.connection.cursor()
        cur.execute("UPDATE Contact SET First_Name = ? WHERE First_Name = ?" , (new_name, old_name))
        self.connection.commit()

    def update_LName(self, newLName, oldLName):
        cur = self.connection.cursor()
        cur.execute("UPDATE Contact SET LastName = ? WHERE LastName = ?" , (newLName, oldLName))
        self.connection.commit()

    def update_PostCode(self, NewPLZ, OldPLZ):
        cur = self.connection.cursor()
        cur.execute("UPDATE Adress SET PostCode = ? WHERE PostCode = ?" , (NewPLZ, OldPLZ))
        self.connection.commit()
    
    def update_City(self, NewCity, OldCity):
        cur = self.connection.cursor()
        cur.execute("UPDATE Adress SET City = ? WHERE City = ?" , (NewCity, OldCity))
        self.connection.commit()

    def update_Street(self, NewStreet, OldStreet):
        cur = self.connection.cursor()
        cur.execute("UPDATE Adress SET Street = ? WHERE Street = ?" , (NewStreet, OldStreet))
        self.connection.commit()

    def update_HNR(self, newhnr, oldhnr):
        cur = self.connection.cursor()
        cur.execute("UPDATE Adress SET HouseNumber = ? WHERE HouseNumber = ?" , (newhnr, oldhnr))
        self.connection.commit()

    def update_Tel(self, newtel, oldtel):
        cur = self.connection.cursor()
        cur.execute("UPDATE PhoneNumber SET PhoneNumber = ? WHERE PhoneNumber = ?" , (newtel, oldtel))
        self.connection.commit()

    def update_Category(self, Cat, OldCat):
        cur = self.connection.cursor()
        cur.execute("UPDATE Kategorie SET Kategorie = ? WHERE Kategorie = ?" , (Cat, OldCat))
        self.connection.commit()
