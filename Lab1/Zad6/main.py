import random

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

if __name__ == "__main__":
    # Generowanie N losowych liczb
    N = 20  # Możesz zmienić liczbę losowych elementów
    random_numbers = [random.randint(0, 100) for _ in range(N)]
    
    print("Liczby przed sortowaniem:", random_numbers)

    # Sortowanie metodą Bubble Sort
    bubble_sorted = bubble_sort(random_numbers.copy())
    print("Bubble Sort:", bubble_sorted)

    # Sortowanie metodą Merge Sort
    merge_sorted = merge_sort(random_numbers.copy())
    print("Merge Sort:", merge_sorted)

    # Weryfikacja przy pomocy wbudowanej funkcji sortującej
    python_sorted = sorted(random_numbers)
    print("Wbudowana metoda sortowania:", python_sorted)

    # Sprawdzenie, czy wyniki są zgodne
    print("Czy wyniki Bubble Sort są poprawne?", bubble_sorted == python_sorted)
    print("Czy wyniki Merge Sort są poprawne?", merge_sorted == python_sorted)
