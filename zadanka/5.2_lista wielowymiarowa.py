# Stwórz listę A, w której znajdują się dwie listy: w pierwszej umieść integery: 1 i 2, w drugiej 3 i 4.
# Zmodyfikuj listę A tak, aby w zagnieżdżonej liście zamiast integera 3 był string 'trzy'.
# Wydrukuj listę A.


A = [[1, 2], [3, 4]]

A[1][0] = "trzy"

print(A)