import sqlite3
import pytest
import logging


try:
    import adress
except ModuleNotFoundError as e:
    logging.error("Module not found %s", e)


@pytest.fixture
def setup_database():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    # create tables
    cursor.execute("CREATE TABLE Contact (First_Name TEXT, Last_Name TEXT)")
    cursor.execute("CREATE TABLE Adress (PostCode INTEGER, City TEXT, Street TEXT, HouseNumber INTEGER)")
    cursor.execute("CREATE TABLE PhoneNumber (PhoneNumber INTEGER)")

    # insert test data
    cursor.execute("INSERT INTO Contact VALUES ('John', 'Doe')")
    cursor.execute("INSERT INTO Adress VALUES (12345, 'Test City', 'Test Street', 1)")
    cursor.execute("INSERT INTO PhoneNumber VALUES (1234567890)")
    connection.commit()
    yield connection
    connection.close()


def test_update_FName(setup_database):
    updater = adress.Updating()
    updater.connection = setup_database
    updater.update_FName('Jane', 'John')
    cursor = setup_database.cursor()
    cursor.execute("SELECT First_Name FROM Contact")
    result = cursor.fetchone()
    assert result[0] == 'Jane'


def test_update_PostCode(setup_database):
    updater = adress.Updating()
    updater.connection = setup_database
    updater.update_PostCode(54321, 12345)

    cursor = setup_database.cursor()
    cursor.execute("SELECT PostCode FROM Adress")
    result = cursor.fetchone()

    assert result[0] == 54321

