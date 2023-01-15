# User story Kontakt hinzufügen
Als Benutzer möchte ich einen neuen Kontakt in das System hinzufügen können. Ein Bild von einem Kontakt möchte ich auch hinzufügen.
Als Entwickler brauche ich folgende Inputs: Vorname, Nachname, Tel. und Adresse. Und Bild.

**Actors**  <br>
Benutzer

**Input**  <br>
Eingabe von Vorname, Nachname, Tel. und Adresse in einzelnen Textfeldern. 
Hinzufügen des neuen Kontaktes funktioniert dann über einen Button.
Hinzufügen eines Bildes soll auch über einen Button funktionieren.

**Background** <br>
Die Eingegebenen Daten werden in einer Datenbank gespeichert.
Ich werde eine eigene Methode schreiben, die es mir mithilfe eines INSERT - Querys ermöglicht die Datensätze zu speichern.
Mithilfe eines SELECTS-Querys frage ich die Datenbank nach den neu hinzugefügten Namen ab und gebe den hinzugefügten Datensatz aus.


**Internal State change**  <br>
Acknowledgement.

**Output**  <br>
Eventuell die neu eingefügten Kontaktdaten.
Bei der Ausgabe sollen alle Daten in einer Zeile ausgegeben werden. 
Ich muss daher auf die Foreign Keys der jeweiligen Tabellen achten.

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
Eingabe von Vor-und Nachnamen und anschließende Auswahl vom Kontakt durch den Benutzer.
Vor- und Nachname kann in ein Textfeld eingegeben werden. Danach wird ein Kontakt od. mehrere wenn gleiche Namen vorhanden sind ausgegeben und und der Benutzer kann
seinen Kontakt dann auswählen.

**Background** <br>
Nachdem der Benutzer den zu löschenden Kontakt ausgewählt hat, werde ich ihn fragen ob er wirklich diesen Kontakt löschen möchte. Dann werde ich mithilfe eines DELETE Querys den Kontakt löschen.
Da die Tabelle Contact in Relation mit Adress und Phonenumber steht muss ich die FK's berücksichtigen. 
Nach der Reihe werde ich dann die einzelnen Datensätze in den Tabellen der Datenbank löschen.

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

**Background** <br>
Nachdem der Benutzer den zu aktualisierten Kontakt ausgewählt hat, werde ich mithilfe einer Methode, in der ich ein Update Query deklarieren werde, die 
zu aktualisierenden Datensätze überschreiben. Anschließend frage ich mit einem SELECT QUERY den aktualisierten Kontakt ab und gebe diesen aus.

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

**Background** <br>
Nachdem der Benutzer eingegeben hat ob er einen oder alle Kontakte abfragen möchte werde ich mithilfe einer Methode, in der ein SELECT QUERY deklariert ist
die jeweiligen Datensätze ausgeben.


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

**Background** <br>
Wenn der Benutzer auf einen Button drückt, dann wird eine Funktion aufgerufen. Zum Beispiel will der Benutzer einen Kontakt hinzufügen, dann rufe ich eine Funktion auf
die mir das Main-Window der Kontakt-Hinzufüge Option aufruft. In diesem Window befindet sich dann ein ADD-Contact Button über den eine Funktion aufgerufen wird
die mir Datensätze mithilfe von einem INSERT QUERY zur Datenbank hinzufügt. Jeweilige Kontakt-Abfragen, Kontakt-Löschen, Kontakt-Ändern Button sollen am Rand angeführt sein wo der Benutzer dann durch Klicken auf ein neues Window hinkommt. z.B.: klickt er auf Kontakt-Abfragen, dann kann er hier einen Kontakt auswählen und abfragen. (eine entsprechende Funktion muss das navigieren zu diesem neuen Window im Kontakt-Abfragen Button des Main-Windows vom Kontakt-Hinzufügen ermöglichen)
Und auch bei den anderen beiden Optionen: Kontakt-Löschen und Kontakt-Ändert funktioniert das navigieren in die jeweils anderen Optionen bzw. Windows gleich (sprich: über eine Funktion wird das jeweils andere Window aufgerufen). <br> <br>
    - Beim Kontakt-Hinzufügen Window gibt es einen Button Kontakt-Hinzufügen. Mithilfe eines INSERT Querys, das in einer Methode deklariert ist, werden neue Datensätze in die Datenbank eingefügt. <br> <br>
    - Beim Kontakt-Löschen Window gibt es einen Button Kontakt-Löschen. Mithilfe eines DELETE Querys, das in einer Methode deklariert ist, wird der entsprechend ausgewählte Kontakt gelöscht. <br> <br>
    - Beim Kontakt-Ändern Window gibt es einen Button Kontakt-Ändern. Mithilfe eines UPDATE Querys, das in einer Methode deklariert ist, wird der entsprechend ausgewählte Kontakt aktualisiert. <br> <br>
    - Beim Kontakt-Abfrage Window gibt es zwei Buttons: Einen Kontakt abfragen | alle Kontakte abfragen. Mithilfe eines SELECT Querys wird entweder ein Datensatz abgefragt (durch Eingabe von Vor- u. Nachname) oder alle Datensätze.

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

**Background** <br>
Mithilfe eines UPDATE Querys, das in einer Methode deklariert wird, wird die dementsprechende Kategorie zu schon vorhandenden Datensätzen hinzugefügt. Mithilfe eines INSERT Querys, das in einer Methode deklariert wird, wird die dementsprechende Kategorie zu neuen Datensätzen hinzugefügt. Mit betätigen des Buttons wird die jeweilige Funktion aufgerufen und die Aktualisierung bzw. das Hinzufügen der Kategorie vorgenommen.

**Input**  <br>
Es wird einen Button "Kategorie" geben, wo der Benutzer dann die Kategorie hinzufügen kann.
Bestehende Kontakte können ausgewählt werden und anschließend auch kategorisiert werden. - Dieses Feature wird dann in Kontakt-ändern eingebaut werden.
Auswahl der entsprechenden Kategorie durch den Benutzer bei einem spezifischen Kontakt.

**Output**  <br>
Kontaktdaten mit Kategorie.

**Errors**  <br>
Wenn kein Kontakt unter einem bestimmten Namen existiert dann gibt es eine Exception: "Es wurde kein Kontakt unter diesem Namen gefunden."

----------------------------------------------------------------------------------------
