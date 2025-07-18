#DICTIONARY
capitals = {"India":"New Delhi",
            "Germany":"Berlin",
            "Sri Lanka":"Colombo",
            "Japan":"Tokyo",
            "Russia":"Moscow"}
print("keys:")
print(capitals.keys())
for key in capitals.keys():
    print(key,end = ", ")
print()
print()

print("values:")
print(capitals.values())
for value in capitals.values():
    print(value,end = ", ")
print()
print()
print("After update : ")
capitals.update({"England":"London"})
#capitals.pop("Germany")
print(capitals)
print()
print("After pop : ")
capitals.popitem()
print(capitals)