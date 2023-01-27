import pytest
import logging

try:
    import adress
except ModuleNotFoundError as e:
    logging.error("Module not found %s", e)


def test_001_import(capsys):
    assert adress

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""


