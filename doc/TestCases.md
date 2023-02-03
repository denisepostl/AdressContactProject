| Test-Nr. | Testname | Beschreibung | Input | Erwartetes Ergebnis |
| --- | --- | --- | --- | --- | 
| 00 | test_import_successful | Es soll getestet werden, ob der Import des Moduls adress möglich ist.  | -//- | Der Import soll erfolgreich sein|
| 00 | test_*name of class* class_present | Es soll getestet werden, ob die jeweilige Klasse im Modul adress vorhanden ist.  | -//- | Die Klasse sollte im Modul adress vorhanden sein. |
| 00 | test_class_methods_present | Es soll getestet werden, ob notwendige Methoden in der jeweiligen Klasse implementiert wurden.  | -//- | Die Methoden sollten in der jeweiligen Klasse implementiert sein. | 
| 01 | test_create_Phonenumber | Es soll getestet werden ob sich die Tabelle PhoneNumber mit der Methode **create_PhoneNumber**, die in der Create Klasse implementiert wurde in der Datenbank erstellen lässt. | -//- | Die Tabelle PhoneNumber sollte erfolgreich erstellt worden sein|
| 01 | test_create_Contact | Es soll getestet werden ob sich die Tabelle Contact mit der Methode **create_Contact**, die in der Create Klasse implementiert wurde erstellen lässt. | -//- | Die Tabelle Contact sollte erfolgreich erstellt worden sein |
| 01 | test_create_Adress | Es soll getestet werden ob sich die Tabelle Adress mit der Methode **create_Adress**, die in der Create Klasse implementiert wurde erstellen lässt. | -//- | Die Tabelle Adress sollte erfolgreich erstellt worden sein |
| 01 | test_create_Category | Es soll getestet werden ob sich die Tabelle Category mit der Methode **create_Category**, die in der Create Klasse implementiert wurde erstellen lässt. | -//- | Die Tabelle Category sollte erfolgreich erstellt worden sein |
| 02 | test_if_tables_exists | Es soll getestet werden ob die Tabellen in der Datenbank erfolgreich erstellt worden sind, sowie alle Attribute vorhanden sind. | -//- | Die Tabellen sowie die einzelnen Attribute der Tabellen sollten in der Datenbank (die in der Connection definiert ist) erfolgreich erstellt worden sein |
