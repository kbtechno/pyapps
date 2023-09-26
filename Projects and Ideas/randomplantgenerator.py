import random

#creating a dictionary of plants for each level of experience
plants = {
    "beginner": ["monsteras", "pothos", "snake plants", "zz plants", "peace lillies"],
    "intermediate": ["philodendrons", "hoyas", "begonias", "succulents", "fiddle leaf figs"],
    "advanced": ["calatheas", "ferns", "alocasias", "peperomias", "stromanthes"]
}

#introduction and prompting user to enter in their experience level
print("\nThis will recommend you a random houseplant based on your experience level.")
plants_type = input("Enter your experience level (beginner, intermediate, advanced): ")

#use dictionary to get a list of plants for the entered experience level
experience = plants.get(plants_type)

#if the experience level is not found in the dictionary print an error message and exit
if experience is None:
    print("Error, you did not choose your level of experience.")
    exit()
    
#randomly choose a plant from the list of plants based on entered experience level   
random_plants = random.choice(experience)

#prints a statement along with the randomly chosen plant
print("\nYour randomly chosen plant is:", random_plants)

#useage of various conditionals to print a short message about the randomly chosen plant
if random_plants == "monsteras":
    print("One of the most popular and commonly found!")
elif random_plants == "pothos" or random_plants == "philodendrons":
    print("There are so many varieties!")
elif random_plants == "succulents" or random_plants == "zz plants" or random_plants == "snake plants":
    print("Make sure you don't overwater them!")
elif random_plants == "fiddle leaf figs":
    print("These look great in the corner of a room!")
elif random_plants == "begonias":
    print("These do really well in the summer!")
elif plants_type == "advanced":
    print("Good luck keeping this one alive! They require a lot of humidity!")
else:
    print(f'{random_plants.title()} are a great choice!')
    
#prints the other items within the chosen list using an f-string and the .join function
print(f'\nHere is the entirety of the list: {", ".join(experience)}.')