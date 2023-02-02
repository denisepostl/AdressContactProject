import sqlite3


class QuerySearchBy():
    """Class for Searching Records by Name | Phonenumber or askin all"""

    def __init__(self):
        self.connection = sqlite3.connect("database/adress_cat.db")

    def askin_query(self, first_name, last_name):
        """Asking for a contact by first and last name"""
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
                on a.ID = d.Contact_ID
            where First_Name like "%s" and LastName like "%s" """ % (first_name, last_name,)

        cur.execute(query)
        self.contact = cur.fetchall()
        self.connection.commit()

    def askin_phone_query(self, phone):
        """Search for a contact by Phone Number."""
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
                on a.ID = d.Contact_ID
            where PhoneNumber like "%s" """ % (phone,)

        cur.execute(query)
        self.contact = cur.fetchall()
        self.connection.commit()

    def askin_all_query(self):
        """Search for all contacts."""
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
                on a.ID = d.Contact_ID """

        cur.execute(query)
        self.contact = cur.fetchall()
        self.connection.commit()
