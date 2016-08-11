print("Game of Life")
user_college = input("College or no college: ")
while (user_college != "College") and (user_college != "no college"):
	if user_college == "college":
			user_collegechoice = input("Harvard or Stanford:") 
			if user_collegechoice == "Harvard":
				career_choice = input("Doctor or Lawyer:")
				while (career_choice is not "Doctor") and (career_choice is not "Lawyer"):
					career_choice = input("Doctor or Lawyer:")
				if career_choice == "Doctor":
					print("WOW, You make $400,000/year")
				elif career_choice == "Lawyer":
					print("You make 130,000/year")
				else:
					print("try again")
			elif user_collegechoice == "Stanford":
				print("You are studying abroad!")
				study_abroad = input("Europe or Australia:")
				if study_abroad == "Europe":
					print("You fall in love")
				elif study_abroad == "Australia":
					print("You get bitten by a venomous spider, and sadly you die!")
				else:
					print("try again")
			else:
				print("try again")
	elif user_college == "no college":
		print("YOU WORK AT MCDONALDS FOREVER!")

