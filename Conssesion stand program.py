#CONSSESION STAND PROGRAM
menu = {"idly" : 20,
        "poori" : 30,
        "chapatthi" : 30,
        "parotta" : 30}
cart = []
total = 0
quantity = 0
amount = 0
print("---------- MENU ----------")
for key,value in menu.items():
    print(f"{key} : ₹{value:.2f}")
print("--------------------------")

while True:
    input_food = input("Enter the food you want (q to quit) : ").lower()
    if input_food == "q":
        print("Thank You.")
        break
    else:
        quantity = int(input("Enter the Quantity : "))
        cart.append(input_food)
print("---------- YOUR CART ----------")
for food in cart:
    print(f"{food} : ₹{menu.get(food):.2f} x{quantity}")
    amount = menu.get(food) * quantity
    total +=amount
print(f"Your Total is : ₹{total:.2f}")
print("-------------------------------")