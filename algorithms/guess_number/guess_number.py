import random

number = int(random.uniform(1,100))
userchoice = int(input("Votre réponse: "))
while number != userchoice:
	if userchoice < number:
		print("Trop petit")
	elif userchoice > number:
		print("Trop grand")
	else:
		break
	userchoice = int(input("Votre réponse: "))
print("Bonne réponse")
