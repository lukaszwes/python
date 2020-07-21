#napisz finkcje sprawdzajaca, czy dane zlowo jest palindromem
#przetestuj na przykladzie slow "kajak" oraz "anakonda"

# def if_palindrom(word: str):
#     if word == word[::-1]:
#         print(f"Slowo {word} jest palindromem")
#     else:
#         print(f"Slowo {word} nie jest palindromem")

def if_palindrom(slowo):
    poczatek = 0                              # stwórz indeks poczatkowy równy 0
    koniec = len(slowo) - 1                   # stwórz indeks końcowy równy długości stringa zmniejszonej o 1
    while poczatek < koniec:                 # wykonuj pętlę dopóki indeks poczatkowy jest mniejszy lub równy indeksowi końcowemu
        if slowo[poczatek] != slowo[koniec]:  # jeśli wartosc zmiennej slowo od indeksu początkowego jest różna od wartości od indeksu końcowego
            return False                      # zwróć False
        else:                                 # w przeciwnym wypadku
            poczatek += 1                     # zwiększ indeks początkowy o 1
            koniec -= 1                       # zmniejsz indeks końcowy o 1
    return True                               # jeśli funkcja dotarła do tego miejsca, to znaczy że słowo jest palindromem i funkcja zwraca True


print(if_palindrom("kajak"))
print(if_palindrom("anakonda"))