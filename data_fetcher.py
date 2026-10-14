import requests
import sys

# die beiden nachfolgenden Importe verstecken den API-Key, damit er nicht auf GitHub landet
import os
from dotenv import load_dotenv


load_dotenv() # Lädt die Variablen aus der .env-Datei in die Umgebung
API_KEY = os.getenv("API_KEY") # Liest die Variable aus
URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
    },
    """
    # Prüfen, ob API-Key in .env-Datei
    if not API_KEY:
        print("Error: API_KEY is missing. Please check your .env file.")
        sys.exit(1)  # Stoppt das Programm mit Fehlercode 1

    my_params = {"name": animal}  # 1. Parameter als Dictionary definieren
    my_headers = {"X-Api-Key": API_KEY} # 2. Header für den API-Key definieren

    # Netzwerkanfrage wird versucht. Falls es nicht klappt (no Internet) -> Fehler ausgeben
    try:
        response = requests.get(URL, params=my_params, headers=my_headers) # 3. Die Anfrage abschicken
    except requests.exceptions.RequestException as error:
        print(f"Netzwerkfehler: {error}")
        return []

    # Check: ist alles gut gelaufen? Sonst: Fehler anzeigen und leere Liste zurück.
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Server Error: Status Code = {response.status_code}")
        return []
