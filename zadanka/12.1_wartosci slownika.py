jezyki = ["Java", "Python", "C#", "Ruby"]

#1
revers = []

for index, _ in enumerate(jezyki):
    revers.append(jezyki[(index+1) * (-1)])

print(revers)


#2

# jezyki.reverse()          #reverse zmienia na stale liste jezyki
# print(jezyki)


#3

reverse1 = jezyki.__reversed__()

print(list(reverse1))

#4

print(jezyki[::-1])

#5

revers2 = []

for jezyk in jezyki:
    revers2.insert(0, jezyk)
print(revers2)

