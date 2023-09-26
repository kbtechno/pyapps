my_foods = ['pizza', 'falafel', 'carrots']
friend_foods = my_foods[:]

my_foods.append("burrito")
friend_foods.append("taco")

print("My favorite foods are:")
for food in my_foods:
    print(f"- {food}")

print("My friend's favorite foods are:")
for food in friend_foods:
    print(f"- {food}")