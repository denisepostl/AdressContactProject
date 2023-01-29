import sqlite3
import logging
import pytest

try:
    import adress
except ModuleNotFoundError as e:
    logging.error("Module not found %s", e)



def test_get_del_id():
    # Add a test contact to the database
    del_obj = adress.Delete()
    connection = sqlite3.connect("database/adress.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO Contact (First_Name, LastName) VALUES ('John', 'Doe')")
    connection.commit()

    # Test that the correct ID is returned
    id = del_obj.get_del_id("John", "Doe")
    cur.execute("SELECT ID FROM Contact WHERE First_Name = 'John' AND LastName = 'Doe'")
    assert cur.fetchone()[0] == id

def test_delete_adress():
    # Add a test contact and address to the database
    del_obj = adress.Delete()
    connection = sqlite3.connect("database/adress.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO Contact (First_Name, LastName) VALUES ('John', 'Doe')")
    cur.execute("SELECT ID FROM Contact WHERE First_Name = 'John' AND LastName = 'Doe'")
    contact_id = cur.fetchone()[0]
    cur.execute("INSERT INTO Adress (Contact_ID, City, Street) VALUES (?, 'New York', 'Main St')", (contact_id,))
    connection.commit()

    # Delete the test address
    del_obj.get_del_id("John", "Doe")
    del_obj.delete_adress()

    # Test that the address was deleted
    cur.execute("SELECT * FROM Adress WHERE Contact_ID = ?", (contact_id,))
    assert cur.fetchone() == None

def test_delete_phonenumber():
    # Add a test contact and PhoneNumber to the database
    del_obj = adress.Delete()
    connection = sqlite3.connect("database/adress.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO Contact (First_Name, LastName) VALUES ('John', 'Doe')")
    cur.execute("SELECT ID FROM Contact WHERE First_Name = 'John' AND LastName = 'Doe'")
    contact_id = cur.fetchone()[0]
    cur.execute("INSERT INTO PhoneNumber (PhoneNumber, Contact_ID) VALUES ('066412121',?)", (contact_id,))
    connection.commit()

    # Delete the test Phone
    del_obj.get_del_id("John", "Doe")
    del_obj.delete_phonenumber()

    # Test that the address was deleted
    cur.execute("SELECT * FROM PhoneNumber WHERE Contact_ID = ?", (contact_id,))
    assert cur.fetchone() == None

