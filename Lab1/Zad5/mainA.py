import re

def remove_words_with_regex(text, words_to_remove):
    # Tworzymy wzorzec wyrażeń regularnych dla słów do usunięcia
    pattern = r'\b(' + '|'.join(re.escape(word) for word in words_to_remove) + r')\b'
    # Usuwamy dopasowane słowa
    return re.sub(pattern, '', text).strip()

if __name__ == "__main__":
    # Przykładowy tekst wejściowy
    text = "To jest przykładowy tekst, który należy przefiltrować."
    # Słowa do usunięcia
    words_to_remove = {"jest", "który"}
    # Usunięcie wybranych słów
    result = remove_words_with_regex(text, words_to_remove)
    print("Tekst po przefiltrowaniu:")
    print(result)