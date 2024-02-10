low = 1
high = 6
question = "Wprowadzono niepoprawną wartość. Podaj liczbę jeszcze raz"

response = int(input("Podaj liczbę z zakresu: %s do %s " % (low, high)))

def ask_number(question, low, high):
    "poproś o podanie liczby z odpowiedniego zakresu"
    if response not in range(int(low), int(high)):
       response = low 
    return response 
    
#main

ask_number(response==1, low, high)
print(response) 