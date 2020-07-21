a = "abcdefg"

b = list(a)
b[1] = "X"

a = "".join(b)

print(a)