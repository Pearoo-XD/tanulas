"""import random
goal = random.randint(30, 40)
guessnum = int(input("Mennyi próbálkozási lehetőséget szeretnél? | "))
guess = 0
while goal != guess and guessnum:
    guess = int(input("Tippelj egyet! | "))
    guessnum -= 1
    if guess > goal:
        print("Túl magas! | ")
    elif guess < goal:
        print("Túl alacsony! | ")
if guess == goal:
    print("Siker! A szám %s volt." % goal)
else:
    print("Nem sikerült. A szám %s volt." % goal)"""

"""#################
### Fibonacci ###
#################

num1 = 0
num2 = 1
counter = 20
print("A sor: ")
while counter != 0:
    print(str(num1) + "\n")
    temp = num1 + num2
    num1 = num2
    num2 = temp
    counter -= 1"""

##############################
# Prímszámok 1 és 100 között #
##############################

i = 1
while i < 100:

    i += 1
