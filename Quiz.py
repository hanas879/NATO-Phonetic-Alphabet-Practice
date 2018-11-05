import random
from time import sleep

questions = ["What is A?", "What is B?", "What is C?", "What is D?", "What is E?", "What is F?", "What is G?", "What is H?", "What is I?", "What is J?", "What is K?", "What is L?", "What is M?", "What is N?", "What is O?", "What is P?", "What is Q?", "What is R?", "What is S?", "What is T?", "What is U?", "What is V?", "What is W?", "What is X?", "What is Y?", "What is Z?"]
answers = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"]
stopCommands = ["exit", "Exit", "quit", "Quit", "stop", "Stop"]
quit = False

score = 0

while quit == False:
	
	randomNumber = random.randint(0, 25)

	print(questions[randomNumber])

	answer = input()

	if answer == answers[randomNumber]:
		score += 1
		print("########################################")
		print("CORRECT! Your score is:", score)
		print("########################################")
		sleep(3)

	elif answer in stopCommands:
		quit = True

	else:
		print("WRONG! The correct answer is: ", answers[randomNumber])
		print("")
		score = 0
		print("########################################")
		print("Your score has been reset. It is now: ", score)
		print("########################################")
		sleep(6)

print("Goodbye!")