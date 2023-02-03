# Address-Datenbank ✆

### Ziel

Ein Benutzer kann 

    - Kontaktdaten speichern (Vorname, Nachname, Ort, PLZ, Straße, Hausnummer, Telefonnummer)

    - gespeicherte Kontakte auflisten (alle/od. definierte anhand Vor-/und Nachname)

    - Kontaktinformationen aktualisieren (durch Eingabe von Vor-/und Nachname kann er neue Informationen hinzufügen)

    - Kontaktinformationen löschen (Der ganze Kontakt wird gelöscht. Vorher wird der Kontakt noch einmal ausgegeben und gefragt ob das der richtige Kontakt ist.)

    - Bild (z.B.: Profilbild) vom lokalen Rechner zu einem Kontakt hinzufügen (durch betätigen eines Buttons kann er ein Bild auswählen, welches dann in einem neuen   Ordner abgespeichert wird, damit es später bei der Abfrage eines Kontakts angezeigt werden kann)

### User-Stories
Die User-Stories befinden sich unter: [doc](https://github.com/denisepostl/AdressContactProject/blob/main/doc/UserStory.md)

### Feature

    - Kontakt gehört zur Familie/Freunde (Eigene Tabelle: Roles notwendig, die zur Contact-Tabelle referenziert)

### Verwendung von Python, SQLite und TKinter

Es wird eine SQLite Datenbank für die Speicherung von Address-Daten verwendet. Mit TKinter soll ein GUI erstellt werden und die Datenbank muss dementsprechend verbunden werden.

### Datenmodell (Stand: 20.01.2023)

![Datenmodell](https://github.com/denisepostl/AdressContactProject/blob/main/datamodel/datamodel.png)

Wegen der möglicherweise führenden Nullen die bei Telefonnummer, PLZ u. Hausnummer auftreten könnten habe ich mich für die Telefonnummer und PLZ für den Datentyp VARCHAR entschieden und für die Hausnummer verwende ich den Datentyp NVARCHAR.

### Datenmodell für das Feature: Kategorie (Stand: 20.01.2023)

![Datenmodell](https://github.com/denisepostl/AdressContactProject/blob/main/img/DatamodellExtension.png)


### Beim Ausführen des Programms soll folgender Screen erscheinen: (Stand: 12.01.2023)

![StartScreen](https://github.com/denisepostl/AdressContactProject/blob/main/img/StartScreen.png)

### Bei der Auswahl des Buttons: Kontakt hinzufügen soll folgender Screen erscheinen: (Stand: 20.01.2023)

![StartScreen](https://github.com/denisepostl/AdressContactProject/blob/main/img/Adress.png)

### Query SqLite

Für die Erstellung der Datenbank kann [create_database.py](https://github.com/denisepostl/AdressContactProject/blob/main/adress/create_database.py) ausgeführt werden.
Anschließend werden die Tabellen in der Datenbank *adress.db* erstellt. <br>
Das SQL-File mit den CREATE Table Statements und die Datenbank befinden sich unter: [database](https://github.com/denisepostl/AdressContactProject/tree/main/database)

### Kommandozeilenprogramm

Beim Ausführen von [main_contact.py](https://github.com/denisepostl/AdressContactProject/tree/main/adress/main_contact.py) kann ein kleines Kommandozeilenprogramm ausprobiert werden, dass den Benutzern erlaubt einen Kontakt hinzuzufügen, abfragen, Kontaktdaten ändern und zu löschen. 

### Tests

| Test-Nr. | Testname | Beschreibung | Input | Erwartetes Ergebnis |
| --- | --- | --- | --- | --- | 
| 00 | test_import_successful | Es soll getestet werden, ob der Import des Moduls adress möglich ist.  | -//- | Der Import soll erfolgreich sein|
| 00 | test_*name of class* class_present | Es soll getestet werden, ob der die jeweilige Klasse im Modul adress vorhanden ist.  | -//- | Die Klasse sollte im Modul adress vorhanden sein. |
| 00 | test_class_methods_present | Es soll getestet werden, ob notwendige Methoden in der Klasse implementiert wurden.  | -//- | Die Methoden sollten in der jeweiligen Klasse implementiert sein. | 
| 01 | test_create_Phonenumber | Es soll getestet werden ob sich die Tabelle PhoneNumber mit der Methode create_PhoneNumber, die in der Create Klasse implementiert wurde erstellen lässt. | -//- | Die Tabelle PhoneNumber sollte erfolgreich erstellt worden sein|
| 01 | test_create_Contact | Es soll getestet werden ob sich die Tabelle Contact mit der Methode create_Contact, die in der Create Klasse implementiert wurde erstellen lässt. | -//- | Die Tabelle Contact sollte erfolgreich erstellt worden sein|
| 01 | test_create_Adress | Es soll getestet werden ob sich die Tabelle Adress mit der Methode create_Create_Adress, die in der Create Klasse implementiert wurde erstellen lässt. | -//- | Die Tabelle Adress sollte erfolgreich erstellt worden sein|
| 01 | test_create_Category | Es soll getestet werden ob sich die Tabelle Category mit der Methode create_Category, die in der Create Klasse implementiert wurde erstellen lässt. | -//- | Die Tabelle Category sollte erfolgreich erstellt worden sein|
| 02 | test_if_tables_exists | Es soll getestet werden ob die Tabelle in der Datenbank erfolgreich erstellt worden sind, sowie alle Attribute vorhanden sind. | -//- | Die Tabellen sowie die einzelnen Attribute der Tabellen sollten in der Datenbank erfolgreich erstellt worden sein |
| 03 | test_insert_name | Es soll getestet werden ob sich Vor- u. Nachname in die Tabelle Contact mit der Methode **insert_Name**, welche in der Klasse Insert implementiert wurde, einfügen lassen. Als Datenbank wird eine :memory: db verwendet | Testdaten: Vor- u. Nachname | Die Testdaten sollten erfolgreich in die Tabelle Contact der :memory: db eingefügt worden sein|
| 03 | test_insert_adress | Es soll getestet werden ob sich PLZ, Haus-Nr., Straße u. Ort in die Tabelle Adress mit der Methode **insert_Adress**, welche in der Klasse Insert implementiert wurde, einfügen lassen. Als Datenbank wird eine :memory: db verwende | Testdaten: PLZ, Haus-Nr, Straße, Ort | Die Testdaten sollten erfolgreich in die Tabelle Contact der :memory: db eingefügt worden sein|
| 03 | test_insert_category | Es soll getestet werden ob sich eine Kategorie in die Tabelle Kategorie mit der Methode **insert_Category**, welche in der Klasse Insert implementiert wurde, einfügen lässt. Als Datenbank wird eine :memory: db verwendet | Testdaten: Kategorie | Die Testdaten sollte erfolgreich in die Tabelle Kategorie der :memory: db eingefügt worden sein|
| 03 | test_insert_phone_number | Es soll getestet werden ob sich eine Tel.-Nr. in die Tabelle PhoneNumber mit der Methode **insert_PhoneNumber**, welche in der Klasse Insert implementiert wurde, einfügen lässt. Als Datenbank wird eine :memory: db verwendet | Testdaten: Tel.-Nr. | Die Testdaten sollte erfolgreich in die Tabelle PhoneNumber der :memory: db eingefügt worden sein|
| 04 | test_update_FName | Es soll getestet werden ob sich der Vorname mit der Methode **update_FName**, welche in der Klasse Updating implementiert wurde, anhand der ID aktualisieren lässt. Als Datenbank wird eine :memory: db verwendet | Testdaten: Vorname (neuer Name), ID des zu aktualisierenden Kontakts | Der Vorname sollte erfolgreich in der Tabelle Contact der :memory: db mit der entsprechenden ID aktualisiert worden sein|
| 04 | test_update_LName | Es soll getestet werden ob sich der Vorname mit der Methode **update_LName**, welche in der Klasse Updating implementiert wurde, anhand der ID aktualisieren lässt. Als Datenbank wird eine :memory: db verwendet | Testdaten: Nachname (neuer Name), ID des zu aktualisierenden Kontakts | Der Vorname sollte erfolgreich in der Tabelle Contact der :memory: db mit der entsprechenden ID aktualisiert worden sein|
| 04 | test_update_City | Es soll getestet werden ob sich der Ort mit der Methode **update_City**, welche in der Klasse Updating implementiert wurde, anhand der Contact_ID aktualisieren lässt. Als Datenbank wird eine :memory: db verwendet | Testdaten: Ort (neuer Ort), Contact_ID des zu aktualisierenden Orts | Der Ort sollte erfolgreich in der Tabelle Kategorie der :memory: db anhand der entsprechenden Contact_ID aktualisiert worden sein|
| 04 | test_update_HNR | Es soll getestet werden ob sich die Hausnummer mit der Methode **update_HNR**, welche in der Klasse Updating implementiert wurde, anhand der Contact_ID aktualisieren lässt. Als Datenbank wird eine :memory: db verwendet | Testdaten: Haus-Nr. (neue Haus-Nr.), ID des zu aktualisierenden Kontakts | Die Hausnummer sollte erfolgreich in der Tabelle Adress der :memory: db anhand der entsprechenden Contact_ID aktualisiert worden sein|
| 04 | test_update_tel | Es soll getestet werden ob sich die Telefonnummer mit der Methode **update_Tel**, welche in der Klasse Updating implementiert wurde, anhand der Contact_ID aktualisieren lässt. Als Datenbank wird eine :memory: db verwendet | Testdaten: Tel.-Nr. (neue Tel.-Nr.), ID des zu aktualisierenden Kontakts | Die Telefonnummer sollte erfolgreich in der Tabelle PhoneNumber der :memory: db anhand der entsprechenden Contact_ID aktualisiert worden sein|
| 04 | test_update_Street | Es soll getestet werden ob sich die Straße mit der Methode **update_Street**, welche in der Klasse Updating implementiert wurde, anhand der Contact_ID aktualisieren lässt. Als Datenbank wird eine :memory: db verwendet | Testdaten: Staße (neue Straße), ID des zu aktualisierenden Kontakts | Die Straße sollte erfolgreich in der Tabelle Adress der :memory: db anhand der entsprechenden Contact_ID aktualisiert worden sein|
| 04 | test_update_PostCode | Es soll getestet werden ob sich die PLZ mit der Methode **update_PostCode**, welche in der Klasse Updating implementiert wurde, anhand der Contact_ID aktualisieren lässt. Als Datenbank wird eine :memory: db verwendet | Testdaten: PLZ (neue PLZ), ID des zu aktualisierenden Kontakts | Die Postleitzahl sollte erfolgreich in der Tabelle Kategorie der :memory: db anhand der entsprechenden Contact_ID aktualisiert worden sein|
| 04 | test_update_Category | Es soll getestet werden ob sich die Kategorie mit der Methode **update_Category**, welche in der Klasse Updating implementiert wurde, anhand der Contact_ID aktualisieren lässt. Als Datenbank wird eine :memory: db verwendet | Testdaten: Kategorie (neue Kategorie), ID des zu aktualisierenden Kontakts | Die Kategorie sollte erfolgreich in der Tabelle Kategorie der :memory: db anhand der entsprechenden Contact_ID aktualisiert worden sein|
| 05 | test_delete_adress | Es soll getestet werden ob sich die Adresse (PLZ, Haus-Nr., Straße, Ort) mit der Methode **delete_adress**, welche in der Klasse Delete_Contact implementiert wurde, anhand der Contact_ID löschen lässt. Als Test-Datenbank wird eine :memory: db verwendet | Es wurden Testdaten in die entsprechenden Tabellen eingefügt: PLZ, Haus-Nr., Straße, Ort; Vor-u. Nachname; Contact_ID | Die Adresse sollte erfolgreich in der Tabelle Kategorie der :memory: db anhand der entsprechenden Contact_ID aktualisiert worden sein|
| 05 | test_delete_phonenumber | Es soll getestet werden ob sich die Adresse (PLZ, Haus-Nr., Straße, Ort) mit der Methode **delete_adress**, welche in der Klasse Delete_Contact implementiert wurde, anhand der Contact_ID löschen lässt. Als Test-Datenbank wird eine :memory: db verwendet | Es wurden Testdaten in die entsprechenden Tabellen eingefügt: PLZ, Haus-Nr., Straße, Ort; Vor-u. Nachname; Contact_ID | Die Adresse sollte erfolgreich in der Tabelle Kategorie der :memory: db anhand der entsprechenden Contact_ID aktualisiert worden sein|
| 05 | test_delete_category | Es soll getestet werden ob sich die Adresse (PLZ, Haus-Nr., Straße, Ort) mit der Methode **delete_adress**, welche in der Klasse Delete_Contact implementiert wurde, anhand der Contact_ID löschen lässt. Als Test-Datenbank wird eine :memory: db verwendet | Es wurden Testdaten in die entsprechenden Tabellen eingefügt: PLZ, Haus-Nr., Straße, Ort; Vor-u. Nachname; Contact_ID | Die Adresse sollte erfolgreich in der Tabelle Kategorie der :memory: db anhand der entsprechenden Contact_ID aktualisiert worden sein|
| 05 | test_delete_contact_with_data | Es soll getestet werden ob sich die Adresse (PLZ, Haus-Nr., Straße, Ort) mit der Methode **delete_adress**, welche in der Klasse Delete_Contact implementiert wurde, anhand der Contact_ID löschen lässt. Als Test-Datenbank wird eine :memory: db verwendet | Es wurden Testdaten in die entsprechenden Tabellen eingefügt: PLZ, Haus-Nr., Straße, Ort; Vor-u. Nachname; Contact_ID | Die Adresse sollte erfolgreich in der Tabelle Kategorie der :memory: db anhand der entsprechenden Contact_ID aktualisiert worden sein|
| 06 | test_query_search_by_invalid_input | Es soll getestet werden ob sich die Adresse (PLZ, Haus-Nr., Straße, Ort) mit der Methode **delete_adress**, welche in der Klasse Delete_Contact implementiert wurde, anhand der Contact_ID löschen lässt. Als Test-Datenbank wird eine :memory: db verwendet | Es wurden Testdaten in die entsprechenden Tabellen eingefügt: PLZ, Haus-Nr., Straße, Ort; Vor-u. Nachname; Contact_ID | Die Adresse sollte erfolgreich in der Tabelle Kategorie der :memory: db anhand der entsprechenden Contact_ID aktualisiert worden sein|
| 06 | test_query_search_by_empty_input | Es soll getestet werden ob sich die Adresse (PLZ, Haus-Nr., Straße, Ort) mit der Methode **delete_adress**, welche in der Klasse Delete_Contact implementiert wurde, anhand der Contact_ID löschen lässt. Als Test-Datenbank wird eine :memory: db verwendet | Es wurden Testdaten in die entsprechenden Tabellen eingefügt: PLZ, Haus-Nr., Straße, Ort; Vor-u. Nachname; Contact_ID | Die Adresse sollte erfolgreich in der Tabelle Kategorie der :memory: db anhand der entsprechenden Contact_ID aktualisiert worden sein|
| 06 | test_query_search_by_null_input | Es soll getestet werden ob sich die Adresse (PLZ, Haus-Nr., Straße, Ort) mit der Methode **delete_adress**, welche in der Klasse Delete_Contact implementiert wurde, anhand der Contact_ID löschen lässt. Als Test-Datenbank wird eine :memory: db verwendet | Es wurden Testdaten in die entsprechenden Tabellen eingefügt: PLZ, Haus-Nr., Straße, Ort; Vor-u. Nachname; Contact_ID | Die Adresse sollte erfolgreich in der Tabelle Kategorie der :memory: db anhand der entsprechenden Contact_ID aktualisiert worden sein|
| 06 | test_query_search_by_valid_input | Es soll getestet werden ob sich die Adresse (PLZ, Haus-Nr., Straße, Ort) mit der Methode **delete_adress**, welche in der Klasse Delete_Contact implementiert wurde, anhand der Contact_ID löschen lässt. Als Test-Datenbank wird eine :memory: db verwendet | Es wurden Testdaten in die entsprechenden Tabellen eingefügt: PLZ, Haus-Nr., Straße, Ort; Vor-u. Nachname; Contact_ID | Die Adresse sollte erfolgreich in der Tabelle Kategorie der :memory: db anhand der entsprechenden Contact_ID aktualisiert worden sein|
| 07 | test_get_name_id | Es soll getestet werden ob sich die Adresse (PLZ, Haus-Nr., Straße, Ort) mit der Methode **delete_adress**, welche in der Klasse Delete_Contact implementiert wurde, anhand der Contact_ID löschen lässt. Als Test-Datenbank wird eine :memory: db verwendet | Es wurden Testdaten in die entsprechenden Tabellen eingefügt: PLZ, Haus-Nr., Straße, Ort; Vor-u. Nachname; Contact_ID | Die Adresse sollte erfolgreich in der Tabelle Kategorie der :memory: db anhand der entsprechenden Contact_ID aktualisiert worden sein|
| 08 | test_askin_query | Es soll getestet werden ob sich die Adresse (PLZ, Haus-Nr., Straße, Ort) mit der Methode **delete_adress**, welche in der Klasse Delete_Contact implementiert wurde, anhand der Contact_ID löschen lässt. Als Test-Datenbank wird eine :memory: db verwendet | Es wurden Testdaten in die entsprechenden Tabellen eingefügt: PLZ, Haus-Nr., Straße, Ort; Vor-u. Nachname; Contact_ID | Die Adresse sollte erfolgreich in der Tabelle Kategorie der :memory: db anhand der entsprechenden Contact_ID aktualisiert worden sein|
| 08 | test_askin_phone_query | Es soll getestet werden ob sich die Adresse (PLZ, Haus-Nr., Straße, Ort) mit der Methode **delete_adress**, welche in der Klasse Delete_Contact implementiert wurde, anhand der Contact_ID löschen lässt. Als Test-Datenbank wird eine :memory: db verwendet | Es wurden Testdaten in die entsprechenden Tabellen eingefügt: PLZ, Haus-Nr., Straße, Ort; Vor-u. Nachname; Contact_ID | Die Adresse sollte erfolgreich in der Tabelle Kategorie der :memory: db anhand der entsprechenden Contact_ID aktualisiert worden sein|
| 08 | test_askin_all | Es soll getestet werden ob sich die Adresse (PLZ, Haus-Nr., Straße, Ort) mit der Methode **delete_adress**, welche in der Klasse Delete_Contact implementiert wurde, anhand der Contact_ID löschen lässt. Als Test-Datenbank wird eine :memory: db verwendet | Es wurden Testdaten in die entsprechenden Tabellen eingefügt: PLZ, Haus-Nr., Straße, Ort; Vor-u. Nachname; Contact_ID | Die Adresse sollte erfolgreich in der Tabelle Kategorie der :memory: db anhand der entsprechenden Contact_ID aktualisiert worden sein|
| 08 | test_askin_by_id | Es soll getestet werden ob sich die Adresse (PLZ, Haus-Nr., Straße, Ort) mit der Methode **delete_adress**, welche in der Klasse Delete_Contact implementiert wurde, anhand der Contact_ID löschen lässt. Als Test-Datenbank wird eine :memory: db verwendet | Es wurden Testdaten in die entsprechenden Tabellen eingefügt: PLZ, Haus-Nr., Straße, Ort; Vor-u. Nachname; Contact_ID | Die Adresse sollte erfolgreich in der Tabelle Kategorie der :memory: db anhand der entsprechenden Contact_ID aktualisiert worden sein|







