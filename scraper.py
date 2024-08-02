import argparse
import requests
from bs4 import BeautifulSoup
import csv
import os

# Funkcja główna realizująca zadania
def main(site_url, element_id, output_file):
    # Stworzenie tablicy z 4 elementami: GROUP, URL, DESCRIPTION, INFO
    data = []

    # Pobranie zawartości strony www ze zmiennej SITE_URL
    response = requests.get(site_url)

    # Sprawdzenie, czy strona została poprawnie pobrana
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Zapisanie napotkanego linku i jego opisu z tagów <a> wewnątrz ELEMENT_ID
        element = soup.find(id=element_id)
        if element:
            current_group = None

            for child in element.descendants:
                if child.name == 'h2':
                    # Pobranie nazwy zmiennej GROUP z tagu <h2>
                    current_group = child.get_text()

                if child.name == 'a':
                    # Zapisanie napotkanego linku i jego opisu
                    url = child.get('href')
                    description = child.get_text()
                    # Pobranie tekstu za tagiem <a>
                    next_sibling = child.next_sibling
                    info = next_sibling.strip() if next_sibling else ''

                    if url and current_group:
                        # Zapisanie zmiennych GROUP, URL, DESCRIPTION, INFO do tablicy
                        data.append((current_group, url, description, info))
        else:
            print(f"Error: Element with ID '{element_id}' not found on the page.")
    else:
        print(f"Error: Unable to fetch the site. Status code: {response.status_code}")

    # Zapisanie danych do pliku CSV
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Group', 'URL', 'Description', 'Info'])
        writer.writerows(data)

    print(f"Data successfully saved to {output_file}")

if __name__ == "__main__":
    # Konfiguracja argumentów z linii poleceń
    parser = argparse.ArgumentParser(description="Web scraper for a specific site and element.")
    parser.add_argument('SITE_URL', type=str, help='URL of the site to scrape')
    parser.add_argument('ELEMENT_ID', type=str, help='ID of the element within the site')
    parser.add_argument('--output_file', type=str, default='output.csv',
                        help='Optional output CSV file path (default: output.csv)')

    args = parser.parse_args()

    # Ustawienie domyślnej ścieżki do pliku, jeśli argument output_file nie został podany
    output_file_path = args.output_file if args.output_file else os.path.join(os.getcwd(), 'output.csv')

    # Uruchomienie funkcji głównej z przekazanymi argumentami
    main(args.SITE_URL, args.ELEMENT_ID, output_file_path)