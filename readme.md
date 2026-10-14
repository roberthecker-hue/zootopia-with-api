# ZOO-Anwendungs-Generator (Animals Web Generator)

Ein Python-basiertes CLI-Tool, das Tierdaten dynamisch über die **API Ninjas Animals API** abruft und daraus eine strukturierte HTML-Webseite (`animals.html`) erzeugt.

## 🌟 Features

* **Dynamischer Datenabruf:** Ruft Echtzeit-Informationen zu Tieren (Ernährung, Standorte, Typ, etc.) von einer externen API ab.
* **Dynamische HTML-Generierung:** Verarbeitet die JSON-Daten und fügt sie sauber in ein wiederverwendbares HTML-Template ein.
* **Robuste Fehlerbehandlung & Fallback:** Wenn ein eingegebenes Tier nicht existiert oder der API-Schlüssel fehlt, wird eine verständliche Rückmeldung geliefert bzw. eine Fehlerseite gerendert.
* **Mehrdatei-Architektur:** Trennung von Datenbeschaffung (`data_fetcher.py`) und Benutzeroberfläche/HTML-Generierung (`animals_web_generator.py`).
* **Sicheres API-Management:** Geheimhaltung sensibler Zugangsdaten mittels `.env`-Datei und `.gitignore`.

## 🛠️ Voraussetzungen

* Python 3.8 oder neuer
* Ein kostenloser API-Schlüssel von [API Ninjas (Animals API)](https://api-ninjas.com/api/animals)

## 🚀 Installation & Setup

1. **Repository klonen:**

   ```bash
   git clone https://github.com/roberthecker-hue/zootopia-with-api.git
   cd zootopia-with-api
   ```

2. **Abhängigkeiten installieren:**
   Installiere alle benötigten Bibliotheken mit `pip`:

   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Konfiguration

1. Erstelle eine neue Datei namens `.env` im Hauptverzeichnis deines Projekts.
2. Trage deinen API-Schlüssel von API Ninjas folgendermaßen ein (ohne Leerzeichen um das `=`):

   ```env
   API_KEY=dein_persoenlicher_api_schluessel_hier
   ```

> ⚠️ **Hinweis:** Die `.env`-Datei ist in der `.gitignore` eingetragen und wird **nicht** auf GitHub hochgeladen, um deinen Schlüssel zu schützen.

## 💻 Nutzung

1. Starte das Hauptprogramm im Terminal:

   ```bash
   python animals_web_generator.py
   ```

2. Gib den Namen eines Tieres auf Englisch ein (z. B. `Fox`, `Elephant`, `Dog`).
3. Das Programm ruft die Daten ab und erzeugt oder aktualisiert die Datei `animals.html`.
4. Öffne die generierte `animals.html` in deinem Browser, um das Ergebnis zu sehen.

## 📂 Projektstruktur

```text
├── animals_web_generator.py # Hauptskript für Benutzereingabe & HTML-Generierung
├── data_fetcher.py          # Modul zum Abrufen & Absichern der API-Daten
├── animals_template.html    # HTML-Vorlage mit Platzhalter __REPLACE_ANIMALS_INFO__
├── animals.html             # Die final generierte Web-Datei (Ausgabe)
├── requirements.txt         # Auflistung der externen Python-Pakete
├── .gitignore               # Schließt sensible Dateien (.env) von Git aus
└── README.md                # Dokumentation des Projekts
```