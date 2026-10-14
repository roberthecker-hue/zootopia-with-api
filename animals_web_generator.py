import data_fetcher


def serialize_animal(animal_obj):
    """Serialize an animal object to HTML string."""
    output = ''
    output += '<li class="cards__item">'

    # Name zuordnen und ausgeben
    name = animal_obj.get('name')
    if name:
        output += f'<div class="card__title">{name}</div>'

    output += '<div class="card__text">'
    output += '<ul class="card__details">'

    # Sind Characteristics vorhanden? Dann Diet zuordnen und ausgeben
    characteristics = animal_obj.get('characteristics')
    if characteristics:
        diet = characteristics.get('diet')
        if diet:
            output += f'<li class="card__detail-item"><strong>Diet:</strong> {diet}</li>'

    # Sind Locations vorhanden und die Liste nicht None UND nicht eine leere Liste []?
    # Dann ersten Ort aus Locations zuordnen und ausgeben
    locations = animal_obj.get('locations')
    if locations:
        orte_text = ", ".join(locations)  # Zusammenfügen, falls es mehr als eine Location gibt
        if len(locations) > 1:
            label = "Locations"
        else:
            label = "Location"
        output += f'<li class="card__detail-item"><strong>{label}:</strong> {orte_text}</li>'

    # Sind Characteristics vorhanden? Dann Type zuordnen und ausgeben
    if characteristics:
        type_info = characteristics.get('type')
        if type_info:
            output += f'<li class="card__detail-item"><strong>Type:</strong> {type_info}</li>'

    output += '</ul>'
    output += '</div>'
    output += '</li>'
    return output


def get_animal_information(animals_data):
    """Shows information about animal (animals_data)."""
    output = ''
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)
    return output


def load_html(file_path):
    """ Loads a HTML file """
    with open(file_path, "r", encoding="utf-8") as fileobj:
        html_data = fileobj.read()
    return html_data


def replace_template_placeholders(html_template, animal_information):
    """Replaces placeholder in HTML Template with animal_information from JSON."""
    new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animal_information)
    return new_html


def write_new_html(file_path, new_html):
    """New file from HTML-template plus animal_information."""
    with open(file_path, "w", encoding="utf-8") as fileobj:
        fileobj.write(new_html)


def ask_user_animal_name():
    """Asks user to enter animal name."""
    animal_name = input("Enter a name of an animal: ")
    return animal_name.strip()


def main():
    animal_name = ask_user_animal_name()
    animals_data = data_fetcher.fetch_data(animal_name)  # Daten von API holen

    # Guard Clause, falls leere Liste zurückkommt
    if not animals_data:
        animal_information = f'<h2>Das Tier "{animal_name}" existiert nicht.</h2>'
        print("Animal does not exist. Fallback-Website was generated to the file animals.html.")
    else:
        animal_information = get_animal_information(animals_data)
        print("Website was successfully generated to the file animals.html.")

    html_template = load_html('animals_template.html')
    new_html = replace_template_placeholders(html_template, animal_information)
    write_new_html('animals.html', new_html)


if __name__ == '__main__':
    main()
