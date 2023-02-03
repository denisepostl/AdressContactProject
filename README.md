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
| 00 | test_*name of class* class_present | Es soll getestet werden, ob die jeweilige Klasse im Modul adress vorhanden ist.  | -//- | Die Klasse sollte im Modul adress vorhanden sein. |
| 00 | test_class_methods_present | Es soll getestet werden, ob notwendige Methoden in der jeweiligen Klasse implementiert wurden.  | -//- | Die Methoden sollten in der jeweiligen Klasse implementiert sein. | 
| 01 | test_create_Phonenumber | Es soll getestet werden ob sich die Tabelle PhoneNumber mit der Methode **create_PhoneNumber**, die in der Create Klasse implementiert wurde in der Datenbank erstellen lässt. | -//- | Die Tabelle PhoneNumber sollte erfolgreich erstellt worden sein|
| 01 | test_create_Contact | Es soll getestet werden ob sich die Tabelle Contact mit der Methode **create_Contact**, die in der Create Klasse implementiert wurde erstellen lässt. | -//- | Die Tabelle Contact sollte erfolgreich erstellt worden sein |
| 01 | test_create_Adress | Es soll getestet werden ob sich die Tabelle Adress mit der Methode **create_Adress**, die in der Create Klasse implementiert wurde erstellen lässt. | -//- | Die Tabelle Adress sollte erfolgreich erstellt worden sein |
| 01 | test_create_Category | Es soll getestet werden ob sich die Tabelle Category mit der Methode **create_Category**, die in der Create Klasse implementiert wurde erstellen lässt. | -//- | Die Tabelle Category sollte erfolgreich erstellt worden sein |
| 02 | test_if_tables_exists | Es soll getestet werden ob die Tabellen in der Datenbank erfolgreich erstellt worden sind, sowie alle Attribute vorhanden sind. | -//- | Die Tabellen sowie die einzelnen Attribute der Tabellen sollten in der Datenbank (die in der Connection definiert ist) erfolgreich erstellt worden sein |
| 03 | test_insert_name | Es soll getestet werden ob sich Vor- u. Nachname in die Tabelle Contact mit der Methode **insert_Name**, welche in der Klasse Insert implementiert wurde, einfügen lassen. Als Test-Datenbank wird eine :memory: db verwendet | Testdaten: Vor- u. Nachname | Die Testdaten sollten erfolgreich in die Tabelle Contact der :memory: db eingefügt worden sein |

| 03 | test_insert_adress | Es soll getestet werden ob sich PLZ, Haus-Nr., Straße u. Ort in die Tabelle Adress mit der Methode **insert_Adress**, welche in der Klasse Insert implementiert wurde, einfügen lassen. Als Test-Datenbank wird eine :memory: db verwendet | Testdaten: PLZ, Haus-Nr, Straße, Ort, Contact_ID | Die Testdaten sollten erfolgreich in die Tabelle Adress der :memory: db eingefügt worden sein |

| 03 | test_insert_category | Es soll getestet werden ob sich eine Kategorie in die Tabelle Kategorie mit der Methode **insert_Category**, welche in der Klasse Insert implementiert wurde, einfügen lässt. Als Test-Datenbank wird eine :memory: db verwendet | Testdaten: Kategorie, Contact_ID | Die Testdaten sollten erfolgreich in die Tabelle Kategorie der :memory: db eingefügt worden sein |

| 03 | test_insert_phone_number | Es soll getestet werden ob sich eine Tel.-Nr. in die Tabelle PhoneNumber mit der Methode **insert_PhoneNumber**, welche in der Klasse Insert implementiert wurde, einfügen lässt. Als Test-Datenbank wird eine :memory: db verwendet | Testdaten: Tel.-Nr., Contact_ID | Die Testdaten sollten erfolgreich in die Tabelle PhoneNumber der :memory: db eingefügt worden sein |
