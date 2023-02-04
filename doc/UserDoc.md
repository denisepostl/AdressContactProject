# StartScreen
Beim Auführen von [main_gui](https://github.com/denisepostl/AdressContactProject/blob/main/adress/main_gui.py) erscheint folgender Start Screen:
![Screen](https://github.com/denisepostl/AdressContactProject/blob/main/img/StartScreen.png)

Hier kann der User eine beliebige Auswahl treffen. 

# Kontakt hinzufügen
![Add](https://github.com/denisepostl/AdressContactProject/blob/main/img/add.png) <br><br>
Möchte der User einen Kontakt hinzufügen, so müssen alle Datensätze im richtigen Datentyp 
eingegeben werden. Ansonsten gibt es folgende Warnung: 
![Warning](https://github.com/denisepostl/AdressContactProject/blob/main/img/Datentypwarning.png)


Darüber hinaus wird bei der Postleitzahl nur eine vierstellige Nummernfolge akzeptiert.
Ansonsten gibt es eine Fehlermeldung: 
![Error](https://github.com/denisepostl/AdressContactProject/blob/main/img/PLZError.png)

**Bild hinzufügen**
Mit Klick auf *Browse* wird Zugriff auf den Explorer des PC's gewährleistet. Der User kann nun nach einem Bild suchen und dieses auswählen.

**Kategorie hinzufügen**
Mit Klick auf *Kategorie hinzufügen* kann der User einen Kontakt einer Kategorie zuweisen.
![Kategorie](https://github.com/denisepostl/AdressContactProject/blob/main/img/Kategorie.png)

# Kontakt abfragen

Möchte der User Daten eines Kontaktes abfragen so kann er dies hier tun: 
![Abfragen](https://github.com/denisepostl/AdressContactProject/blob/main/img/Query.png)

Anhand Eingabe von Vor- u. Nachnamme oder Telefonnummer wird ein spezifischer Kontakt aufgelistet.
Weiters kann der User alle Kontakte abfragen. Beim auswählen eines Kontaktes werden die spezifischen Informationen dargestellt.

![Ask](https://github.com/denisepostl/AdressContactProject/blob/main/img/QueryALL.png)

Wird keine Telefonnummer eingegeben und versucht nach einen Kontakt zu suchen so erscheind folgende Warnung:
<br><br><br><br><br><br><br><br><br>
![Warnung](https://github.com/denisepostl/AdressContactProject/blob/main/img/telerror.png)


Auch wenn der User keinen Vor- u. Nachnamen verwendet erscheint eine Warnung: 
![Warnung](https://github.com/denisepostl/AdressContactProject/blob/main/img/Error.png)

Sind keine Datensätze gespeichert erscheint folgende Info: 

![Warnung](https://github.com/denisepostl/AdressContactProject/blob/main/img/keineDatens%C3%A4tze.png)


Ist ein Eintrag nicht vorhanden so erscheint folgende Info:
![Info](https://github.com/denisepostl/AdressContactProject/blob/main/img/EintragNichtVorhanden.png)


# Kontakt löschen

Ein Kontakt kann durch Eingabe von Vor. - u. Nachname gesucht werden. 
<br><br>
![Löschen](https://github.com/denisepostl/AdressContactProject/blob/main/img/delete.png)




Bei der Auswahl eines Kontakts mit Klick auf *Kontakt löschen* bekommt
der User folgende Meldung:
<br><br>
![Auswahl](https://github.com/denisepostl/AdressContactProject/blob/main/img/deleteask.png)


Mit betätigen des Ja Buttons wird der Kontakt aus der Datenbank gelöscht und ist somit nicht mehr im Management System vorhanden.


# Kontakt aktualisieren

Weiters hat der User die Möglichkeit verschiedene Daten eines Kontaktes zu aktualisieren. 
Nach erfolgreicher Suchde des Kontakts können mit anschließender Auswahl beliebige Änderungen vorgenommen werden. 
![Update](https://github.com/denisepostl/AdressContactProject/blob/main/img/Update.png)

Beispielsweise kann das Foto aktualisiert werden: 
<br><br>
![Photo](https://github.com/denisepostl/AdressContactProject/blob/main/img/updatephoto.png)

Eine weitere Möglichkeit wäre die Aktualisierung der Kategorie:
<br><br>
![Kategorie](https://github.com/denisepostl/AdressContactProject/blob/main/img/updatekategorie.png)

Allgemeine Daten können aktualisiert werden:
<br><br>
![UpdateData](https://github.com/denisepostl/AdressContactProject/blob/main/img/Edit.png)

Es können auch noch weitere Tel.-Nummern oder Adressen hinzugefügt werden: <br>
![Tel](https://github.com/denisepostl/AdressContactProject/blob/main/img/telhinzuf%C3%BCgen.png)
<br><br><br>>
![Adress](https://github.com/denisepostl/AdressContactProject/blob/main/img/adresseHinzuf%C3%BCge.png)

Im Hintergrund wird z.B.: eine Tel.-Nr. in die Datenbank eingefügt und die dementsprechende ID des Contacts wird hinzugegeben:
![Database](https://github.com/denisepostl/AdressContactProject/blob/main/img/phonenumberdatabase.png)
