def replace_words_in_text(text, replacements):
    # Tworzymy listę słów z tekstu wejściowego
    words = text.split()
    # Zamieniamy słowa zgodnie z podanym słownikiem
    replaced_words = [replacements.get(word, word) for word in words]
    # Łączymy słowa w nowy tekst
    return " ".join(replaced_words)

if __name__ == "__main__":
    # Przykładowy tekst wejściowy (można załadować z pliku)
    text = "To jest przykładowy tekst, który należy zmienić."
    # Słownik z zamiennikami słów
    replacements = {
        "jest": "to",
        "przykładowy": "testowy",
        "który": "jaki"
    }
    # Zamiana słów w tekście
    result = replace_words_in_text(text, replacements)
    print("Tekst po zamianie słów:")
    print(result)
