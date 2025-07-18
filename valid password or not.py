#VALID PASSWORD OR NOT
temp = True
while temp:
    password = input("Enter your password : ")
    if len(password) < 8:
        print("Invalid Password. Minimum 8 characters required.")
    elif not any(i.isupper() for i in password):
        print("Invalid Password. At least one alphabet should be of upper Case [A-Z].")
    elif not any(i.islower() for i in password):
        print("Invalid Password. At least one alphabet should be of lower Case [a-z].")
    elif not any(i.isdigit() for i in password):
        print("Invalid Password. At least 1 number or digit between [0-9].")
    else:
        print("Valid password")