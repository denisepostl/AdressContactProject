# User story Kontakt hinzufügen
Als Benutzer möchte ich einen neuen Kontakt in das System hinzufügen können.
Als Entwickler brauche ich folgende Inputs: Vorname, Nachname, Tel. und Adresse.

**Actors**  <br>
Benutzer

**Input**  <br>
Eingabe von Vorname, Nachname, Tel. und Adresse in einzelnen Textfeldern. 
Hinzufügen des neuen Kontaktes funktioniert dann über einen Button.


**Internal State change**  <br>
Acknowledgement.

**Output**  <br>
Eventuell die neu eingefügten Kontaktdaten.
Bei der Ausgabe sollen alle Daten in einer Zeile ausgegeben werden. 
Ich muss daher auf die Foreign Keys der jeweiligen Tabellen achten.

**Errors**  <br>
Wenn der Benutzer einen falschen Datentyp verwendet wird ein Error erscheinen. - Ich werde Exceptions verwenden. 
Wenn der Bentuzer den gleichen Vor-u. Nachnamen eingibt, der in der Datenbank vorhanden ist, werde ich nachfragen ob das gewünscht ist.

----------------------------------------------------------------------------------------

# User story Kontakt löschen
Als Benutzer möchte ich einen Kontakt anhand Vor-u. Nachnamen und anschließender Auswahl löschen können.
Als Entwickler muss ich wissen welchen Kontakt der Benutzer löschen will.

**Actors**  <br>
Benutzer

**Input**  <br>
Eingabe von Vor-und Nachnamen und anschließende Auswahl vom Kontakt durch den Benutzer.
Vor- und Nachname kann in ein Textfeld eingegeben werden. Danach wird ein Kontakt od. mehrere wenn gleiche Namen vorhanden sind und der Benutzer kann
seinen Kontakt dann auswählen.

**Internal State change**  <br>
Already deleted Contact.

**Output**  <br>
Ich frage ob der Benutzer wirklich den Kontakt löschen möchte - wenn Ja: 
"Der Kontakt wurde erfolgreich gelöscht."

**Errors**  <br>
Wenn kein Kontakt mit diesem Namen gefunden wurde gibt es eine Exception: "Es wurde kein Kontakt mit diesem Namen gefunden."

----------------------------------------------------------------------------------------

# User story Kontaktupdate
Als Benutzer möchte ich Daten für einen Kontakt aktualisieren.
Als Entwickler muss ich wissen, welchen Kontakt und welche Datensätze der Benutzer aktualisieren möchte.

**Actors**  <br>
Benutzer

**Input**  <br>
Der Benutzer muss den entsprechenden Kontakt auswählen. 
Ich lass ihn zuerst Vor-u. Nachname eingeben und danach soll der Benutzer den entsprechenden Kontakt auswählen.
Anschließend kann der Benutzer den Kontakt aktualisieren.

**Internal State change**  <br>
Deleted Contact.

**Output**  <br>
Es wird dann folgendes ausgeben:
    - "Ihr Kontakt wurde erfolgreich aktualisiert."

Und der aktualisierte Kontakt soll mit den neuen Datensätzen ausgegeben werden.


**Errors**  <br>
Wenn kein Kontakt unter diesem Namen gefunden wurde gibt es eine Exception: "Es wurde kein Kontakt unter diesem Namen gefunden."

----------------------------------------------------------------------------------------

# User story Kontaktabfrage
Als Benutzer möchte ich einen bestimmten Kontakt abfragen können oder alle.
Als Entwickler muss ich wissen welchen Kontakt der Benutzer abfragen will und ob er nur einen oder alle Kontakte sehen möchte.

**Actors**  <br>
Benutzer

**Input**  <br>
Ich werde eine Auswahl mit 2 Buttons benötigen: "Alle Kontakte abfragen" | "Einen speziellen Kontakt abfragen"

Wenn ein bestimmter Kontakt abgefragt werden soll benötige ich vom Benutzer:
    - Eingabe von Vorname, Nachname 
Danach gebe ich den Kontakt aus.
Ansonsten kann der Benutzer auf einen Button drücken: Alle Kontakte abfragen

**Internal State change**  <br>
Deleted Contact.

**Output**  <br>
Die Kontaktdaten werden ausgegeben.

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
Kontaktdaten können aktualisiert, geändert, gelöscht oder abgefragt werden.

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

Als Entwickler benötige ich eine Auswahl vom Benutzer. Danach kann ich den Kontakt dementsprechend kategorisieren.

**Actors**  <br>
Benutzer

**Input**  <br>
Es wird einen Button "Kategorie" geben, wo er Benutzer dann die Kategorie hinzufügen kann.
Bestehende Kontakte können ausgewählt werden und anschließend auch kategorisiert werden. - Dieses Feature wird dann in Kontakt-ändern eingebaut werden.
Auswahl der entsprechenden Kategorie durch den Benutzer bei einem spezifischen Kontakt.

**Output**  <br>
Kontaktdaten mit Kategorie.

**Errors**  <br>
Wenn kein Kontakt unter einem bestimmten Namen existiert dann gibt es eine Exception: "Es wurde kein Kontakt unter diesem Namen gefunden."

----------------------------------------------------------------------------------------
