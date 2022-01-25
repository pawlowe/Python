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
