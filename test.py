"""
baza = {
    ("Lukasz", "Wesolowski", 30),
    ("Kinga", "Porzyczka", 24)
}


for name, surname, age in baza:
    print(name)
"""

slownik = {
    "Lukasz" : 30,
    "Kinga"  : 24
}

print(slownik)

slownik.update({"Marta" : 27})

print(slownik)
