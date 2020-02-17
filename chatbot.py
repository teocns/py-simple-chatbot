import random
import pandas as pd

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']
random_greeting = random.choice(greetings)

question = ['How are you?','How are you doing?']
responses = ['Okay',"I'm fine"]
random_response = random.choice(responses)

data = {
    "john":500,
    "mark":200,
    "shaun":300
}


while True:
	userInput = input(">>> ")
	if userInput in greetings:
		print(random_greeting)
	elif userInput in question:
		print(random_response)
	elif userInput.lower() in data:
		print(data[userInput])
	elif userInput == 'exit':
		exit()
	else:
		print("I did not understand what you said")
