x = "myszydokazujągdykotanieczują"


slownik = {}


for litera in x:
    if litera not in slownik.keys():
        slownik[litera] = 1
    else:
        slownik[litera] += 1


print(slownik)


