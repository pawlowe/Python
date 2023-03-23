#-----------1,39---------------
name = input("Podaj swoje imie \n")
lista = []
for i in name.upper():
    if i not in lista:
        lista.append(i)
sorted_lista = sorted(lista)
print(sorted_lista)
#-----------1,40---------------
name = input("Podaj imie \n")
surname = input("Podaj nazwisko \n")
name2 = name.strip()
surname2 = surname.strip()               
number = len(name2) + len(surname2)
lista_name = set()
for i in name2.upper():
     if i not in lista_name:
        lista_name.add(i)          
lista_surname = set()
for i in surname2.upper():
     if i not in lista_surname:
        lista_surname.add(i)
unique = set()
for i in lista_name:
    if i not in lista_surname:
        unique.add(i)
for i in lista_surname:
    if i not in lista_name:
        unique.add(i)
print( number, len(unique))
#-----------3.3---------------------
import random
number = random.randint(1,100)
tries = 1
guess = int(input("Podaj liczbę od 1 do 100. Na zgadnięcie liczby masz 5 szans\n"))

while guess != number and tries <= 4:
        if guess > number:
            print("Niestety to nie ta liczba. Twoja liczba jest za duża. Próbuj dalej")  
        else:
            print("Niestety to nie ta liczba. Twoja liczba jest za mała. Próbuj dalej")
        tries += 1
        guess = int(input("Podaj liczbę od 1 do 100. Na zgadnięcie liczby masz 5 szans\n"))

if guess == number:
    print("Brawo! Udało Ci się zgadnąć. Liczba to: ", number, "\n Ilość prób to: ", tries)
else:
    print("niestety zabrakło Ci szans, nie odgadłeś liczby ", number)
#-----------1,41---------------
month1 = input("Podaj nazwę pierwszego miesiąca: sty, lut, mar, kwi, maj, lip, sie, wrz, paz, lis, gru\n")
month2 = input("Podaj nazwę drugiego miesiąca: sty, lut, mar, kwi, maj, cze, lip, sie, wrz, paz, lis, gru\n")
months = {"sty":1, "lut":2, "mar":3, "kwi":4, "maj":5, "cze":6, "lip":7, "sie":8, "wrz":9, "paz":10, "lis":11, "gru":12}
value1 = months[month1.lower()]
value2 = months[month2.lower()]
if value1 == value2:
    print("Ilość miesięcy, która mija od pierwszego do drugiego miesiąca wynosi: 12")
elif value1 > value2:
    result = 12 - value1 + value2
    print("Ilość miesięcy, która mija od pierwszego do drugiego miesiąca wynosi: ", result)
else:
    result = value2 - value1
    print("Ilość miesięcy, która mija od pierwszego do drugiego miesiąca wynosi: ", result)
#-----------3.4---------------------
import random
number = int(input("Podaj liczbę całkowita od 1 do 100. Komputer na odgadnięcie Twojej liczby będzie miał 5 szans\n"))
tries = 1
guess = 50
value = guess // 2

while guess != number and tries <= 4:
        if guess > number:
            print("Niestety to nie ta liczba. Twoja liczba jest za duża. Próbuj dalej")
            guess = guess - value
        else:
            print("Niestety to nie ta liczba. Twoja liczba jest za mała. Próbuj dalej")
            guess = guess + value
        tries += 1
        value = value // 2
        
if guess == number:
    print("Brawo! Udało Ci się zgadnąć. Liczba to: ", number, "\n Ilość prób to: ", tries)
else:
    print("niestety zabrakło Ci szans, nie odgadłeś liczby ", number)
#-----------1.42---------------------
slownik = {"-":"minus", 0:"zero", 1:"jeden", 2:"dwa", 3:"trzy", 4:"cztery",
           5:"pięć", 6:"sześć", 7:"siedem", 8:"osiem", 9:"dziewięć"}
wyraz = input("Wprowadź dowolną liczbę\n")
for letter in wyraz:
    print(letter)
    slowo = slownik.get(letter)
    print(slowo)
    #spacja = " "
    zapis = slowo
print(zapis.strip())    
