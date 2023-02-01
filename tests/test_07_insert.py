import sqlite3
import logging
import pytest

try:
    import adress
except ModuleNotFoundError as e:
    logging.error("Module not found %s", e)


@pytest.fixture
def in_memory_db():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    cursor.execute("CREATE TABLE Contact ('ID' INTEGER PRIMARY KEY AUTOINCREMENT, 'First_Name' TEXT, 'LastName' TEXT)")
    cursor.execute("CREATE TABLE Adress ('ID' INTEGER PRIMARY KEY AUTOINCREMENT, 'PostCode' TEXT, 'Street' TEXT, 'City' TEXT, 'Housenumber' TEXT, 'Contact_ID' INTEGER)")
    cursor.execute("CREATE TABLE Kategorie ('ID' INTEGER PRIMARY KEY AUTOINCREMENT, 'Kategorie' TEXT, 'Contact_ID' INTEGER)")
    cursor.execute("CREATE TABLE PhoneNumber ('ID' INTEGER PRIMARY KEY AUTOINCREMENT, 'PhoneNumber' TEXT, 'Contact_ID' INTEGER)")
    
    yield conn
    
    conn.close()

def test_insert_name(in_memory_db):
    insert = adress.Insert()
    insert.connection=in_memory_db
    insert.insert_Name("John", "Doe")
    cursor = in_memory_db.cursor()
    cursor.execute("SELECT First_Name, LastName FROM Contact")
    result = cursor.fetchone()
    assert result[0] == 'John'
    assert result[1] == 'Doe'


 

def test_insert_address(in_memory_db):
    insert = adress.Insert()
    insert.connection=in_memory_db
    insert.insert_Name("John", "Doe")
    insert.insert_Address("12345", "Main St", "San Francisco", "42")
    cursor = in_memory_db.cursor()
    cursor.execute("SELECT a.PostCode, a.Street, a.City, a.HouseNumber from adress a join contact c on a. ID = c.ID")
    result = cursor.fetchone()
    assert result[0] == '12345'
    assert result[1] == 'Main St'
    assert result[2] == 'San Francisco'
    assert result[3] == '42'

    

def test_insert_category(in_memory_db):
    insert = adress.Insert()
    insert.connection=in_memory_db
    insert.insert_Name("John", "Doe")
    insert.Insert_Category("Freund")
    cursor = in_memory_db.cursor()
    cursor.execute("SELECT a.Kategorie from Kategorie a join contact c on a. ID = c.ID")
    result = cursor.fetchone()
    assert result[0] == 'Freund' 

def test_insert_phone_number(in_memory_db):
    insert = adress.Insert()
    insert.connection=in_memory_db
    insert.insert_Name("John", "Doe")
    insert.insert_PhoneNumber("0644202010")
    cursor = in_memory_db.cursor()
    cursor.execute("SELECT a.PhoneNumber from PhoneNumber a join contact c on a. ID = c.ID")
    result = cursor.fetchone()
    assert result[0] == '0644202010'