# [download](http://download.biosoc.org)

1. Przygotuj zmienne: SITE_URL, ELEMENT_ID, OUTPUT_FILE, Parametry SITE_URL i ELEMENT_ID powinny być podawane jako argumenty podczas uruchamiania z lini poleceń
2. Stwórz tablicę z 3 elementami: GROUP,URL,DESCRIPTION,INFO
3. Pobierz zawartość strony www ze zmiennej SITE_URL
4. Zapisz napotkany link do zmiennej URL z tagu <a> i jego opis do zmiennej DESCRIPTION podczas przeszukiwania drzewa DOM na podstawie obszaru wskazanego przez elementu ELEMENT_ID drzewa DOM pobranej strony www
5. Dodadtkowo podczas pobierania każdego tagu <a> pobierz tekst znajdujący się za tym tagiem i zapisz go do zmiennej INFO w tablicy
5. Pobierz nazwę zmiennej GROUP <h2> podczas pobierania linków i aktualizuj go za każdym razem gdy napotkasz tag <h2> 
6. Za każdym razem gdy znajdziej tag <a> zapisz do tablicy 3 zmienne:  GROUP,URL,DESCRIPTION 
7. Zapisz tablicę do wskazanego w zmiennej pliku OUTPUT_FILE
8. Uruchom skrypt z linii poleceń, przekazując odpowiednie argumenty do zmiennych: SITE_URL, ELEMENT_ID, OUTPUT_FILE,
9. Wygeneruj html i javascript pobierający plik output.csv i pokazujący go jako tabelę z wyrenderowanymi klikalnymi linkami tam gdzie jest url


2. **Uruchom skrypt z linii poleceń, przekazując odpowiednie argumenty**:

   ```bash
   python scraper.py https://www.click2drug.org/ Cats1 --output_file output.csv
   ```




Aby zrealizować żądanie, możemy zmodyfikować funkcję `createTable` tak, aby automatycznie skracała ciągi znaków bez spacji, które są dłuższe niż 20 znaków, dodając na końcu trzy kropki ("..."). Oto pełny przykład, uwzględniający te zmiany:


Wprowadzone zmiany:

1. Dodano funkcję `truncateLongText`, która skraca ciągi znaków bez spacji dłuższe niż 20 znaków i dodaje "..." na końcu.
2. W funkcji `createTable` użyto funkcji `truncateLongText` do przetworzenia wartości komórki przed jej wyświetleniem, z wyjątkiem przypadków, w których komórka zawiera URL.

Cały kod powinien spełniać założenia: pobierać plik CSV, generować tabelę HTML oraz skracać zbyt długie ciągi znaków.





Zaktualizujmy skrypt, aby dodatkowo pobierał tekst znajdujący się za każdym tagiem `<a>` i zapisywał go do zmiennej `INFO`, a następnie zapisywał te informacje do tablicy.


### Elementy nowo dodane do skryptu:

1. **Zmiana struktury danych**:
   - Tablica `data` teraz przechowuje cztery elementy: `GROUP`, `URL`, `DESCRIPTION`, `INFO`.

2. **Zbieranie informacji**:
   - Pobieranie tekstu znajdującego się za tagiem `<a>`: `next_sibling` jest pobierany, a jego zawartość jest trimowana za pomocą `strip()`, aby usunąć niepotrzebne białe znaki.
   - Jeśli `next_sibling` istnieje, jego zawartość jest przypisywana do zmiennej `INFO`.

3. **Zapis danych do CSV**:
   - Dodatkowa kolumna `INFO` w pliku CSV.



### Dodatkowe wyjaśnienia:

- **.next_sibling**:
   - `.next_sibling` zwraca następny logiczny węzeł w drzewie DOM. Jeśli tekst znajduje się natychmiast po tagu `<a>`, zostanie on zwrócony.
   - W przypadku, gdy następny węzeł to inny element (np. tag HTML), `.next_sibling` może zwrócić błąd. W bardziej skomplikowanych scenariuszach struktury HTML może być konieczne użycie bardziej zaawansowanych metod nawigacji po drzewie DOM.


### Wyjaśnienie zmian:

1. **Argumenty z linii poleceń**:
   - Dodany został opcjonalny argument `--output_file`, który pozwala użytkownikowi określić nazwę i ścieżkę do pliku CSV.
   - Domyślna wartość ustawiona na `output.csv`.

2. **Funkcja do zapisu pliku**:
   - Dodano import modułu `csv`.
   - Sekcja zapisująca dane do pliku CSV za pomocą `csv.writer`.

3. **Domyślna ścieżka pliku**:
   - Sprawdzenie, czy argument `output_file` jest podany, i ustawienie domyślnej ścieżki jako `output.csv` w bieżącym katalogu, jeśli brak argumentu.

skrapowania danych, wygodnego zapisu do pliku CSV, co pozwala na dalszą analizę lub przetwarzanie danych w późniejszym czasie.


parametry `SITE_URL` i `ELEMENT_ID` jako argumenty z linii poleceń. W tym celu użyjemy modułu `argparse`, który jest standardowym narzędziem do obsługi argumentów wiersza poleceń w Pythonie.


Wykorzystuje on bibliotekę `requests` do pobrania strony internetowej i `BeautifulSoup` z biblioteki `bs4` do analizy drzewa DOM.


### Opis działania skryptu:
1. **Przygotowanie zmiennych SITE_URL i ELEMENT_ID**:
    - `SITE_URL`: URL strony, którą chcesz pobrać.
    - `ELEMENT_ID`: ID elementu HTML, którego zawartość ma być przeszukana.

2. **Stworzenie tablicy `data`**: Przechowuje tuple zawierające wartości dla `GROUP`, `URL`, `DESCRIPTION`.

3. **Pobranie zawartości strony**: Użycie biblioteki `requests` do pobrania strony.

4. **Parsowanie drzewa DOM**: Użycie `BeautifulSoup` do przetwarzania HTML strony.

5. **Wyszukiwanie elementów**:
    - Zidentyfikowanie sekcji przez ID elementu.
    - Przeszukiwanie drzewa DOM tej sekcji.
    - Aktualizacja zmiennej `current_group` przy każdym napotkanym tagu `<h2>`.
    - Przy napotkaniu tagu `<a>`, aktualizacja tablicy `data` o wartości `GROUP`, `URL`, `DESCRIPTION`.

6. **Wyświetlenie zebranych danych**: Każda pozycja w tablicy `data` jest drukowana.