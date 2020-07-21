# Naszym zadaniem jest sprawdzić, czy liczba 7430 znajduje się wśród kluczy słownika.

x = 7430

S = {x:x+1 for x in range(10000) if x%23 == 0}

if x in S.keys():
    print("True")
else:
    print("False")


#or

print("True" if x in S.keys() else "False")