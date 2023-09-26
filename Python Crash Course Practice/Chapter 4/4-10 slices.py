pizzas = ['pepperoni pizza', 'veggie pizza', 'sausage pizza', 'hawaiian pizza', 'cheese pizza']

print("\nThe first three items in this list are:")
for pizza in pizzas[:3]:
    print(pizza.title())
    
print("\nThe middle three items in this list are:")
for pizza in pizzas[1:4]:
    print(pizza.title())
    
print("\nThe last three items in this list are:")
for pizza in pizzas[2:5]:
    print(pizza.title())