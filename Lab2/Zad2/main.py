import multiprocessing
from multiprocessing import Process, Manager

def merge(left, right):
    """Scalanie dwóch posortowanych list."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort_worker(data, result):
    """Worker do sortowania i zapisu wyniku."""
    result.extend(parallel_merge_sort(data))

def parallel_merge_sort(data):
    """Główna funkcja równoległego sortowania."""
    if len(data) <= 1:
        return data
    if len(data) <= 1000:  # Dla małych danych przełącz na zwykłe sortowanie
        return sorted(data)

    mid = len(data) // 2

    # Użycie Manager.List do wymiany wyników między procesami
    with Manager() as manager:
        left_result = manager.list()
        right_result = manager.list()

        left_process = Process(target=merge_sort_worker, args=(data[:mid], left_result))
        right_process = Process(target=merge_sort_worker, args=(data[mid:], right_result))

        # Start i dołączenie procesów
        left_process.start()
        right_process.start()

        left_process.join()
        right_process.join()

        # Scalanie wyników
        return merge(left_result, right_result)

if __name__ == "__main__":
    # Przykładowe dane do sortowania
    import random
    data = [random.randint(0, 10000) for _ in range(10000)]

    print("Sortowanie rozpoczęte...")
    sorted_data = parallel_merge_sort(data)
    print(sorted_data)
    print("Sortowanie zakończone!")
