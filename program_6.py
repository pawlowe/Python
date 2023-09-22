Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>
-----------1.57-------------------
dictionary = {login1:haslo1, login2:haslo2, login3:haslo3}

login = input("Podaj login: ")
haslo = input("Podaj hasło: ")
klucz = login + ";" + haslo

if klucz in dictionary:
    print("Udało Ci się zalogować"
else:
    print("niepoprawny login lub hasło")
    
