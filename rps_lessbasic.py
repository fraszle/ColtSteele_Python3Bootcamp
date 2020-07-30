import random

print("...rock...")
print("...paper...")
print("...scissors...")

player = input("Enter your choice: ")
player = player.lower()

comp = random.randint(1, 3)
if comp == 1:
	comp = "rock"
	print("The computer plays: rock")
elif comp == 2:
	comp = "paper"
	print("The computer plays: paper")
else:
	comp = "scissors"
	print("The computer plays: scissors")

if player == comp:
	print("It's a tie!")
elif player == "rock":
	if comp == "scissors":
		print("Player wins!")
	elif comp == "paper":
		print("Computer wins!")
elif player == "paper":
	if comp == "rock":
		print("Player wins!")
	elif comp == "scissors":
		print("Computer wins!")
elif player == "scissors":
	if comp == "paper":
		print("Player wins!")
	elif comp == "rock":
		print("Computer wins!")
else:
	print("Something went wrong! :(")
