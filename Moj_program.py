print("Hello world")
#-----------------------------------------
num = 2+2
print(num)
print(2+2)
#-----------------------------------------
dir(min)
#-----------------------------------------
list = [1, 15, 2, -2, 18]
print(min(list))
#-----------------------------------------
value = (((10+10)/2)-5)*3
print(int(value))
#-----------------------------------------
n = "moje imie"
print(n)
#-----------------------------------------
cytat = '''"Początek jest najważniejszą częścią pracy" - Platon'''
print(cytat)
#-----------------------------------------
cytat = '''"Początek jest najważniejszą częścią pracy" - Platon'''
print(cytat.upper())
#-----------------------------------------
cytat = '''"Pocz ątek jest najważni ejszą częś cią pracy" - Platon'''
print(cytat[0:5] + cytat[6:24] + cytat[25:35] + cytat[36:])
#-----------------------------------------
text = "Nauka programowania wymaga wytrwałej pracy"
print(text[0:19])
print(text[20:26])
print(text[27:])
#-----------------------------------------
zmienna = "Warto się uczyć - programowanie jest ciekawe"
print(zmienna[16:])
print(zmienna[0:18])
#-----------------------------------------
num1 = "10"
num2 = "20"
num3 = "30"
print(num1 + num2 + num3)
num1_1 = int(num1)
num2_2 = int(num2)
num3_3 = int(num3)
print(num1_1 + num2_2 + num3_3)
#-----------------------------------------
zmienna1 = 10
zmienna2 = 20
zmienna3 = 30
zmienna4 = zmienna1 + zmienna2 + zmienna3
print(zmienna4)
zmienna5 = str(zmienna1) + str(zmienna2) + str(zmienna3)
print(zmienna5)
zmienna6 = ' oraz '
print(str(zmienna1) + zmienna6 + str(zmienna2) + zmienna6 + str(zmienna3))
#-----------------------------------------
text1 = "uczę"
text2 = "się"
text3 = "programowania"
print(' '.join([text1, text2, text3]))
#-----------------------------------------
a = 4
b = 7
print((a+b)-a,(a+b)-b)
#-----------------------------------------
a = 1
b = 2
print(a, b)
print(a + b)
#-----------------------------------------
b= 3
print(a, b)
#-----------------------------------------
b = 2
b = b + 5
print(b)
del b
#-----------------------------------------
napis = "hello"
calkowita = int(20)
rzeczywista = 10
#-----------------------------------------
z = 17%7
print( z*(z+3))
#-----------------------------------------
h = input("Podaj wysokość trójkąta: ")
h1 = float(h)
a = input("Podaj podstawę trójkąta: ")
a1 = float(a)
p = 0.5 * a1 * h1
print(f'Pole trójkąta wynosi: {p:.2f}')
#-----------------------------------------
miasto = "Warszawa"
panstwo = "Polska"
print(miasto + " " + panstwo)
#-----------------------------------------
cyt = '''"Jakiś sobie cytat"'''
aut = "Gal Anonim"
print(cyt + '\n' + '\t' + '\t' + '\t' + aut)
#-----------------------------------------
value = input("Podaj dowolną liczbe całkowitą ")
number = int(value)
if number%2==0:
    print("Podałeś liczbę parzystą")
else:
    print("Podałeś liczbę nieparzystą")
#-----------------------------------------
value = input("Podaj swoją ocenę ")
number = int(value)
if number==5:
    print("dobry uczeń")
else:
    print("pracuj dalej")
#-----------------------------------------
imie = input("Jak masz na imię? ")
nazwisko = input("Jak masz na nazwisko? ")
wiek = input("Ile masz lat? ")
print(imie, nazwisko, wiek, end=" ")
#-----------------------------------------
rachunek = input("\nPodaj kwotę z rachunku: ")
print("Napiwek 15% wynosi: ", (int(rachunek)* 15)/100)
print("Napiwek 20% wynosi: ", (int(rachunek)* 20)/100)
#-----------------------------------------
napis = input("Podaj jakiś wyraz: ")
print(("\n" + napis) * 30)
#-----------------------------------------
#Mój program
number1 = int(input("\nPodaj dowolną liczbe calkowitą\n"))
number2 = int(input("\nPodaj dowolną liczbe calkowitą\n"))
number3 = int(input("\nPodaj dowolną liczbe calkowitą\n"))
print("Suma wszystkich liczb wynosi ", number1 + number2 + number3)
#-----------------------------------------
cena_podstawowa = int(input("Podaj cenę samochodu: \n"))
podatek = (cena_podstawowa * 19)/100
opłata_rej = (cena_podstawowa * 2)/100
prowizja = 2000
dostarczenie = 500
print("Auto: ", cena_podstawowa, "zł.\n" \
      "Podatek: ", podatek, "zł.\n" \
      "Opłata rejestracyjna: ", opłata_rej, "zł.\n" \
      "Prowizja od sprzedaży: ", prowizja, "zł.\n" \
      "Koszt dostarczenia samochodu: ", dostarczenie, "zł.\n" \
      "Całkowity koszt samochodu wynosi: ", \
      cena_podstawowa+podatek+opłata_rej+prowizja+dostarczenie)
#-----------------------------------------
print(3==4)
print(2!=2)
print("Ala ma kota"=="Ola ma kota")
print(3==5 and 1>0 and 4<5)
print(3==3 or 2>4 or 5>7)
#-----------------------------------------
if 2 !=5:
    print('Ok')
#-----------------------------------------
if 2==2:
    print('ok')
else:
    print('błąd')
#-----------------------------------------
liczba = int(input("Podaj jakąś liczbę: \n"))
if liczba > 15:
    print("Twoja liczba jest większa od 15")
elif liczba < 15:
    print("Twoja liczba jest mniejsza niż 15")
else:
    print("Twoja liczba to 15")
#-----------------------------------------
import random
number = random.randint(1,5)
if number == 1:
    print("Znajdziesz złotą monetę")
elif number == 2:
    print("W tym roku pojedziesz na egzotyczne wakacje")
elif number == 3:
    print("W tym tygodniu wygrasz w totolotka")
elif number == 4:
    print("Musisz o siebie dbać, pojawią się problemy zdrowotne")
else:
    print("W tym roku stracisz pracę")
#-----------------------------------------
odpowiedz = input("Czy lubisz podróżować? \n")
if odpowiedz.lower() == 'tak':
    czesto = input("Czy często podróżujesz? \n")
    if czesto.lower() == 'tak':
        print("Dobra robota")
    else:
        print("Podróżuj więcej")
else:
    print("Ciekawe, dlaczego nie?")
#-----------------------------------------
punkty = int(input("Podaj uzyskaną liczbę punktów: \n"))
if punkty <= 20:
    print("Ocena niedostateczna")
if punkty > 20 and punkty <=40:
    print("Ocena dopuszczająca")
if punkty > 40 and punkty <=60:
    print("Ocena dostateczna")
else:
    print("Ocena bardzo dobra")
#-----------------------------------------
import random
o = 0
re = 0
for i in range(100):
    number = random.randint(0, 1)
    if number == 0:
        o += 1
    if number == 1:
        re += 1
        
print("Orzeł wypadł: \n", o , "\nReszka wypadła: \n", re)
