#**kwargs in function
def address(**kwargs):
    for value in kwargs.values():
        print(value)
    print()
    for key in kwargs.keys():
        print(key)
    print()
    for key, value in kwargs.items():
        print(f"{key} : {value}")
address(country = "India",
        state = "Tamil Nadu",
        district = "Coimbatore",
        area = "Karamadai")