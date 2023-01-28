import sqlite3
import pytest
import logging


try:
    import adress
except ModuleNotFoundError as e:
    logging.error("Module not found %s", e)


@pytest.fixture(scope='module')
def setup_db():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    # Create the necessary tables
    cursor.execute("""CREATE TABLE Contact (ID INTEGER PRIMARY KEY, First_Name TEXT, LastName TEXT);""")
    cursor.execute("""CREATE TABLE Adress (ID INTEGER PRIMARY KEY, Street TEXT, PostCode TEXT, City TEXT, HouseNumber TEXT, Contact_ID INTEGER);""")
    cursor.execute("""CREATE TABLE PhoneNumber (ID INTEGER PRIMARY KEY, PhoneNumber TEXT, Contact_ID INTEGER);""")
    connection.commit()

    # Insert some test data
    cursor.execute("""INSERT INTO Contact (ID, First_Name, LastName) VALUES (1, 'John', 'Doe');""")
    cursor.execute("""INSERT INTO Contact (ID, First_Name, LastName) VALUES (2, 'Jane', 'Doe');""")
    cursor.execute("""INSERT INTO Adress (ID, Contact_ID, Street, PostCode, City, HouseNumber) VALUES (1, '123 Main St', '12345', 'Anytown', '1', 1);""")
    cursor.execute("""INSERT INTO Adress (ID, Contact_ID, Street, PostCode, City, HouseNumber) VALUES (2, '456 Elm St', '67890', 'Othertown', '2', 2);""")
    cursor.execute("""INSERT INTO PhoneNumber (ID, Contact_ID, PhoneNumber) VALUES (1, '5551231234', 1);""")
    cursor.execute("""INSERT INTO PhoneNumber (ID, Contact_ID, PhoneNumber) VALUES (2, '5555551111', 2);""")
    connection.commit()

    yield connection

    connection.close()

def test_askin_query(setup_db):
    query = adress.Ask()
    query.connection = setup_db

    # Test a query that should return a result
    print(query.askin('John', 'Doe'))
    #assert result == ('John', 'Doe', '123 Main St', '12345', 'Anytown', '1', '5551231234')


