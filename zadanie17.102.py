"""
Zadanie z generatorem yield
Wygeneruj 20 liczb ktore sa wynikiem przemnozenia przez siebie,
przerwij dzialanie funkcji, a pozneij kontynuuj i wyswietl 30 kolejnych liczb
"""

def generate_multipled_numbers():
    x = 0
    while True:
        x += 1
        number = x ** 2
        yield number

a = generate_multipled_numbers()
generated_numbers = []

for _ in range(20):
    generated_numbers.append(next(a))
print(generated_numbers)

for _ in range(30):
    generated_numbers.append(next(a))
print(generated_numbers)