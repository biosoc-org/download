1. Stwórz skrypt o nazwie geturl.py, który pobiera w argumentach konsoli: nazwę pliku csv z argumentu: INPUT oraz nazwę strony www z argumentu: URL i argument: COL
2. Pobierz plik csv ze zmiennej INPUT i zapisz go do tablicy, pierwszy wiersz to nazwy kolumn, zapisz je dynamicznie jako klucze wartości z kolejnych wierszy
3. Pobieraj z pętli kolejne wiersze tablicy i z kolumny o nazwie takiej jak zawartość zmiennej COL zapisz wartość do zmiennej PREFIX
4. Za każdym razem przy zapisywaniu zmiennej PREFIX dodaj jej zawartość do zmiennej URL i zapisz do zmiennej URL_PREFIX
5. Zapisz zmienną URL_PREFIX do tablicy i wyświetl w shellu
6. Pobierz zawartość strony URL_PREFIX, jeśli Zostanie wykryte przekierowanie pobierz URL docelowej strony i zapisz do URL_PREFIX
7. Gdy strona zostanie pobrana do folderu HTML zapisz do tablicy zmieną URL_PREFIX, nazwę strony jako zmienną NAME opis jako DESCRIPTION i meta dane jako META 
8. Zapisz pobraną stronę  do folderu o nazwie argumentu HTML podanego przy wykonywaniu skryptu 
9. Zapisz tablicę do pliku CSV o nazwie podanej w argumencie OUTPUT przy wykonywaniu skryptu



Aby uruchomić skrypt, musisz użyć następującej komendy w terminalu/shellu:

```sh
python geturl.py output.csv https://www.click2drug.org/ URL html html.csv
```
- `input.csv` to nazwa pliku CSV z danymi wejściowymi.
- `http://example.com/` to bazowy URL.
- `columnName` to nazwa kolumny w pliku CSV, której wartości będą używane do budowy URL.
- `html_folder` to folder, w którym będą zapisywane pobrane pliki HTML.
- `output.csv` to nazwa pliku wyjściowego, w którym będą zapisane wyniki.


```sh
python geturl.py output2.csv https://www.click2drug.org/ URL html html.csv
```
```sh
python geturl.py output3.csv https://www.click2drug.org/ URL html html.csv
```
```sh
python geturl.py output4.csv https://www.click2drug.org/ URL html html.csv
```
```sh
python geturl.py output5.csv https://www.click2drug.org/ URL html html.csv
```
```sh
python geturl.py output6.csv https://www.click2drug.org/ URL html html.csv
```
```sh
python geturl.py output7.csv https://www.click2drug.org/ URL html html.csv
```
```sh
python geturl.py output8.csv https://www.click2drug.org/ URL html html.csv
```
```sh
python geturl.py output9.csv https://www.click2drug.org/ URL html html.csv
```
```sh
python geturl.py output10.csv https://www.click2drug.org/ URL html html.csv
```
```sh
python geturl.py output11.csv https://www.click2drug.org/ URL html html.csv
```
```sh
python geturl.py output12.csv https://www.click2drug.org/ URL html html.csv
```

### Opis działań skryptu:

1. **Sprawdzanie liczby argumentów**:
   Skrypt oczekuje dokładnie pięciu argumentów: `INPUT`, `URL`, `COL`, `HTML` (folder dla plików HTML) oraz `OUTPUT` (plik wynikowy CSV).

2. **Tworzenie folderu dla plików HTML**:
   Sprawdzane jest, czy podany folder istnieje. Jeśli nie, tworzony jest nowy folder o podanej nazwie.

3. **Pobieranie zawartości URL i obsługa przekierowań**:
    - Skrypt pobiera zawartość URL. Jeśli wykryte zostanie przekierowanie, zapyana jest docelowa URL.
    - Zawartość strony jest następnie zapisana do pliku HTML w określonym folderze.

4. **Ekstrakcja informacji ze strony**:
    - Tytuł strony (`NAME`) jest pobierany z tagu `<title>`.
    - Opis strony (`DESCRIPTION`) jest pobierany z meta tagu `<meta name="description">`.
    - Wszystkie meta tagi są zapisywane w słowniku `meta_data`.

5. **Zapisywanie wyników do tablicy**:
    - Do tablicy `results` dodawane są słowniki zawierające URL, nazwę, opis i meta dane.

6. **Zapis do pliku CSV**:
    - Tablica `results` jest zapisywana do pliku CSV podanego w argumencie `OUTPUT`.

7. **Obsługa błędów**:
   Skrypt obsługuje zarówno wyjątki związane z brakiem pliku CSV, jak i błędy HTTP.






Upewnij się, że masz zainstalowane wymagane biblioteki:

```sh
pip install requests beautifulsoup4
```
