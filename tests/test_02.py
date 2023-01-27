import sqlite3
import logging

try:
    import adress
except ModuleNotFoundError as e:
    logging.error("Module not found %s", e)


def test_001_add_Name():
    add_obj = adress.Add()
    ID = 1
    first_name = "John"
    last_name = "Doe"
    add_obj.add_Name(ID, first_name, last_name)
    conn = sqlite3.connect("database/adress.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Contact WHERE ID = 1")
    result = c.fetchall()
    assert len(result) == 1
    assert result[0][1] == first_name
    assert result[0][2] == last_name
    conn.close()

def test_002_add_Address():
    add_obj = adress.Add()
    street = "Main St"
    post_code = "12345"
    city = "New York"
    house_number = "5"
    Contact_ID = 1
    add_obj.add_Address(street, post_code, city, house_number, Contact_ID)
    conn = sqlite3.connect("database/adress.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Adress WHERE Contact_ID = 1")
    result = c.fetchall()
    assert len(result) == 1
    assert result[0][1] == street
    assert result[0][2] == post_code
    assert result[0][3] == city
    assert result[0][4] == house_number
    assert result[0][5] == Contact_ID
    conn.close()
    
def test_003_add_PhoneNumber():
    add_obj = adress.Add()
    phone_number = "06401212"
    Contact_ID = 1
    add_obj.add_PhoneNumber(phone_number, Contact_ID)
    conn = sqlite3.connect("database/adress.db")
    c = conn.cursor()
    c.execute("SELECT * FROM PhoneNumber WHERE Contact_ID = 1")
    result = c.fetchall()
    assert len(result) == 1
    assert result[0][1] == phone_number
    assert result[0][2] == Contact_ID
    conn.close()
