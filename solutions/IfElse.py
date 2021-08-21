print("sayı giririnz : ")
number = int(input())

if number % 2 == 1:
    print("Weird")
else:
    if number>=2 and number <= 5:
        print("Not Weird")
    elif number>=6 and number<=20:
        print("Weird")
    else:
        print("Not Weird")

