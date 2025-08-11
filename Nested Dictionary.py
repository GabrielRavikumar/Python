nested_dict = {'person1' : {'name' : 'Gabriel', 'age' : 20},
               'person2' : {'name' : 'Glady','age' : 21}}
print("printing particular element in the nested dictionary.")
print(nested_dict['person2']['age'])
print(f"name1 : {nested_dict['person1']['name']} " 
      f"\nname2 : {nested_dict['person2']['name']}")
print()
print('adding and printing an element in the nested dictionary')
nested_dict['person3'] = {'name' : 'anand','age' : 22}
print(f"name3 : {nested_dict['person3']['name']}")
print()
print('printing the whole nested dictionary')
for person,details in nested_dict.items():
    print(f"{person} : ")
    for key,value in details.items():
        print(f"{key} : {value}")
    print()
