
lista = [1, 2, 3, True, ("a", "b")]

tupla = (6, 7, 8, False, ["x", "y"])



lista[1] = "dwa"
print(lista)

# tupla[1] = "siedem"
# print(tupla)


lista.append(4)
tupla = (*tupla, 9)

print(lista)
print(tupla)