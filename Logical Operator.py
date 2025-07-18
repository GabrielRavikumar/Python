temperature = int(input("Enter the temperature in celsius :"))
rain = input("Is it Raining (Type yes/no) :")
if temperature > 35 or temperature < 0 or rain == 'yes':
    print("The outdoor event is cancelled.")
else:
    print("The outdoor event has been scheduled.")