menu_items = ('prime rib', 'lobster', 'mashed potatoes', 'smoked salmon', 'sirloin steak')

print("You can choose from these items on our menu:")
for item in menu_items:
    print(f"- {item}")
    
#menu_items.append('creamed corn') ---Program will not execute this because we are
#dealing with a tuple

menu_items = ('prime rib', 'lobster', 'mashed potatoes', 'fried cod', 'texas toast')

print("\nOur menu has changed.")
print("You can now choose from our updated menu:")
for item in menu_items:
    print(f"- {item}")