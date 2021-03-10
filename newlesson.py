#############
# FIGYELEM! #
#############

# Egyszerre csak egy része működik, a szekciók el vannak választva. Ha nem szeretnéd, hogy összezavarodjon,
# tegyél egy ilyet: """ az elejére (a #-es részhez) és a végére (a következő #-es rész elejére).

#######################
# Találd ki a számot! #
#######################

import random
goal = random.randint(30, 40) # A 30 és a 40 közötti számok generálása. Ezt átállíthatod kevesebbre vagy többre.
guessnum = int(input("Mennyi próbálkozási lehetőséget szeretnél? | ")) # Ha szeretnéd, hogy ez legyen meghatározva, add meg a változónak azt az értéket, amennyi lehetőséget szeretnél adni a játékosnak.
guess = 0
while goal != guess and guessnum:
    guess = int(input("Tippelj egyet! | ")) # Anmikor a kódot futtatod, ide beírhatsz egy számot.
    guessnum -= 1
    if guess > goal:
        print("Túl magas! | ") # Ide is beírhatsz számot a kód futtatásánál.
    elif guess < goal:
        print("Túl alacsony! | ") # Ide is beírhatsz számot a kód futtatásánál.
if guess == goal:
    print("Siker! A szám %s volt." % goal) # Ha eltaláltad, kapsz egy kexet és kiírja a számot.
else:
    print("Nem sikerült. A szám %s volt." % goal) # Ha nem találtad el, kiírja a számot.

#################
### Fibonacci ###
#################

# Ez itt a Fibonacci, vagy ismertebb nevén az aranymetszés.
# A lényege az, hogy elkezd egy listát (0, 1), és mindig összeadja az első két számot (0 + 1 = 1). Az eredmény lesz a második szám a következő esetnél, tehát 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8, stb.
# Az így létrejött lista: 0, 1, 1, 2, 3, 5, 8.

num1 = 0 # Ha ezt átállítod, a (0, 1)-nél a 0 helyett a te számod lesz írva.
num2 = 1 # Ha ezt átállítod, a (0, 1)-nél az 1 helyett a te számod lesz írva.
counter = 20 # Itt be lehet állítani, hogy hány számig menjen.
# Példa: 10-nél:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
print("A sor: ")
while counter != 0:
    print(str(num1) + "\n")
    temp = num1 + num2
    num1 = num2
    num2 = temp
    counter -= 1

#######################################
# HAMAROSAN: PRÍMSZÁMOK SZELEKTÁLÁSA! #
#######################################
