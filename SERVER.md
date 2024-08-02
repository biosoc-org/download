Aby utworzyć serwer Python za pomocą biblioteki `Flask`, który pobierze plik z folderu "html" na podstawie URL zapytania, możesz postępować zgodnie z poniższymi krokami. `Flask` jest lekką biblioteką, która umożliwia łatwe budowanie serwerów HTTP i obsługę zapytań.

### Instalacja Flask
Najpierw zainstaluj Flask, jeśli jeszcze go nie masz:

```sh
pip install Flask
```

### Uruchomienie serwera

Aby uruchomić serwer, w terminalu przejdź do folderu zawierającego `server.py` i uruchom:

```sh
python server.py
```


### Jak działa serwer Flask

**Endpoint obsługujący nasze zapytanie**:
Definiowany jest endpoint `/html/redirection-new.php`, który akceptuje jedynie żądania typu GET.

**Pobranie i weryfikacja parametrów**:
Pobierane są parametry URL (`URL`) oraz NAME (`NAME`) z zapytania. Jeśli któryś z parametrów nie zostanie podany, zwracany jest błąd 400 (bad request).

**Konstrukcja ścieżki pliku**:
Generowana jest ścieżka do pliku w folderze `html` na podstawie podanych parametrów.

**Wysyłanie pliku do klienta**:
Jeśli plik istnieje, zostanie wysłany do klienta. W przeciwnym razie zwracany jest błąd 404 (file not found).

**Uruchomienie serwera**:
Serwer uruchamia się na porcie 5000, dostępny z dowolnego hosta (`0.0.0.0`).


### Przykładowe zapytanie

Gdy serwer jest uruchomiony, możesz wysłać zapytanie HTTP do serwera w poniżej opisany sposób, np. za pomocą przeglądarki lub narzędzia `curl`:

#### W przeglądarce
Przejdź do:

```
http://localhost:5000/html/redirection-new.php?URL=465031495f5333cb7fa195df4c1e39ea1d8c38fd1f271a032879d044b479e18c&NAME=Zinc15Database.html
```

#### Używając `curl`:

```sh
curl "http://localhost:5000/html/redirection-new.php?URL=465031495f5333cb7fa195df4c1e39ea1d8c38fd1f271a032879d044b479e18c&NAME=Zinc15Database.html"
```

Jeśli plik istnieje w katalogu `html` z odpowiednią nazwą, zostanie on pobrany. W przeciwnym razie otrzymasz odpowiedni komunikat o błędzie.