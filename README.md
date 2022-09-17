# Open-Bot-DE
Wilkommen bei dem Open-Source Projekt "Open-Bot", das ist die Deutsche Version!
Bei diesem Projekt geht es um Discord Bots in Python, diese Anleitung wird euch durch das Setup der Bots leiten, bis zum Thema Bot-Hosting!
Dieses Projekt wird auch noch viele Updates bekommen, die auch schon in Planung sind!

### Installation der Software
Erst musst du dir Python(https://www.python.org/downloads/) runterladen und mit der PIP-Funktion installieren!
Dann musst du dir eine IDE herunterladen, ich empfehle dir Visiual Studio Code(https://code.visualstudio.com/download), deine IDE musst du dann 
installieren.
Jetzt musst du mit dem Befehl(py -3 -m pip install -U discord.py[voice]) Discordpy installieren.
WICHTIG: DU MUSST MINDESTENS PYTHON 3.8 haben!

### Erstellen der Bots
Hier(https://discord.com/developers/applications) musst du 2 Applications erstellen, jetzt musst du einmal in jede Application reingehen und einen Bot 
erstellen.
Dann musst du bei jeder im Bereich Bot, die Ersten beiden Optionen an, und die letzten drei aus.
Dann gehst du bie beiden in den Bereich OAuth2, wählst dann "bot" und applications.commands" aus, dann stellst du die Berechtigungen auf Administrator.
Jetzt musst du die Bots nur noch auf deinen Jeweiligen Server packen, dafür nutzt du den Einladungslink, der dir generiert wurde.
Als letztes musst wieder in den Bereich Bot gehen und auf "Reset Token" drücken, den Token musst darfst du nicht weitergeben, sonst kann jeder mit deinem  Bot machen was er will, den Token solltest du auch sichern, sonst kannst du den Bot nicht starten.
Den Token kannst du übrigens immer zurrücksetzen!

### Skripte für die Verbindung mit Discord bearbeiten
Du musst in Discord den Einstellungen unter Erweitert den Entwicklermodus aktivieren.
Jezt musst du dir die Skripte aus dem Ordner Skripte herunterladen.
In der letzen Zeile musst du die Token deiner Bots eingeben, also im Main-Bot  Skript den Token von deinem normalen Bot und im Server-Stats Bot Skript 
musst du den Token von deinem Server Stats Bot eingeben. 

### Erkärung einer Funktion

Bei dem Event:
```
@client.event
async def on_message(message):
    if message.author == client.user:
        return
```
gibt es die Funkiion, das der Bot auf eine Nachricht antwortet:

```
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
```

Mit dieser Funktion kann der Bot schon sehr viel, darüber läuft die Support und Voice Funktion.

### Status vom bot einstellen
```
activity = discord.Game(name="Akivität deines Bots", type=1)
```
Das "Aktivität deines Bots" kannst du gegen deine eigene Statusmeldung austauschen z.B "//help" oder was auch immer
WICHTIG : Die Anführungszeichen darfst du nicht löschen

### Einrichten der Welcome und Autoroles Funktion
```
autoroles = {
    "ID of your Server": {'memberoles': ["Memberroles"],  }
```
Hier müsst ihr bei "ID of your Server" die ID von Eurem Server eingben und bei dem "Memberroles" die Standard Rollen für normale Mitglieder.
Bei den Memberoles müsst ihr auch die ID's der Rollen einfügen.
Jetzt musst du nur noch bei ""ID from your Welcome Channel" die ID vom Wilkommenschannel eingeben.
|c


### Einrichten der Support Funktion
```
channel = await guild.create_text_channel(str(message.author))
         await channel.set_permissions(message.author,send_messages=True,read_message_history=True,read_messages=True)
         await channel.set_permissions(discord.utils.get(message.author.guild.roles, id = ("Member") ),send_messages=False,read_messages =                        False,read_message_history=False)
         await channel.set_permissions(discord.utils.get(message.author.guild.roles, id = ("Staff") ),send_messages=True,read_messages =                          True,read_message_history=True)
```
In diesem Skript werdet ihr einmal "Member" und "Staff" sehen
Member oder Staff müsst ihr durch die jeweiligen Rollen austauschen, Member für die Rollen der Normalen Benutzer(Die haben kein Zugriff auf den Kanal" und Staff für die Rollen vom Team(Haben vollen Zugriff auf den Kanal).
Die Berechtigungen könnt ibr aber auch anpassen, den Block mit den Rechten müsst ihr für jede Rolle anpasssen.
"ID from your Welcome Channel"


### Hosting
Damit dein Bot immer funktioniert, musst du deinen Bot irgendwo hosten, du kannst es z.B über deinen Computer macehn, der muss dann aber dauerhaft an 
sein, damit der Bot immer läuft.
Du kannst zum Hosten von deinem Bot einen Raspberry Pi 4 Hosten (https://www.raspberrypi.com/products/raspberry-pi-4-model-b/?variant=raspberry-pi-4-model-b-4gb), am besten ist der mit 4GB Ram dafür,dazu empfehle ich dir ein Gehäuse mit Lüfter!
Der Pi verbraucht sehr wenig Strom, darauf muust du nur die Discord Python Libary installieren und das Skript starten. Damit der Remotezugriff
funktioniert, musst du VNC-Server in den Einstellungen Aktivieren (Einstellungen>Raspberry-Pi_Konfiguration>Schnittstellen>VNC), dann in der Raspberry Pi Konfiguration(Terminal>"sudo raspi-config">Display Options>VNC Resoulution>1920x1080)





