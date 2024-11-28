import os

def count_files(directory):
    try:
        # Pobierz listę wszystkich plików i podkatalogów w katalogu
        entries = os.listdir(directory)
        # Filtruj tylko pliki
        files = [entry for entry in entries if os.path.isfile(os.path.join(directory, entry))]
        return len(files)
    except FileNotFoundError:
        print(f"Katalog {directory} nie istnieje.")
        return 0
    except PermissionError:
        print(f"Brak uprawnień do odczytu katalogu {directory}.")
        return 0

# Testowanie funkcji
if __name__ == "__main__":
    directory = "C:\\Program Files\\Microsoft"  # Możesz podać dowolny katalog
    file_count = count_files(directory)
    print(f"Ilość plików w katalogu '{directory}': {file_count}")