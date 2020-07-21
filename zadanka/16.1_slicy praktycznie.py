# Pytanie 15 - napisz funkcję, która sprawdzi czy podany string
# zaczyna się słowem "python" i kończy rozszerzeniem ".py"
# Przetestuj nią stringi:
a = "python_moj_kod.py"
b = "python_notatki.txt"


def check_if_python(string: str):
    if string[:6] == "python" and string[-3:] == ".py":
        return True
    return False


print(check_if_python(b))