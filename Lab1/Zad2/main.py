import os

def list_files_recursive(directory):
    try:
        for entry in os.listdir(directory):
            path = os.path.join(directory, entry)
            if os.path.isfile(path):
                print(path)
            elif os.path.isdir(path):
                list_files_recursive(path)
    except PermissionError:
        print(f"Brak dostępu do katalogu: {directory}")
    except FileNotFoundError:
        print(f"Katalog {directory} nie istnieje.")

if __name__ == "__main__":
    directory = "C:\\Program Files\\Microsoft" # Podaj ścieżkę do katalogu
    list_files_recursive(directory)