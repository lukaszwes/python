#Napisz generator x, który zwróci 10 kolejnych wielokrotności liczby 5 - zaczynając od 5, kończąc na 50 (włącznie).
#Następnie napisz pętlę for, która wypisze kolejne wartości zwracane przez generator (i nie spowoduje wypisania StopIteration Error).

# Twój kod tutaj.


def x():
    for num in range(5, 51 ,5):
        yield num

z = x()


for _ in range(10):
    print(next(z))


# OR

# try:
#     while True:
#         print(next(z))
# except StopIteration:
#     pass
