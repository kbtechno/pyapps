usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, how are you doing today?")
        else:
            print(f"Hello {username.title()}, thank you for logging in.")
else:
    print("We can't find this user.")
        