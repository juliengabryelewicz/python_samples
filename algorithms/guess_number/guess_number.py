import random

number = int(random.uniform(1,100))
userchoice = int(input("Your answer: "))
while number != userchoice:
	if userchoice < number:
		print("Too small")
	elif userchoice > number:
		print("Too big")
	else:
		break
	userchoice = int(input("Your answer: "))
print("Correct")
