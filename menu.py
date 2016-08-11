import random

adjective = ["spicy", "savory", "hearty", "simmering", "mouth-watering", "herby", "finger-licking-good"]
ethnic = [" honduran", " punjabi", " ethiopian", " chinese", " mexican", " italian", " vietnamese" ]
type_of_food = [" curry", " chole", " naan", " roti", " tortillas", " enchiladas"," enfrijoladas"]
menu = []
for i in range(7):
	random_adjective_index = random.randint(0,len(adjective) - 1)
	random_ethnic_index = random.randint(0,len(ethnic) - 1)
	random_type_of_food_index = random.randint(0,len(type_of_food)-1)
	menu_item = adjective [random_adjective_index] + ethnic [random_ethnic_index] + type_of_food [random_type_of_food_index]
	#print(menu_item)
	menu.append(menu_item)
	
print(menu)


	
