import re

def replace_words_with_regex(text, replacements):
    # Tworzymy funkcję pomocniczą dla re.sub, która zastępuje słowa
    def replace_match(match):
        return replacements.get(match.group(0), match.group(0))
    
    # Tworzymy wzorzec dopasowujący wszystkie słowa do zamiany
    pattern = r'\b(' + '|'.join(re.escape(word) for word in replacements.keys()) + r')\b'
    # Zamieniamy dopasowane słowa
    return re.sub(pattern, replace_match, text)

if __name__ == "__main__":
    # Przykładowy tekst wejściowy
    text = "To jest przykładowy tekst, który należy zmienić."
    # Słownik z zamiennikami słów
    replacements = {
        "jest": "to",
        "przykładowy": "testowy",
        "który": "jaki"
    }
    # Zamiana słów w tekście
    result = replace_words_with_regex(text, replacements)
    print("Tekst po zamianie słów:")
    print(result)
