A = [1, 2, 3, 3, 1, 2, 2, 3]


B = []


for element in A:
    if element not in B:
        B.append(element)
print(B)

C = list(set(A))

print(C)


