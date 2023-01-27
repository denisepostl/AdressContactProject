import pytest
import sqlite3
import logging

try:
    import adress
except ModuleNotFoundError as e:
    logging.error("Module not found %s", e)


def test_get_del_id(delete_obj):
    delete_obj = adress.Delete()
    assert delete_obj.get_del_id("John", "Doe") == 1

def test_delete_contact(delete_obj):
    delete_obj = adress.Delete()
    delete_obj.delete_contact("John", "Doe")
    cur = delete_obj.connection.cursor()
    cur.execute("SELECT * FROM Contact WHERE First_Name='John' and LastName='Doe'")
    result = cur.fetchall()
    assert len(result) == 0

def test_delete_adress(delete_obj):
    delete_obj = adress.Delete()
    delete_obj.get_del_id("John", "Doe")
    delete_obj.delete_adress()
    cur = delete_obj.connection.cursor()
    cur.execute("SELECT * FROM Adress WHERE Contact_ID=1")
    result = cur.fetchall()
    assert len(result) == 0

def test_delete_phonenumber(delete_obj):
    delete_obj = adress.Delete()
    delete_obj.get_del_id("John", "Doe")
    delete_obj.delete_phonenumber()
    cur = delete_obj.connection.cursor()
    cur.execute("SELECT * FROM PhoneNumber WHERE Contact_ID=1")
    result = cur.fetchall()
    assert len(result) == 0
