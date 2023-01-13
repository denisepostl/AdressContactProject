# User story Kontakt hinzufügen
Als Benutzer möchte ich einen neuen Kontakt in das System hinzufügen können.

**Actors**  <br>
Benutzer

**Input**  <br>
Eingabe von Vorname, Nachname, Tel. und Adresse.

**Internal State change**  <br>
Acknowledgement.

**Output**  <br>
Eventuell die neu eingefügten Kontaktdaten.

**Errors**  <br>
Falscher Datentyp. 
Gleicher Vor-u. Nachname (Nachfragen ob das gewünscht ist)

----------------------------------------------------------------------------------------

# User story Kontakt löschen
Als Benutzer möchte ich einen Benutzer anhand Vor-u. Nachnamen und anschließender Auswahl löschen können.

**Actors**  <br>
Benutzer

**Input**  <br>
Eingabe von Vor-und Nachnamen und anschließende Auswahl vom Kontakt.

**Internal State change**  <br>
Already deleted Contact.

**Output**  <br>
Nachfragen ob der Benutzer wirklich den Kontakt löschen möchte - wenn Ja: 
"Der Kontakt wurde erfolgreich gelöscht."

**Errors**  <br>
Es wurde kein Kontakt mit diesem Namen gefunden.

----------------------------------------------------------------------------------------

# User story Kontaktupdate
Als Benutzer möchte ich Daten für einen Kontakt aktualisieren.

**Actors**  <br>
Benutzer

**Input**  <br>
Auswahl des Kontakts. (Eingabe von Vor-u. Nachname u. anschließende Auswahl)
Eingabe von aktualisierten Daten.

**Internal State change**  <br>
Deleted Contact.

**Output**  <br>
"Ihr Kontakt wurde erfolgreich aktualisiert:"
Der aktualisierte Kontakt soll ausgegeben werden.


**Errors**  <br>
Es wurde kein Kontakt unter diesem Namen gefunden.

----------------------------------------------------------------------------------------

# User story Kontaktabfrage
Als Benutzer möchte ich einen bestimmten Kontakt abfragen können oder alle.

**Actors**  <br>
Benutzer

**Input**  <br>
Wenn ein bestimmter Kontakt abgefragt werden soll:
    - Eingabe von Vorname, Nachname und anschließende Ausgabe dieses Kontakts
Ansonsten Klick auf einem Button: Alle Kontakte abfragen

**Internal State change**  <br>
Deleted Contact.

**Output**  <br>
Kontaktdaten.

**Errors**  <br>
Es wurde kein Kontakt unter diesem Namen gefunden.

----------------------------------------------------------------------------------------

# User story GUI
Als Benutzer möchte ich die Kontaktdaten in einer GUI sehen, speichern, löschen oder ändern können. Ein erstes Window sollte mir eine Auswahl ermöglichen was ich mit den Kontaktdaten tun möchte. Anschließend soll das entsprechende Window mit z.B.: Kontakt einfügen kommen, wo man zu anderen Windows navigieren kann. Zum Startfenster kommt man nur beim erstmaligen Start der Anwendung.

**Actors**  <br>
Benutzer

**Input**  <br>
Auswahl der entsprechenden Tätigkeiten die gemacht werden möchten.

**Output**  <br>
Graphische Oberfläche.
Kontaktdaten.

----------------------------------------------------------------------------------------

# User story Feature: Kategorie
Als Benutzer möchte ich meine Kontakte anhand einer Kategorie kennzeichnen.
Wenn es sich z.B.: um ein Familienmitglied handelt, soll sich diese Kategorie auswählen lassen.
Auswahlmöglichkeiten:
    - Familie
    - Freunde
    - Schulkollegen
    - Arbeitskollegen
    - ...

**Actors**  <br>
Benutzer

**Input**  <br>
Auswahl der entsprechenden Kategorie.


**Output**  <br>
Kontaktdaten mit Kategorie.

**Errors**  <br>
Es wurde kein Kontakt unter diesem Namen gefunden.

----------------------------------------------------------------------------------------
