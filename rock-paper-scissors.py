# # # # # # # # # # # # #  # # # # # # # # # # # #  # # # # # # # # # # # # 
# Super simple Python game of Rock, Paper, Scissors!
#
#
# Original problem from:
#    http://www.reddit.com/r/beginnerprojects/comments/2ah82f/rock_paper_scissors/
# Instructions:
# 1. Ask RPS
# 2. Computer move
# 3. Compare
#    ((score?))
# 4. Results
#    ((again?))
#
# # # # # # # # # # # # # 

from random import randint

# # # # # # # # # # # # # # #
#
# Define Global Variables!
#
# # # # # # # # # # # # # # #
active = True
p_score = 0
c_score = 0
draw = 0

# # # # # # # # # # # # # 
#
# Define functions!
#
# # # # # # # # # # # # # 
def computer_turn():

	# generate random no. 0-2
	comp_choice = randint(0,2)
	print comp_choice
	if comp_choice == 0:
		return "rock"
	elif comp_choice == 1:
		return "paper"
	elif comp_choice == 2:
		return "scissors"
	else:
		print "Error ocurred during computer's turn."
		return

def compare_choices(p, c):
	global p_score
	global c_score
	global draw

	if p == "rock":
		if c == "rock":
			draw += 1
			return "draw"
		elif c == "paper":
			c_score += 1 
			return "computer"	
		elif c == "scissors":
			p_score += 1
			return "player"

	elif p == "paper":
		if c == "rock":
			p_score += 1
			return "player"
		elif c == "paper":
			draw += 1
			return "draw"
		elif c == "scissors":
			c_score += 1
			return "computer"

	elif p == "scissors": 
		if c == "rock":
			c_score += 1
			return "computer"
		elif c == "paper":
			p_score += 1
			return "player"
		elif c == "scissors":
			draw += 1
			return "draw"
	return

def print_results():
	global active
	print "Player: {0} \n Computer: {1} \n Draws: {2}".format(p_score, c_score, draw)
	while(True):
		choice = raw_input("Play again (y/n): ").lower()
		if choice == "y" or choice == "yes":
			active = True
			break
		elif choice == "n" or choice == "no":
			active = False
			break
		else:
			print "Unrecognized command, try again!"
	return


# # # # # # # # # # # # # 
#
#
# Start main program !!
#
# # # # # # # # # # # # # 

print "Welcome to RPS!"

while active: 

	while True:
		p_input = raw_input("Please enter a choice (Rock, Paper, Scissors OR RPS): ").lower()
		if p_input == "rock" or p_input == "paper" or p_input == "scissors" or p_input == "r" or p_input == "p" or p_input == "s":
			if p_input == "r":
				p_input = "rock"
			elif p_input == "p":
				p_input = "paper"
			elif p_input == "s":
				p_input = "scissors"
			break
		else:
			print "Please enter a valid choice (rock, paper, scissors (r, p, s)!"
	
	c_input = computer_turn()
	print p_input
	print c_input
	winner = compare_choices(p_input, c_input)

	if winner == "player":
		print "Player wins!"
	elif winner == "computer":
		print "Computer wins!"
	elif winner == "draw":
		print "Tie!"

	print_results()

print "Thanks for playing!"
