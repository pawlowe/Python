#------------------1.54------------------------
SPK = int(input("Podaj kapitał początkowy:\n"))
P = int(input("Podaj oprocentowanie:\n"))
N = int(input("Podaj okres oszczędności:\n"))

Kn = SPK*((1+(P/(100*12)))**(N*12))

print(f"Całkowita kwota oszczędności na koniec okresu rozliczeniowego wyniesie: {Kn:.2f}")
numbers = []
#------------------1.55------------------------
for i in range(2000, 3200):
    if(i%7==0 and i%5!=0):
        numbers.append(i)
        
print(numbers)
#------------------5.1-------------------------
import random
words = ["kot", "pies", "kogut", "kura", "koń", "słoń"]
numbers = []
iterrations = len(words)
for i in range(iterrations):
    number = random.randint(0, iterrations-1)
    while number in numbers:
        number = random.randint(0, iterrations-1)
    numbers.append(number)
    print(words[number])
#-----------------1.56 --------------------------
text = input("Wprowadź jakiś tekst:\n")
print(text.split("."))
for i in text.split("."):
    print(len(i.split()))
#------------------5.2---------------------------
points = 30
inventory = []

choice = None
while choice != "0":

    print(
    """
    Konfiguracja postaci:

    0 - zakończ
    1 - wyświetl inwentarz i liczbę punktów
    2 - dodaj produkt do inwentarza
    3 - usuń produkt z inwentarza
    """
    )

    choice = input("Wybierasz: ")

    if choice == "0":
        print("Zakończyłeś tworzenie swojego bohatera. Twój inwentarz to: ")
        print(inventory)

    elif choice == "1":
        print("Oto Twój inwentarz: ", inventory)
        print("Twoja liczba punktów: ", points)

    elif choice == "2":
        value = None
        while value != "0":
    
            print(
            """
            Którą z cech chcesz dodać do swojego bohatera
            0 - wyjdź z kreatora
            1 - siła 10 pkt
            2 - zdrowie 15 pk
            3 - mądrość 15 pkt
            4 - zręczność 10 pkt
            """
            )
        
            value = input()
            
            if value == "0":
                print("Zakończyłeś dodawanie cech do swojego bohatera. Twóje cechy to: ")
                print(inventory)
        
            elif value == "1":
                if points >= 10:
                    inventory.append("Siła")
                    points -= 10
                else:
                    print("Masz za mało punktów aby wybrać tą opcję")
                    print(points)

            elif value == "2":
                if points >= 15:
                    inventory.append("Zdrowie")
                    points -= 15
                else:
                    print("Masz za mało punktów aby wybrać tą opcję")
                    print(points)
                    
            elif value == "3":
                if points >= 15:
                    inventory.append("Mądrość")
                    points -= 15
                else:
                    print("Masz za mało punktów aby wybrać tą opcję")
                    print(points)
            else:
                if points >= 10:
                    inventory.append("Zręczność")
                    points -= 10
                else:
                    print("Masz za mało punktów aby wybrać tą opcję")
                    print(points)    

    elif choice == "3":
        value2 = None
        while value2 != "0":
    
            print(
            """
            Którą z cech chcesz dodać do swojego bohatera
            0 - wyjdź z kreatora
            1 - siła 10 pkt
            2 - zdrowie 15 pk
            3 - mądrość 15 pkt
            4 - zręczność 10 pkt
            """
            )
        
            value2 = input()
            
            if value2 == "0":
                print("Zakończyłeś dodawanie cech do swojego bohatera. Twóje cechy to: ")
                print(inventory)
        
            elif value2 == "1":
                if "Siła" in inventory:
                    inventory.remove("Siła")
                    points += 10
                else:
                    print("Nie ma takiej pozycji na liście Twojego inwentarza")
            elif value2 == "2":
                if "Zdrowie" in inventory:
                    inventory.remove("Zdrowie")
                    points += 15
                else:
                    print("Nie ma takiej pozycji na liście Twojego inwentarza")
            elif value2 == "3":
                if "Mądrość" in inventory:
                    inventory.remove("Mądrość")
                    points += 15
                else:
                    print("Nie ma takiej pozycji na liście Twojego inwentarza")
            else:
                if "Zręczność" in inventory:
                    inventory.remove("Zręczność")
                    points += 10
                else:
                    print("Nie ma takiej pozycji na liście Twojego inwentarza")
