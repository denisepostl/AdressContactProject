# User story Kontakt hinzufügen
Als Benutzer möchte ich einen neuen Kontakt in das System hinzufügen können. Ein Bild von einem Kontakt möchte ich auch hinzufügen.
Als Entwickler brauche ich folgende Inputs: Vorname, Nachname, Tel. und Adresse. Und Bild.

**Actors**  <br>
Benutzer

**Input**  <br>
Eingabe von Vorname (Typ: VARCHAR), Nachname (Typ: VARCHAR), Tel. (Typ: VARCHAR) und Adresse (Ort u. Straße Typ: VARCHAR | PLZ u. Hausnummer Typ: Integer) in einzelnen Textfeldern. 
Hinzufügen des neuen Kontaktes funktioniert dann über einen Button.
Hinzufügen eines Bildes (Format: jpg oder png) soll auch über einen Button funktionieren.

**Background** <br>
Die eingegebenen Daten werden in einer Datenbank gespeichert.
Ich werde eine eigene Methode schreiben, die es mir mithilfe eines INSERT - Querys ermöglicht die Datensätze in der DB zu speichern.
Mithilfe eines SELECTS-Querys (ich mache eine eigene Methode dafür) frage ich die Datenbank nach den neu hinzugefügten Namen ab (eine eigene Variable wird benötigt die ich dann bei der SELECT-Methode verwende) und gebe den hinzugefügten Datensatz aus.
Über einen Button soll der Benutzer nach Bildern lokal im Explorer suchen können. Ich werde für den Image import Pillow verwenden. Das Bild werde ich dann in einem Ordner abspeichern.


**Internal State change**  <br>
Benutzer wurde hinzugefügt.

**Output**  <br>
Eventuell die neu eingefügten Kontaktdaten.
Bei der Ausgabe sollen alle Daten in einer Zeile ausgegeben werden. 
Ich muss daher auf die Foreign Keys der jeweiligen Tabellen achten (Für das Verbinden der Tabellen werde ich joins verwenden).

**Errors**  <br>
Wenn der Benutzer einen falschen Datentyp verwendet wird ein Error erscheinen. - Ich werde Exceptions verwenden. 
Wenn der Benutzer den gleichen Vor-u. Nachnamen eingibt, der in der Datenbank vorhanden ist, werde ich nachfragen ob das gewünscht ist.

----------------------------------------------------------------------------------------

# User story Kontakt löschen
Als Benutzer möchte ich einen Kontakt anhand Vor-u. Nachnamen und anschließender Auswahl löschen können.
Als Entwickler muss ich wissen welchen Kontakt der Benutzer löschen will.

**Actors**  <br>
Benutzer

**Input**  <br>
Eingabe von Vor-und Nachnamen (Typ: VARCHAR) und anschließende Auswahl vom Kontakt durch den Benutzer. 
Vor- und Nachname kann in ein Textfeld eingegeben werden. Danach wird ein Kontakt od. mehrere wenn gleiche Namen vorhanden sind ausgegeben und der Benutzer kann seinen Kontakt dann auswählen.

**Background** <br>
Nachdem der Benutzer den zu löschenden Kontakt ausgewählt hat, werde ich ihn fragen ob er wirklich diesen Kontakt löschen möchte. Dann werde ich mithilfe eines DELETE Querys (welches in einer Methode deklariert wird) den Kontakt löschen.
Da die Tabelle Contact in Relation mit Adress und Phonenumber steht muss ich die FK's berücksichtigen (Ich muss die Tabellen Joinen). 
Nach der Reihe werden dann die einzelnen Datensätze in den Tabellen der Datenbank gelöscht.

**Internal State change**  <br>
Kontakt wurde gelöscht.

**Output**  <br>
Ich frage ob der Benutzer wirklich den Kontakt löschen möchte - wenn Ja gebe ich folgendes aus (vielleicht in einem neuen kleinen Fenster das aufscheint): 
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
Ich lass ihn zuerst Vor-u. Nachname (Typ: VARCHAR) eingeben und danach soll der Benutzer den entsprechenden Kontakt auswählen (ev. in einer Tabelle oder über Buttons zum bestätigen ob das der richtige Kontakt ist).
Anschließend kann der Benutzer den Kontakt aktualisieren - er kann nun neue Daten eingeben.

**Background** <br>
Nachdem der Benutzer den zu aktualisierten Kontakt ausgewählt hat, werde ich mithilfe einer Methode, in der ich ein Update Query deklarieren werde, die 
zu aktualisierenden Datensätze überschreiben. Anschließend frage ich mit einem SELECT QUERY (welches in einer Methode deklariert wird) den aktualisierten Kontakt ab und gebe diesen aus.

**Internal State change**  <br>
Kontakt wurde aktualisiert.

**Output**  <br>
Es wird dann folgendes ausgegeben:
    - "Ihr Kontakt wurde erfolgreich aktualisiert." (ev. erscheint ein neues, kleines Fenster)

Und der aktualisierte Kontakt soll mit den neuen Datensätzen ausgegeben werden.


**Errors**  <br>
Wenn kein Kontakt unter diesem Namen gefunden wurde, gibt es eine Exception: "Es wurde kein Kontakt unter diesem Namen gefunden."
Wenn falsche Datentypen für den Vornamen und Nachnamen eingegeben wurde, wird es auch eine Exception geben: "Bitte beachten Sie den Datentyp"

----------------------------------------------------------------------------------------

# User story Kontaktabfrage
Als Benutzer möchte ich einen bestimmten Kontakt abfragen können oder alle.
Als Entwickler muss ich wissen welchen Kontakt der Benutzer abfragen will und ob er nur einen oder alle Kontakte sehen möchte.

**Actors**  <br>
Benutzer

**Input**  <br>
Ich werde eine Auswahl mit 2 Buttons benötigen: "Alle Kontakte abfragen" | "Einen speziellen Kontakt abfragen"

Wenn ein bestimmter Kontakt abgefragt werden soll benötige ich vom Benutzer:
    - Eingabe von Vorname, Nachname (Typ: VARCHAR)
    - Eingabe von Telefonnummer (Typ: Integer)
Danach gebe ich den Kontakt aus.
Ansonsten kann der Benutzer auf einen Button drücken: Alle Kontakte abfragen

**Background** <br>
Nachdem der Benutzer eingegeben hat ob er einen oder alle Kontakte abfragen möchte werde ich mithilfe einer Methode, in der ein SELECT QUERY deklariert ist
die jeweiligen Datensätze ausgeben.


**Internal State change**  <br>
Kontakt wird ausgegeben.

**Output**  <br>
Die Kontaktdaten werden ausgegeben. Entweder nur die spezifischen von einem Kontakt oder alle.
Das gespeicherte Kontaktbild wird daneben ausgegeben.

**Errors**  <br>
Wenn kein Kontakt unter einem bestimmten Namen gefunden wurde gibt es eine Exception: "Es wurde kein Kontakt unter diesem Namen gefunden".
Wenn falsche Datentypen für die Abfrage verwendet wurden wird es auch eine Exception geben: "Bitte Datentyp beachten"

----------------------------------------------------------------------------------------

# User story GUI
Als Benutzer möchte ich die Kontaktdaten in einer GUI sehen, speichern, löschen oder ändern können. Ein erstes Window sollte mir eine Auswahl ermöglichen was ich mit den Kontaktdaten tun möchte. Anschließend soll das entsprechende Window mit z.B.: Kontakt einfügen kommen, wo man zu anderen Windows navigieren kann. Zum Startfenster kommt man nur beim erstmaligen Start der Anwendung.

**Actors**  <br>
Benutzer

**Background** <br>
Wenn der Benutzer auf einen Button drückt, dann wird eine Funktion aufgerufen. Zum Beispiel will der Benutzer einen Kontakt hinzufügen, dann rufe ich eine Funktion auf
die mir das Main-Window der Kontakt-Hinzufüge Option aufruft. In diesem Window befindet sich dann ein ADD-Contact Button über den eine Funktion aufgerufen wird
die mir Datensätze mithilfe von einem INSERT QUERY zur Datenbank hinzufügt. Jeweilige Kontakt-Abfragen, Kontakt-Löschen, Kontakt-Ändern Buttons sollen am Rand angeführt sein wo der Benutzer dann durch Klicken auf ein neues Window hinkommt. z.B.: klickt er auf Kontakt-Abfragen, dann kann er hier einen Kontakt auswählen und abfragen. (eine entsprechende Funktion muss das navigieren zu diesem neuen Window im Kontakt-Abfragen Button des Main-Windows vom Kontakt-Hinzufügen ermöglichen)
Und auch bei den anderen beiden Optionen: Kontakt-Löschen und Kontakt-Ändert funktioniert das navigieren in die jeweils anderen Optionen bzw. Windows gleich (sprich: über eine Funktion wird das jeweils andere Window aufgerufen). <br> <br>
    - Beim Kontakt-Hinzufügen Window gibt es einen Button Kontakt-Hinzufügen. Mithilfe eines INSERT Querys, das in einer Methode deklariert ist, werden neue Datensätze in die Datenbank eingefügt. <br> <br>
    - Beim Kontakt-Löschen Window gibt es einen Button Kontakt-Löschen. Mithilfe eines DELETE Querys, das in einer Methode deklariert ist, wird der entsprechend ausgewählte Kontakt gelöscht. Vorher wird der Kontakt durch Eingabe von Vor- u. Nachname vom Benutzer ausgewählt.  <br> <br>
    - Beim Kontakt-Ändern Window gibt es einen Button Kontakt-Ändern. Mithilfe eines UPDATE Querys, das in einer Methode deklariert ist, wird der entsprechend ausgewählte Kontakt aktualisiert. Der Benutzer kann hier ähnlich wie beim DELETE seinen Kontakt auswählen und dementsprechnd neue Daten in neuen Textfeldern eingeben, die dann übernommen werden. <br> <br>
    - Beim Kontakt-Abfrage Window gibt es zwei Buttons: Einen Kontakt abfragen | alle Kontakte abfragen. Mithilfe eines SELECT Querys wird entweder ein Datensatz abgefragt (durch Eingabe von Vor- u. Nachname) oder alle Datensätze. Der Benutzer kann hier in jeweils einem Textfeld Vor- u. Nachname od. Telefonnummer eingeben.

**Input**  <br>
Auswahl der entsprechenden Tätigkeiten die gemacht werden möchten.

**Internal State change**  <br>
Die gewünschte Option wird durchgeführt z.B.: switchen auf das Benutzer-Hinzufügen Window.

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

**Background** <br>
Mithilfe eines UPDATE Querys, das in einer Methode deklariert wird, wird die dementsprechende Kategorie zu schon vorhandenden Datensätzen hinzugefügt. Mithilfe eines INSERT Querys, das in einer Methode deklariert wird, wird die dementsprechende Kategorie zu neuen Datensätzen hinzugefügt. Mit betätigen des Buttons wird die jeweilige Funktion aufgerufen und die Aktualisierung bzw. das Hinzufügen der Kategorie vorgenommen.

**Input**  <br>
Es wird einen Button "Kategorie" geben, wo der Benutzer dann die Kategorie hinzufügen kann.
Bestehende Kontakte können ausgewählt werden und anschließend auch kategorisiert werden. - Dieses Feature wird dann in Kontakt-ändern eingebaut werden.
Auswahl der entsprechenden Kategorie durch den Benutzer bei einem spezifischen Kontakt.

**Internal State change**  <br>
Die Kategorie wurde erfolgreich hinzugefügt / aktualisiert.

**Output**  <br>
Kontaktdaten mit Kategorie.

**Errors**  <br>
Wenn kein Kontakt unter einem bestimmten Namen existiert dann gibt es eine Exception: "Es wurde kein Kontakt unter diesem Namen gefunden."

----------------------------------------------------------------------------------------
