import requests

# die beiden nachfolgenden Importe verstecken den API-Key, damit er nicht auf GitHub landet
import os
from dotenv import load_dotenv


load_dotenv() # Lädt die Variablen aus der .env-Datei in die Umgebung
API_KEY = os.getenv("API_KEY") # Liest die Variable aus

URL = "https://api.api-ninjas.com/v1/animals"


def get_animal_data(animal):
    """Gets data from an animal from API Ninja."""
    my_params = {"name": animal} # 1. Parameter als Dictionary definieren
    my_headers = {"X-Api-Key": API_KEY} # 2. Header für den API-Key definieren
    response = requests.get(URL, params=my_params, headers=my_headers) # 3. Die Anfrage abschicken

    # Check: ist alles gut gelaufen? Sonst: Fehler anzeigen und leere Liste zurück.
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Status Code = {response.status_code}")
        data = []
        return data


def print_animal_data(data):
    """Prints data from an animal from API Ninja."""
    for item in data:
        print("Name:", item["name"])
        print("Locations:", item["locations"])
        print("Characteristics:", item["characteristics"])
        print()


def main():
    animal_data = get_animal_data("giraffe")

    # Check: Sind Daten gekommen? Nur dann werden sie im else-Zweig verarbeitet.
    if not animal_data:
        print("No data found!")
    else:
        print_animal_data(animal_data)
        print(f"\n>>> {len(animal_data)} animal(s) found <<<\n")


if __name__ == "__main__":
    main()
