import random

print ("1 is wide reciever, 2 is tackle, 3 is guard, 4 is guard, 5 is tackle, 6 is tight end, 7 is wr, 8 is qb, 9 is fb, 10 is hb, 11 center")
min = 1
max = 11

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print ("choosing positions...")
    print ("The psitions are....")
    number1 = random.randint(min, max)
    number2 = random.randint(min, max)
    print (number1)
    print (number2)
    roll_again = input("choose new positions?")


variable= input("once you have all positions type-ready- if not type -nr- or not ready")



while variable ==("ready"):
	throw = input("if you want a pass type pass, if you want run type run")

	while throw ==("pass"):


		min = 1
		max = 4


		roll_again = input("choose pass?")

		while roll_again == "yes" or roll_again == "y":
			print ("The routes are....")
			number1 = random.randint(min, max)
			number2 = random.randint(min, max)
			print (number1)
			print (number2)
			roll_again = input("choose pass")


	while throw ==("run"):
		print("if you get 1 run a left sweep, if you get 2 run through 3 hole, if you get 3 run through 2 hole, if you get 4 run a right sweep")

		min = 1
		max = 4


		roll_again = "yes"

	while roll_again == "yes" or roll_again == "y":
	    print ("The routes are....")
	    number1 = random.randint(min, max)
	    number2 = random.randint(min, max)
	    print (number1)
	    print (number2)
	    roll_again = input("choose new run? if yes type y if no hit enter")
