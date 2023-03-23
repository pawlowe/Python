#-----------1.42---------------------
slownik = {"-":"minus", "0":"zero", "1":"jeden", "2":"dwa", "3":"trzy", "4":"cztery",
           "5":"pięć", "6":"sześć", "7":"siedem", "8":"osiem", "9":"dziewięć"}
wyraz = input("Wprowadź dowolną liczbę\n")
zapis = ""
for letter in wyraz:
    slowo = slownik.get(letter)
    zapis = zapis + slowo + " "
print(zapis.strip())
#-----------1.43---------------------
slowa = {}
len_0 = 0
for i in range(5):
    slowo_i = input("Wprowadź słowo: \n")
    len_i = len(slowo_i)
    print(len_i)
    if len_i > len_0:
        len_0 = len_i
        final = slowo_i
print("Nadłuższe słowo to: ", final)        
#-----------1.44---------------------
wiek = int(input("Podaj swój wiek: \n"))
if wiek < 18:
    print("dziecko")
elif wiek >= 18 and wiek <=45:
    print("młody")
else:
    print("ok")
#-----------1.45---------------------
wiek = int(input("Podaj swój wiek: \n"))
plec = input("Podaj swoją płeć: \n")
if wiek < 18:
    print("dziecko")
elif wiek >= 18 and wiek <=60:
    print("Pracujesz?")
elif wiek > 60 and wiek <=65:
    if plec.lower() == "m":
        print("Pracujesz?")
    else:
        print("emeryt")
else:
    print("emeryt")
#-----------1.46---------------------
number = int(input("Podaj liczbę całkowita dodatnią\n"))
             
while number < 0:
    print("Źle, jeszcze raz")
    number = int(input("Podaj liczbę całkowita dodatnią\n"))
#-----------1.47---------------------
lista = [4, 5, 6, 7]
while len(lista) != 0:
    del lista[0]
    print(lista)
#-----------4.1----------------------
start = int(input("Wprowadź liczbę początkową\n"))
end = int(input("Wprowadź liczbę końcową\n"))
distance = int(input("Wprowadź jaki ma być odstęp między kolejnymi liczbami\n"))
value = start
while value <= end:
    print(value)
    value += distance
#-----------1.48----------------------
print(((1.e+3+34.5),)*20)
#-----------4.2----------------------
word = input("Wpisz dowolne słowo\n")
position = len(word)
new_word = ""
for i in range(position):
    new_word += word[position-1]
    position -= 1
print(new_word)
#-----------1.49----------------------
sum = 0
for i in range(1000):
    sum += i
print(sum)    
#-----------4.3----------------------
import random
WORDS = ("python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon")
word = random.choice(WORDS)
correct = word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]
print("Witaj w grze. Uporządkuj litery aby odgadnąć słowo")
print("Zgadnij jakie to słowo: " , jumble)
guess = input("\nTwoja odpowiedź: ")
point = 100
while guess != correct and guess != "":
    print("Niestety, to nie to słowo.")
    help = int(input("Jeśli potrzebujesz podpowiedzi wprowadź 1, jeśli nie 0\n"))
    if help == 1:
        value = random.randrange(len(correct))
        letter = correct[value]
        print(value + 1, " litera słowa to: ", letter)
        guess = input("\nTwoja odpowiedź: ")
        point -=5
    else:    
        guess = input("\nTwoja odpowiedź: ")
        point -= 1
if guess == correct:
    print("Zgadza się!, Zgadłeś! Zdobyta ilość punktów wynosi: ", point)
#-----------1.50----------------------
for i in range(100):
    print(i+1)
sum = 101
for ii in range(100):
    value = sum - (ii+1)
    print(value)
for iii in range(50):
    value2 = iii+1
    if value2%2==0:
        print(value2)
for iiii in range(100):
    value3 = iiii +1
    if value3%3==0:
        print(value3)
#-----------4.4----------------------
dictionary = ("kolorowe", "anagram", "łatwy", "jarmarki", "odpowiedź", "gra")
word1 = random.choice(dictionary)
letters = len(word1)
your_word = ""
chance = 5
print("Witaj w grze. Zgadnij jakie to słowo: ")
print(letters*'_ ')
print("Masz 5 szans aby dopytać o litery, które znajdują się w danym słowie.")
print("Potem będziesz musiał odgadnąć to słowo")
for i in range(chance):
    letter = input("Podaj literę: ")
    if letter in word1:
        print("Tak. Ta litera występuje w tym słowie")
    else:
        print("Nie. Ta litera nie występuje w tym słowie")
your_word = input("Podaj swoją odpowiedź: ")
if your_word == word1:
    print("Gratulacje! Odgadłeś słowo")
else:
    print("Niestety nie udało Ci się odgadnąć. Prawidłowe słowo to: ", word1)
    



