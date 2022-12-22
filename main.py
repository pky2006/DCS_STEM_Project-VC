import os
import sys
import json
import time

with open("Question Bank.json",encoding='utf-8') as file:
	ques=json.load(file,strict=False) # strict=False allows to store '\n','\t' etc. 

level_1=ques["lv_1"] 
level_2=ques["lv_2"]
level_3=ques["lv_3"]
# structure: [{"Question":xxx, "Choice":["A","B",...],"Ans":xxx, "Elaborations":xxx},{...}]

while True:
	score = 0
	correct = 0
	wrong = 0
	history = []

	print("\nWelcome to District Cooling System Q&A Game\n")
	start=input("Do you want to start the game? (Press '0' to exit or press 'Enter' to start) :")
	if start == '0':
		sys.exit()
	print("-"*10) # Divide diff. parts

	for a in range(0,len(level_1)):
		print("Q: ",level_1[a]["Question"])
		
		for i in range(0,len(level_1[a]["Choice"])):
			print(level_1[a]["Choice"][i])

		while True:
			ans=input("Ans: ").upper()
			if ans == level_1[a]["Ans"]:
				print("Well Done")
				score += 1
				correct += 1

			elif ans not in ("A","B"):
				print("Please input again\n")
				continue

			else:
				print("Good Try")
				wrong += 1
			history.append(ans)
			break


		print(history)
		print('\nElaborations: ',level_1[a]["Elaborations"])
		print("-"*20,"\n")
		time.sleep(2)	# Wait 2 second for the user to read the elaborations
