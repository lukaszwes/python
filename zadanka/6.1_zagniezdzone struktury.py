# Pytanie 5 - z poniższej listy wypisz stringa "schowany"

L = [[34, False], [0], [('abc', 123), {'a': 1, 'x': (True, 'schowany', 5)}]]

szukany_tekst = L[2][1]["x"][1]

print(szukany_tekst)