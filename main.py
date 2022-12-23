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
	status = 1
	ques_num = 1

	print("\nWelcome to District Cooling System Q&A Game\n")
	start=input("Do you want to start the game? (Press '0' to exit or press 'Enter' to start) :")
	if start == '0':
		sys.exit()
	print("-"*10,"\n") # Divide diff. parts

	for level in (level_1,level_2,level_3):
		for a in range(0,len(level)):
			print(f"Question: {ques_num} : {level[a]['Question']}")
			ques_num += 1

			for i in range(0,len(level[a]["Choice"])):
				print(level[a]["Choice"][i])

			while True:
				print("\n") 
				ans=input("Your Ans: ").upper()

				if status == 1 and ans in ("A","B"):
					break
				elif status == 2 and ans in ("A","B","C","D"):
					break
				elif status == 3 and ans in ("A","B","C","D","E"):
					break
				else:
					print("Your input is wrong. Please input again.\n")

			if ans == level[a]["Ans"]:
				print("Well Done!")
				score += 1
				correct += 1

			else:
				print("Good Try")
				wrong += 1
				print("\nThe Correct Ans: ",level[a]["Ans"])

			history.append(ans)

			if level[a]["Elaborations"] != "null":
				print('\nElaborations: ',level[a]["Elaborations"],"\n\n")

			print("Your Score: ",score)
			print("-"*20,"\n")
			time.sleep(2)	# Wait 2 second for the user to read the elaborations

		status += 1
		if status <= 3:
			print(f"Congratulation! You are level {status}\n")
			
