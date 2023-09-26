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

#The table isn't ready for the amount of people we invited
print("\nI'm sorry I can only invite 2 people to my party now.")

name = guests.pop()
print(f"I'm sorry but we don't have enough room for you {name}!")

name = guests.pop()
print(f"I'm sorry but we don't have enough room for you {name}!")

name = guests.pop()
print(f"I'm sorry but we don't have enough room for you {name}!")

name = guests.pop()
print(f"I'm sorry but we don't have enough room for you {name}!")

#There should be two remaining guests so we'll invite them
name = guests[0].title()
print(f"\nYou've been invited {name}!")

name = guests[1].title()
print(f"You've been invited {name}!")

#Empty out the list completely
del(guests[0])
del(guests[0])

#Show the list is empty
print(guests)