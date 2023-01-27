import os

try:
    import adress
except Exception as e:
    print(type(e))
    adress = None


def test_import_successful():
    """Test if import is possible."""
    assert type(adress) == type(os)
