guests = ['Albert Einstein', 'Michael K. Williams', 'Bernie Sanders']

name = guests[0].title()
print(f"I would like to formally invite you to my party, {name}!")

name = guests[1].title()
print(f"I would like to formally invite you to my party, {name}!")

name = guests[2].title()
print(f"I would like to formally invite you to my party, {name}!")

name = guests[0].title()
print(f"\nSorry, {name} can't make it to the party!")

#Albert can't make it to the party
del(guests[0])
guests.insert(0,'Gary Bussey')

#Print invitations again
name = guests[0].title()
print(f"\nI would like to formally invite you to my party, {name}!")

name = guests[1].title()
print(f"I would like to formally invite you to my party, {name}!")

name = guests[2].title()
print(f"I would like to formally invite you to my party, {name}!")

#We have a bigger table so we can add more people
print("\nWe have a bigger table!")
guests.insert(0, 'Bill Gates')
guests.insert(2, 'Barrack Obama')
guests.append('Tom Cruise')

name = guests[0].title()
print(f"I would like to formally invite you to my party, {name}!")

name = guests[1].title()
print(f"I would like to formally invite you to my party, {name}!")

name = guests[2].title()
print(f"I would like to formally invite you to my party, {name}!")

name = guests[3].title()
print(f"I would like to formally invite you to my party, {name}!")

name = guests[4].title()
print(f"I would like to formally invite you to my party, {name}!")

name = guests[5].title()
print(f"I would like to formally invite you to my party, {name}!")