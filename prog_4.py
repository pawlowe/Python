#-----------1.51----------------------
notes = ["1", "2", "3", "4", "5", "6"]
sum = 0
i = 0

note = input("Wpisz swoją ocenę: ")

while note != "":
    if note in notes:
        sum += int(note)
        i += 1
        note = input("Wpisz swoją ocenę: ")
    else:
        print("Podano nie wpłaściwą ocenę")
        note = input("Wpisz swoją ocenę: ")

avg = sum/i

print("Średnia twoich ocen wynosi: ", avg)
#-----------1.52-----------------------
value = 30
sila = 20
zdrowie = 15
madrosc = 10
zrecznosc = 15

while value > 0:
    print("""Wybierz atrybuty swojego bohatera:\n
          A - siła(20pkt)\n
          B - zdrowie(15pkt)\n
          C - mądrość(10pkt)\n
          D - zręczność(15pkt)\n""")
 
    selection = input("Wprowadź odpowiednią literę atrybutu ")
    print(selection)
    if(selection == "A" or selection == "a"):
        if(value - sila >= 0):
            value -= sila
            print(value)
        else:
            print("Masz za malo pkt, aby wybrać ten atrybut ")
    elif(selection == "B" or selection == "b"):
        if(value - zdrowie >= 0):
            value -= zdrowie
            print(value)
        else:
            print("Masz za malo pkt, aby wybrać ten atrybut ")
    elif(selection == "C" or selection == "c"):
        if(value - madrosc >= 0):
            value -= madrosc
            print(value)
        else:
            print("Masz za malo pkt, aby wybrać ten atrybut ")
    elif(selection == "D" or selection == "d"):
        if(value - zrecznosc >= 0):
            value -= zrecznosc
        else:
             print("Masz za malo pkt, aby wybrać ten atrybut ")
    else:
        print("Nie wybrano żadnej opcji")

print("Możesz rozpocząć grę")
#-----------1.53-----------------------
F = -68

for i in range(-20, 41):
    if(i >= 0):
        if(F >= 0):
            print( "+", i, " C | +", F, "F")
        else:
            print( "+", i, " C | ", F, "F")
    else:
        if(F >= 0):
            print(  i, " C | +", F, "F")
        else:
            print(  i, " C | ", F, "F")
    F += 5  
