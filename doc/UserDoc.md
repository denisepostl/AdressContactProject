# User story Kontakt hinzufügen
Als Benutzer möchte ich einen neuen Kontakt in das System hinzufügen können. Ein Bild von einem Kontakt möchte ich auch hinzufügen.
Als Entwickler brauche ich folgende Inputs: Vorname, Nachname, Tel. und Adresse. Und Bild.

**Actors**  <br>
Benutzer

**Input**  <br>
Eingabe von Vorname (Typ: VARCHAR), Nachname (Typ: VARCHAR), Tel. (Typ: VARCHAR) und Adresse (Ort u. Straße Typ: VARCHAR | PLZ (VARCHAR)u. Hausnummer Typ: NVARCHAR - wegen der führenden Nullen die möglich sein könnten (international)) in einzelnen Textfeldern. 
Hinzufügen des neuen Kontaktes funktioniert dann über einen Button.
Hinzufügen eines Bildes (Format: jpg oder png) soll auch über einen Button funktionieren.

**Background** <br>
Die eingegebenen Daten werden in einer Datenbank gespeichert.
Ich werde eine eigene Methode schreiben, die es mir mithilfe eines INSERT - Querys ermöglicht die Datensätze in der DB zu speichern.
Mithilfe eines SELECT-Querys (ich mache eine eigene Methode dafür) frage ich die Datenbank nach den neu hinzugefügten Namen ab (eigene Variablen werden benötigt (für die Inputs des Benutzers in den Textfeldern) die ich dann bei der SELECT-Methode verwende) und gebe den hinzugefügten Datensatz aus.
Über einen Button soll der Benutzer nach Bildern lokal im Explorer suchen können. Ich werde für den Image import Pillow verwenden. Das Bild werde ich dann in einem Ordner abspeichern.
