#Zbiory znaków
a = ['a','e','i','o','u']
b = ['b','c','d','f','g','h','j','k','l','m','n','p','r','s','t','w','z','x','y']
c = ['1','2','3','4','5','6','7','8','9']

#Zapytanie użytkownika o ciąg znaków
text = input('Wpisz dowolny wyraz:')
samogloski = []
spolgloski = []
liczby = []
inne = []

#Zliczanie ciągu znaków
for i in range(len(text)):
    if text[i] in a:
         samogloski.append(text[i])
    elif text[i] in b:
        spolgloski.append(text[i])
    elif text[i] in c:
        liczby.append(text[i])
    else:
        inne.append(text[i])

#Wyświetlanie wyników
print ('Ilość wpisanych samogłosek:', len(samogloski))
print ('Ilość wpisanych spółgłosek:', len(spolgloski))
print ('Ilość wpisanych cyfr:', len(liczby))
print ('Ilość wpisanych znaków:', len(inne))


