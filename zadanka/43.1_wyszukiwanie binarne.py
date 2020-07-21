# Pytanie 42 - przy użyciu wyszukiwania binarnego sprawdź
# czy liczba 341 znajduje się w posortowanej liście P

P = [-10, -7, -5, -3, 0, 3, 5, 21, 68, 341, 500]


def find_number_in_list(x, A):
    left = 0
    right = len(A) - 1

    while left <= right:
        center = (right + left) // 2
        if A[center] == x:
            print(f"Numbert {x} is in the list.")
            break
        elif A[center] < x:
            left = center + 1
        else:
            right = center - 1
    else:
        print(f"Numbert {x} is NOT in the list.")


find_number_in_list(341, P)
