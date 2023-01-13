# Address-Datenbank ✆

### Ziel

Ein Benutzer kann 

    - Kontaktdaten speichern (Vorname, Nachname, Ort, PLZ, Straße, Hausnummer, Telefonnummer)

    - gespeicherte Kontakte auflisten (alle/od. definierte anhand Vor-/und Nachname)

    - Kontaktinformationen aktualisieren (durch Eingabe von Vor-/und Nachname kann er neue Informationen hinzufügen)

    - Kontaktinformationen löschen (Der ganze Kontakt wird gelöscht. Vorher wird der Kontakt noch einmal ausgegeben und gefragt ob das der richtige Kontakt ist.)

Ein Kontakt kann mehr als eine Telefonnummer/Adresse haben.

### Feature

    - Kontakt gehört zur Familie/Freund (Eigene Tabelle: Roles notwendig, die zur Contact-Tabelle referenziert)

### Verwendung von Python, SQLite und TKinter

Es wird eine SQLite Datenbank für die Speicherung von Address-Daten verwendet. Mit TKinter soll ein GUI erstellt werden und die Datenbank muss dementsprechend verbunden werden.

### Datenmodell

![Datenmodell](https://github.com/denisepostl/adress_project/blob/main/datamodel/datamodel.png)

### Beim Ausführen des Programms soll folgender Screen erscheinen:

![StartScreen](https://github.com/denisepostl/adress_project/blob/main/img/StartScreen.png)

