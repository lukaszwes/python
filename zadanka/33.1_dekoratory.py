#napisz dekorator dodajacy przed i po funkcji f znak 3 gwiazdek "***"

def add_stars(funkcja):
    def decorator():
        print("***")
        funkcja()
        print("***")
    return decorator

@add_stars
def funkcja():
    print("Hello world!")



funkcja()