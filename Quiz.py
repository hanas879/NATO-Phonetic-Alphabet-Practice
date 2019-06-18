import random
from time import sleep
import os

questions = ["What is A?", "What is B?", "What is C?", "What is D?", "What is E?", "What is F?", "What is G?", "What is H?", "What is I?", "What is J?", "What is K?", "What is L?", "What is M?", "What is N?", "What is O?", "What is P?", "What is Q?", "What is R?", "What is S?", "What is T?", "What is U?", "What is V?", "What is W?", "What is X?", "What is Y?", "What is Z?"]
answers = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"]
stopCommands = ["exit", "Exit", "quit", "Quit", "stop", "Stop"]
quit = False
saveReply = ["Yes", "yes", "No", "no", "Y", "y", "N", "n"]

score = 0

def clear():
	os.system("cls" if os.name=="nt" else "clear")




#	The main game code starts here:

while quit == False:
	clear()
	randomNumber = random.randint(0, 25)

	print("########################################")
	print("##             Score: ", score,"             ##")
	print("##                                    ##")
	print("##      Type 'exit' to end the game   ##")
	print("########################################")
	print("")
	print(questions[randomNumber])

	answer = input().lower().replace(" ", "")

	if answer == answers[randomNumber].lower():
		score += 1
		clear()
		print("----------------------------------------")
		print("                 CORRECT!                 ")
		print("----------------------------------------")
		sleep(1)
		clear()

	elif answer in stopCommands:
		quit = True

	else:
		clear()
		print("----------------------------------------")
		print("WRONG! The correct answer is: ", answers[randomNumber])
		print("----------------------------------------")
		print("")
		print("########################################")
		print("Your score was: ", score)
		score = 0
		print("and have now been reset. It is now: ", score)
		print("########################################")
		sleep(6)
		clear()

clear()
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("      Goodbye! Thanks for playing       ")
print("")
print("      Your final score is: ", score)
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
save = input("Would you like to save the score to a .txt file? y/n: ")

if save in saveReply:

	clear()
	name = input("Please enter your name: ")
	file = open("SCORE.txt", "a")
	file.write('\n' + name + " | Score: " + str(score));
	file.close()
















"""
   __                      ___ _______
  / /  ___ ____  ___ ____ ( _ )_  / _ \
 / _ \/ _ `/ _ \/ _ `(_-</ _  |/ /\_, /
/_//_/\_,_/_//_/\_,_/___/\___//_//___/


"""
