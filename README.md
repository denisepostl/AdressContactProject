# Address-Datenbank ✆

### Ziel

Ein Benutzer kann 

    - Kontaktdaten speichern (Vorname, Nachname, Ort, PLZ, Straße, Hausnummer, Telefonnummer)

    - gespeicherte Kontakte auflisten (alle/od. definierte anhand Vor-/und Nachname)

    - Kontaktinformationen aktualisieren (durch Eingabe von Vor-/und Nachname kann er neue Informationen hinzufügen)

    - Kontaktinformationen löschen (Der ganze Kontakt wird gelöscht. Vorher wird der Kontakt noch einmal ausgegeben und gefragt ob das der richtige Kontakt ist.)

    - Bild (z.B.: Profilbild) vom lokalen Rechner zu einem Kontakt hinzufügen (durch betätigen eines Buttons kann er ein Bild auswählen, welches dann in einem neuen   Ordner abgespeichert wird, damit es später bei der Abfrage eines Kontakts angezeigt werden kann)

Ein Kontakt kann beliebig viele Adressen und Telefonnummern zugewiesen bekommen. In diesem Projekt wurde dies angenommen.
Eine schönere Lösung hätte man allerdings wenn man den Benutzer eine begrenzte Anzahl an Telefonnummern und Adressen zuweisen lässt.
Dieser Weg wurde implementiert und dafür wurde folgendes Datenmodell angenommen:
![Datenmodell](https://github.com/denisepostl/AdressContactProject/blob/main/img/datamodel_new.png)

### User-Stories
Die User-Stories befinden sich unter: [doc](https://github.com/denisepostl/AdressContactProject/blob/main/doc/UserStory.md)

### Tests

Die dokumentierten Testfälle befinden sich unter: [doc](https://github.com/denisepostl/AdressContactProject/blob/main/doc/TestCases.md)

### Feature

    - Kontakt gehört zur Familie/Freunde (Eigene Tabelle: Roles notwendig, die zur Contact-Tabelle referenziert)

### Verwendung von Python, SQLite und TKinter

Es wird eine SQLite Datenbank für die Speicherung von Address-Daten verwendet. Mit TKinter soll ein GUI erstellt werden und die Datenbank muss dementsprechend verbunden werden.

### Datenmodell (Stand: 20.01.2023)

![Datenmodell](https://github.com/denisepostl/AdressContactProject/blob/main/datamodel/datamodel.png)

Wegen der möglicherweise führenden Nullen die bei Telefonnummer, PLZ u. Hausnummer auftreten könnten habe ich mich für die Telefonnummer und PLZ für den Datentyp VARCHAR entschieden und für die Hausnummer verwende ich den Datentyp NVARCHAR.

### Datenmodell für das Feature: Kategorie (Stand: 20.01.2023)

![Datenmodell](https://github.com/denisepostl/AdressContactProject/blob/main/img/DatamodellExtension.png)

### Query SqLite

Für die Erstellung der Datenbank kann [create_database.py](https://github.com/denisepostl/AdressContactProject/blob/main/adress/create_database.py) ausgeführt werden.
Anschließend werden die Tabellen in der Datenbank *adress.db* erstellt. <br>
Das SQL-File mit den CREATE Table Statements und die Datenbank befinden sich unter: [database](https://github.com/denisepostl/AdressContactProject/tree/main/database)

### Kommandozeilenprogramm

Beim Ausführen von [main_contact.py](https://github.com/denisepostl/AdressContactProject/tree/main/adress/main_contact.py) kann ein kleines Kommandozeilenprogramm ausprobiert werden, dass den Benutzern erlaubt einen Kontakt hinzuzufügen, abfragen, Kontaktdaten ändern und zu löschen. 

### Kleines Benutzerhandbuch

Eine kurze Dokumentation über die Funktionalitäten befindet sich unter: [doc](https://github.com/denisepostl/AdressContactProject/blob/main/doc/UserDoc.md)


