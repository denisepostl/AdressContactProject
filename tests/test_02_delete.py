import pytest
import sqlite3
import logging

try:
    import adress
except ModuleNotFoundError as e:
    logging.error("Module not found %s", e)

def test_delete_contact():
    delete = adress.Delete()
    delete.delete_contact("Max", "Mustermann")
    cur = delete.connection.cursor()
    cur.execute("SELECT * FROM Contact WHERE First_Name='Max' AND LastName='Mustermann'")
    result = cur.fetchone()
    assert result is None
