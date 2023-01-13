# Address-Datenbank ✆

### Ziel

Ein Benutzer kann 

    - Kontaktdaten speichern (Vorname, Nachname, Ort, PLZ, Straße, Hausnummer, Telefonnummer)

    - gespeicherte Kontakte auflisten (alle/od. definierte anhand Vor-/und Nachname)

    - Kontaktinformationen aktualisieren (durch Eingabe von Vor-/und Nachname kann er neue Informationen hinzufügen)

    - Kontaktinformationen löschen (Der ganze Kontakt wird gelöscht. Vorher wird der Kontakt noch einmal ausgegeben und gefragt ob das der richtige Kontakt ist.)

Ein Kontakt kann mehr als eine Telefonnummer/Adresse haben.

### User-Stories
Die User-Stories befinden sich unter: [doc](https://github.com/denisepostl/AdressContactProject/tree/main/doc)

### Feature

    - Kontakt gehört zur Familie/Freund (Eigene Tabelle: Roles notwendig, die zur Contact-Tabelle referenziert)

### Verwendung von Python, SQLite und TKinter

Es wird eine SQLite Datenbank für die Speicherung von Address-Daten verwendet. Mit TKinter soll ein GUI erstellt werden und die Datenbank muss dementsprechend verbunden werden.

### Datenmodell (Stand: 12.01.2023)

![Datenmodell](https://github.com/denisepostl/AdressContactProject/blob/main/datamodel/datamodel.png)

### Beim Ausführen des Programms soll folgender Screen erscheinen: (Stand: 12.01.2023)

![StartScreen](https://github.com/denisepostl/AdressContactProject/blob/main/img/StartScreen.png)

### Query SqLite

Das Query für die Erstellung der Tabellen, welches sich im File *adress_table.sql* befindet wurde ausgeführt. <br>
Anschließend wurden die Tabellen in der Datenbank *adress.db* erstellt. <br>
Das SQL-File und die Datenbank befinden sich unter: [database](https://github.com/denisepostl/AdressContactProject/tree/main/database)

### Kommandozeilenprogramm

Beim ausführen von [main_contact.py](https://github.com/denisepostl/AdressContactProject/tree/main/adress/main_contact.py) kann ein kleines Kommandozeilenprogramm ausprobiert werden, das den Benutzern erlaubt einen Kontakt hinzuzufügen, abfragen, Kontaktdaten ändert und löscht. 






