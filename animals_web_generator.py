import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


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
        erster_ort = locations[0]
        output += f'<li class="card__detail-item"><strong>Location:</strong> {erster_ort}</li>'

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
    """Shows information about animal (animals_data) from JSON file."""
    output = ''
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)
    return output


def load_html(file_path):
    """ Loads a HTML file """
    with open(file_path, "r") as fileobj:
        html_data = fileobj.read()
    return html_data


def replace_template_placeholders(html_template, animal_information):
    """Replaces placeholder in HTML Template with animal_information from JSON."""
    new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animal_information)
    return new_html


def write_new_html(file_path, new_html):
    """New file from HTML-template plus animal_information."""
    with open(file_path, "w") as fileobj:
        fileobj.write(new_html)


def main():
    animals_data = load_data('animals_data.json')
    animal_information = get_animal_information(animals_data)
    html_template = load_html('animals_template.html')
    new_html = replace_template_placeholders(html_template, animal_information)
    write_new_html('animals.html', new_html)


if __name__ == '__main__':
    main()

