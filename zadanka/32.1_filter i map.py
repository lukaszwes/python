# Pytanie 31
# Otrzymujesz listę nazwisk jakie klienci wprowadzili w formularz na stronie internetowej.
# - użyj funkcji filter(), aby usunąć z niego wszystkie wpisy, które nie są stringami
# - użyj funkcji map() aby przerobić nazwiska tak, żeby wszystkie były zapisane poprawnie
# z wielkimi literami tylko na początku imienia i nazwiska.

nazwiska = ['jan kot', 18, 'ANNA KRÓL', 'jÓzef BYK', ['nie', 'wasza','sprawa'], 'ROBERT wąŻ']


new_nazwiska = list(filter(lambda x: type(x) is str, nazwiska))


final_nazwiska = list(map(lambda x: str(x).lower().title(), new_nazwiska))


final_nazwiska2 = [str(x).lower().title() for x in new_nazwiska]


print(final_nazwiska)
print(final_nazwiska2)

