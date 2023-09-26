favorite_pizzas = ['pepperoni pizza', 'veggie pizza', 'sausage pizza']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("hawaiian pizza")
friend_pizzas.append("pesto pizza")

print("My favorite pizzas on this list are:")
for pizza in favorite_pizzas:
    print(f"- {pizza}")
    
print("\nMy friend's favorite pizzas on this list are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")