username = input("Enter username: ")
len_username = len(username)
if len_username > 12 :
    print("your username should not be more than 12 characters. ")
elif  not username.find(" ") == -1:
    print("username cannot contain spaces")
elif not username.isalpha():
    print("username cannot contain digits")
else:
    print(f"Welcome {username}")