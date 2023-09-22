#----------------------1.57-------------------------------------
dictionary = {"login1":"haslo1", "login2":"haslo2", "login3":"haslo3"}

login = input("Podaj login: ")
haslo = input("Podaj hasło: ")
klucz = {login:haslo}

if login in dictionary:
    if dictionary.get(login,) == haslo:
        print("Udało Ci się zalogować")
    else:
        print("niepoprawny login lub hasło")        
else:
    print("niepoprawny login lub hasło")
    
