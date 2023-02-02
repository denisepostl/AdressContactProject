import sqlite3
import pytest
import logging


try:
    import adress
except ModuleNotFoundError as e:
    logging.error("Module not found %s", e)


@pytest.fixture
def setup_database():
    """Create in-memory database for testing."""
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    # create tables
    cursor.execute("CREATE TABLE Contact (First_Name TEXT, LastName TEXT)")
    cursor.execute("CREATE TABLE Adress (PostCode TEXT, City TEXT, Street TEXT, HouseNumber TEXT)")
    cursor.execute("CREATE TABLE PhoneNumber (PhoneNumber TEXT)")
    cursor.execute("CREATE TABLE Kategorie (Kategorie TEXT)")

    # insert test data
    cursor.execute("INSERT INTO Contact VALUES ('John', 'Doe')")
    cursor.execute("INSERT INTO Adress VALUES ('12345', 'Test City', 'Test Street', '1')")
    cursor.execute("INSERT INTO PhoneNumber VALUES ('1234567890')")
    cursor.execute("INSERT INTO Kategorie VALUES ('Freunde')")
    connection.commit()
    yield connection
    connection.close()


def test_update_FName(setup_database):
    """Test if user can update the First Name"""
    updater = adress.Updating()
    updater.connection = setup_database
    updater.update_FName('Jane', 'John')
    cursor = setup_database.cursor()
    cursor.execute("SELECT First_Name FROM Contact")
    result = cursor.fetchone()
    assert result[0] == 'Jane'


def test_update_LName(setup_database):
    """Test if user can update the Last Name"""
    updater = adress.Updating()
    updater.connection = setup_database
    updater.update_LName('Test', 'Doe')
    cursor = setup_database.cursor()
    cursor.execute("SELECT LastName FROM Contact")
    result = cursor.fetchone()
    assert result[0] == 'Test'


def test_update_City(setup_database):
    """Test if user can update the City"""
    updater = adress.Updating()
    updater.connection = setup_database
    updater.update_City('Test', 'Test City')
    cursor = setup_database.cursor()
    cursor.execute("SELECT City FROM Adress")
    result = cursor.fetchone()
    assert result[0] == 'Test'


def test_update_HNR(setup_database):
    """Test if user can update the housenumber"""
    updater = adress.Updating()
    updater.connection = setup_database
    updater.update_HNR('2', '1')
    cursor = setup_database.cursor()
    cursor.execute("SELECT HouseNumber FROM Adress")
    result = cursor.fetchone()
    assert result[0] == '2'


def test_update_Street(setup_database):
    """Test if user can update the street"""
    updater = adress.Updating()
    updater.connection = setup_database
    updater.update_Street('Test', 'Test Street')
    cursor = setup_database.cursor()
    cursor.execute("SELECT Street FROM Adress")
    result = cursor.fetchone()
    assert result[0] == 'Test'


def test_update_PostCode(setup_database):
    """Test if user can update the PostCode"""
    updater = adress.Updating()
    updater.connection = setup_database
    updater.update_PostCode('54321', '12345')

    cursor = setup_database.cursor()
    cursor.execute("SELECT PostCode FROM Adress")
    result = cursor.fetchone()

    assert result[0] == '54321'


def test_update_Category(setup_database):
    """Test if user can update the Category"""
    updater = adress.Updating()
    updater.connection = setup_database
    updater.update_Category('Familie', 'Freunde')

    cursor = setup_database.cursor()
    cursor.execute("SELECT Kategorie FROM Kategorie")
    result = cursor.fetchone()

    assert result[0] == 'Familie'
