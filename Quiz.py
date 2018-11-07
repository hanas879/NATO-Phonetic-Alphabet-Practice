import random
from time import sleep
import os

questions = ["What is A?", "What is B?", "What is C?", "What is D?", "What is E?", "What is F?", "What is G?", "What is H?", "What is I?", "What is J?", "What is K?", "What is L?", "What is M?", "What is N?", "What is O?", "What is P?", "What is Q?", "What is R?", "What is S?", "What is T?", "What is U?", "What is V?", "What is W?", "What is X?", "What is Y?", "What is Z?"]
answers = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"]
stopCommands = ["exit", "Exit", "quit", "Quit", "stop", "Stop"]
quit = False

score = 0

def clear():
	os.system("cls" if os.name=="nt" else "clear")




#	The main game code starts here:

while quit == False:
	
	randomNumber = random.randint(0, 25)

	print("########################################")
	print("##             Score: ", score,"             ##")
	print("########################################")
	print("")
	print(questions[randomNumber])

	answer = input()

	if answer == answers[randomNumber]:
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

file = open("SCORE.txt", "w")
file.write( "Score: " + str(score));
file.close()
sleep(5)
















"""
   __                      ___ _______ 
  / /  ___ ____  ___ ____ ( _ )_  / _ \
 / _ \/ _ `/ _ \/ _ `(_-</ _  |/ /\_, /
/_//_/\_,_/_//_/\_,_/___/\___//_//___/ 
                                       

"""