name = input("Enter your full name without any digits: ")
result = name.isalpha()
if not result :
    print("There is one or more digits in your name.Please correct it.")
else:
    print("👍")