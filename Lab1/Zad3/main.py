def remove_words_from_text(text, words_to_remove):
    # Tworzymy listę słów z wejściowego tekstu
    words = text.split()
    # Filtrujemy słowa, które nie są na liście do usunięcia
    filtered_words = [word for word in words if word not in words_to_remove]
    # Łączymy przefiltrowane słowa w nowy tekst
    return " ".join(filtered_words)

if __name__ == "__main__":
    # Przykładowy tekst wejściowy (można załadować z pliku)
    text = "To jest przykładowy tekst, który należy przefiltrować."
    # Słowa do usunięcia
    words_to_remove = {"jest", "który"}
    # Usunięcie wybranych słów
    result = remove_words_from_text(text, words_to_remove)
    print("Tekst po przefiltrowaniu:")
    print(result)
