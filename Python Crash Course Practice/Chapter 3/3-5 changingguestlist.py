guests = ['Albert Einstein', 'Michael K. Williams', 'Bernie Sanders']

name = guests[0].title()
print(f"I would like to formally invite you to my party, {name}!")

name = guests[1].title()
print(f"I would like to formally invite you to my party, {name}!")

name = guests[2].title()
print(f"I would like to formally invite you to my party, {name}!")

name = guests[0].title()
print(f"Sorry, {name} can't make it to the party!")

#Albert can't make it to the party
del(guests[0])
guests.insert(0,'Gary Bussey')

#Print invitations again
name = guests[0].title()
print(f"I would like to formally invite you to my party, {name}!")

name = guests[1].title()
print(f"I would like to formally invite you to my party, {name}!")

name = guests[2].title()
print(f"I would like to formally invite you to my party, {name}!")