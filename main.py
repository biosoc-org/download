import requests
from bs4 import BeautifulSoup

# 1. Przygotowanie zmiennych SITE_URL i ELEMENT_ID
SITE_URL = 'https://example.com'  # Zastąp to prawidłowym URLEm
ELEMENT_ID = 'content'  # Zastąp to prawidłowym ID elementu

# 2. Stworzenie tablicy z 3 elementami: GROUP, URL, DESCRIPTION
data = []

# 3. Pobranie zawartości strony www ze zmiennej SITE_URL
response = requests.get(SITE_URL)

# Sprawdzenie czy strona została poprawnie pobrana
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # 4. Zapisanie napotkanego linku i jego opisu z tagów <a> wewnątrz ELEMENT_ID
    element = soup.find(id=ELEMENT_ID)
    if element:
        current_group = None

        for child in element.descendants:
            if child.name == 'h2':
                # 5. Pobranie nazwy zmiennej GROUP z tagu <h2>
                current_group = child.get_text()

            if child.name == 'a':
                # Zapisanie napotkanego linku i jego opisu
                url = child.get('href')
                description = child.get_text()
                if url and current_group:
                    # 6. Zapisanie zmiennych GROUP, URL, DESCRIPTION do tablicy
                    data.append((current_group, url, description))
else:
    print(f"Error: Unable to fetch the site. Status code: {response.status_code}")

# Wyświetlenie zapisanych danych
for group, url, description in data:
    print(f"Group: {group}, URL: {url}, Description: {description}")
