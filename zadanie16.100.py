import requests
import json
import credentials
import os
import webbrowser
from termcolor import colored
from pprint import pprint

users= ["kinga", "lukasz", "marta", "lukaszwes"]
# user_ID  = "lukaszwes"
x = True
favourites_cats = {}
# favourites_cats = {2024170: 'https://cdn2.thecatapi.com/images/d9s.jpg', 2024171: 'https://cdn2.thecatapi.com/images/bai.jpg'}

def get_user_favourites():
    r = requests.get("https://api.thecatapi.com/v1/favourites", params,
                     headers = credentials.headers)
    content = decode_json(r)
    favourites_cats ={}
    for item in content:
        cat_id  = item["image_id"]
        cat_url = item["image"]["url"]
        favourites_cats.update({cat_id : cat_url})
    return favourites_cats

def find_new_cat():
    r = requests.get("https://api.thecatapi.com/v1/images/search", params,
                     headers=credentials.headers)
    content = decode_json(r)
    new_cat ={}
    for item in content:
        cat_id  = item["id"]
        cat_url = item["url"]
        new_cat.update({cat_id : cat_url})
    return new_cat

def add_user_favourite_cat(cat_id):
    params.update({"image_id" : cat_id})
    requests.post("https://api.thecatapi.com/v1/favourites", json = params,
                     headers = credentials.headers)
    params.pop("image_id")

def delete_user_favourite_cat(cat_id):
    params.update({"image_id": cat_id})
    requests.delete("https://api.thecatapi.com/v1/favourites", json = params,
                     headers = credentials.headers)
    params.pop("image_id")

def check_if_image_exist(cat_id):
    params.update({"image_id": cat_id})
    r = requests.get("https://api.thecatapi.com/v1/images/", params,
                     headers=credentials.headers)
    content = decode_json(r)
    for item in content:
        if item["url"]:
            return True
        else:
            return False

def decode_json(request):
    try:
        content = request.json()
    except json.decoder.JSONDecodeError:
        print("incompatible json format input")
    else:
        return content

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#welcome screen
print("""Program do zarzadzania lista swoich kociakow
      ,_     _,
      |\\\___//|
      |=6   6=|
      \=._Y_.=/
       )  `  (    ,
      /       \  ((
      |       |   ))
     /| |   | |\_//
     \| |._.| |/-`
      '"'   '"'

Uzytkownicy: """, users)
input("Press Enter to continue...")
cls()
#check username
user_ID = input(colored("Podaj nazwe uzytkownika: ", "green"))
if user_ID in users:
    params = {
        "sub_id": user_ID
    }
else:
    print("Uzytkownik nie istnieje w bazie.")
    input("Press Enter to exit...")
    exit()

#first update of user's favourite cat list
# favourites_cats.update(get_user_favourites())

#menu content
while x:
    print(colored("""***************************************
    Co chcesz zrobic?
        Sprawdz liste swoich ulubionych kotow   [1]
        Wylosuj kotka                           [2]
        Dodaj kotka                             [3]
        Usun kotka                              [4]
        Wyswietl swoje kotki w przegladarce     [5]
        Zapisz wsoja baze na serwerze           [6]
        Zaladuj ostatni zapis bazy kotkow       [9]
        Wyjdz z programu                        [0]
***************************************""", "green"))
    x = input("Twoj wybor: ")

    if x == "0":
        x = False

    elif x == "1":
        if favourites_cats == {}:
            print("Nie masz jeszcze w bazie zadnego kotka :(")
        else:
            print("Twoje kotki :)\n")
            print(favourites_cats)
        input("\nPress Enter to continue...")
        cls()

    elif x == "2":
        random_cat = find_new_cat()
        print("Wylosowany kotek:\n")
        print(random_cat, "\n")
        save = input("Czy chcesz zapisac kotka do swojej bazy? [Y/N]: ")
        if save == "Y" or save == "y":
            favourites_cats.update(random_cat)
        elif save == "N" or save == "n":
            pass
        else:
            print("Dokonales zlego wyboru")
            input("\nPress Enter to continue...")
            cls()

    elif x == "3":
        cat_id = input("Podaj id kota, ktorego chcesz dodac: ")
        add_user_favourite_cat(cat_id)

        input("\nPress Enter to continue...")
        cls()
    elif x == "4":
        cat_id = input("Podaj id kota, ktorego chcesz usunac: ")
        delete_user_favourite_cat(cat_id)
        # if cat_id in list(favourites_cats.keys()):
        #     delete_user_favourite_cat(cat_id)
        # else:
        #     print("Takie ID nie istnieje w twoje bazie")
        input("\nPress Enter to continue...")
        cls()

    elif x == "5":
        if favourites_cats == {}:
            print("Nie masz jeszcze w bazie zadnego kociaka :(")
        else:
            for cat in list(favourites_cats.values()):
                webbrowser.open_new_tab(cat)
            print("Kociaki zostaly wyswietlone w przegladarce www")
        input("\nPress Enter to continue...")
        cls()

    elif x == "9":
        favourites_cats = {}
        favourites_cats.update(get_user_favourites())
        print("Baza kociakow zostala zaktualizowana")
        input("\nPress Enter to continue...")
        cls()

    else:
        print(colored("Podales nieprawidlowy wybor", "red"))

