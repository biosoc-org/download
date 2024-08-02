### Jak utworzyć i używać pliku `requirements.txt`:

1. **Stwórz plik `requirements.txt` w katalogu projektu**:

   ```bash
   echo "beautifulsoup4==4.10.0" > requirements.txt
   echo "requests==2.26.0" >> requirements.txt
   ```

2. **Instalacja zależności z pliku `requirements.txt`**:

   Użyj poniższego polecenia, aby zainstalować wymagane biblioteki w środowisku wirtualnym.
   ```bash
   pip install -r requirements.txt
   ```

### Pełny proces utworzenia i używania pliku `requirements.txt`:

1. **Instalacja bibliotek**: Upewnij się, że masz zainstalowane biblioteki:
   ```bash
   pip install beautifulsoup4 requests
   ```

2. **Zamrożenie wersji biblioteki**: Sprawdź zainstalowane wersje i zapisz je do pliku `requirements.txt`:
   ```bash
   pip freeze > requirements.txt
   ```
