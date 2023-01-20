# Address-Datenbank ✆

### Ziel

Ein Benutzer kann 

    - Kontaktdaten speichern (Vorname, Nachname, Ort, PLZ, Straße, Hausnummer, Telefonnummer)

    - gespeicherte Kontakte auflisten (alle/od. definierte anhand Vor-/und Nachname)

    - Kontaktinformationen aktualisieren (durch Eingabe von Vor-/und Nachname kann er neue Informationen hinzufügen)

    - Kontaktinformationen löschen (Der ganze Kontakt wird gelöscht. Vorher wird der Kontakt noch einmal ausgegeben und gefragt ob das der richtige Kontakt ist.)

    - Bild (z.B.: Profilbild) vom lokalen Rechner zu einem Kontakt hinzufügen (durch betätigen eines Buttons kann er ein Bild auswählen, welches dann in einem neuen   Ordner abgespeichert wird, damit es später bei der Abfrage eines Kontakts angezeigt werden kann)

Ein Kontakt kann mehr als eine Telefonnummer/Adresse haben.

### User-Stories
Die User-Stories befinden sich unter: [doc](https://github.com/denisepostl/AdressContactProject/blob/main/doc/UserStory.md)

### Feature

    - Kontakt gehört zur Familie/Freund (Eigene Tabelle: Roles notwendig, die zur Contact-Tabelle referenziert)

### Verwendung von Python, SQLite und TKinter

Es wird eine SQLite Datenbank für die Speicherung von Address-Daten verwendet. Mit TKinter soll ein GUI erstellt werden und die Datenbank muss dementsprechend verbunden werden.

### Datenmodell (Stand: 20.01.2023)

![Datenmodell](https://github.com/denisepostl/AdressContactProject/blob/main/datamodel/datamodel.png)

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






