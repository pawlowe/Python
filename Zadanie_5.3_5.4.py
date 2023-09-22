
family = {"Jan Kowalski":"Marian Kowalski", "Marek Nowak":"Arek Nowak", "Marian Kowalski":"Józef Kowalski", "Arek Nowak":"Karol Nowak"}
option = ""
son = ""
father = ""
optionList = ["0", "1", "2", "3", "4"]

print("Opcje do wyboru:")
print("""
        0 - sprawdź ojca
        1 - dodaj nową parę
        2 - usuń parę
        3 - zmień imię i nazwisko ojca
        4 - sprawdź dziadka""")

option = input("Wybierz opcję: ")

while option not in optionList:
    print("Podano nieprawidłową opcję wyboru. Wpisz poprawną wartość: ")
    option = input("Wybierz opcję: ")    

son = input("Wprowadź imię i nazwisko syna: ")

if son in family:
    if option == "0":
        print("Ojcem " + son + " jest " + family[son])
    elif option == "2":
        del family[son]
    elif option == "3":
        family[son] = input("Wprowadź imię i nazwisko ojca: ")
    else:
        secondSon = family[son]
        print("Dziadkiem " + son + "jest " + family[secondSon])
else:
    if option == "1":
        print("Dodaj nową parę w relacji syn - ojciec: ")
        print("Imię i nazwisko syna: %s", son)
        father = input(" Wprowadź imię i nazwisko ojca: ")
        family[son]=father
    else:
        print("Nie ma takiej osoby na liście.")

print(family)