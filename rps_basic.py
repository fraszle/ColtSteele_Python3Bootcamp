print("...rock...")
print("...paper...")
print("...scissors...")

choice1 = input("(Enter player 1's choice): ")
choice2 = input("(Enter player 2's choice): ")

print("SHOOT!")

if choice1 == choice2:
	print("It's a tie!")
elif choice1 == "rock":
	if choice2 == "scissors":
		print("player 1 wins!")
	elif choice2 == "paper":
		print("player 2 wins!")
elif choice1 == "paper":
	if choice2 == "rock":
		print("player 1 wins!")
	elif choice2 == "scissors":
		print("player 2 wins!")
elif choice1 == "scissors":
	if choice2 == "paper":
		print("player 1 wins!")
	elif choice2 == "rock":
		print("player 2 wins!")
else:
	print("Something went wrong! :(")
