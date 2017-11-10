import random
def Main():
	print("Guess The Number!")
	while True:
		choice = (input("Type P to play or Q to quit."))
		
		if choice=='Q':
			print("Thanks for Playing! See you soon!")
			break
		if choice=='P':
			playgame()
		else:
			print("Invalid Choice")
			print (choice)
			


def playgame():
	while True:
		computer_choices = list(range(1,11))
		computer_move= random.choice(computer_choices)
		
		while True:
			player_move = int(input("Enter in a number 1 - 10 or Q to quit.\n"))
			if not validMove(player_move):
				print("Invalid Move\n")
				continue
			elif player_move == computer_move:
				print("You guess correct!")
				print("Thanks for Playing!")
				break
			elif player_move > computer_move:
				print("Go Lower!")
			elif player_move < computer_move:
				print("Go Higher!")
			elif player_move == 'Q':
				print("Thank you for playing!")
				break
			
		
		

def validMove(player_move):
	if player_move in list(range(1,11)):
		return True
	return False
	
	
	
	
Main()
		