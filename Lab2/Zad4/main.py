class FibonacciIterator:
    def __init__(self, steps):
        
        self.steps = steps
        self.current_step = 0
        self.a = 0  # Pierwszy wyraz ciągu
        self.b = 1  # Drugi wyraz ciągu

    def __iter__(self):

        return self

    def __next__(self):

        if self.current_step >= self.steps:
            raise StopIteration
        
        # Obliczanie następnego wyrazu
        if self.current_step == 0:
            result = self.a
        elif self.current_step == 1:
            result = self.b
        else:
            result = self.a + self.b
            self.a, self.b = self.b, result

        self.current_step += 1
        return result

# Przykład użycia
if __name__ == "__main__":
    fib = FibonacciIterator(steps=12)  
    for num in fib:
        print(f"{fib.current_step}: {num}")