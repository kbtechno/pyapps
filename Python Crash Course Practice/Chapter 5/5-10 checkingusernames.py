current_users = ['john', 'jerry', 'Cynthia', 'bob', 'marie']
new_users = ['jeff', 'Kyle', 'John', 'bob', 'jessica']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user in current_users:
        print(f"Sorry {new_user}, this name is taken. You will have to create a new username.")
    else:
        print(f"Awesome, {new_user} is still available.")