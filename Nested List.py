nested_list = [['gabriel','glady','anand'],
               ['marcian','kishor','indhuja'],
               ['banusri','hema','chathur']]
print('printing an inner list')
print(nested_list[0])
print()
print('printing an element in the inner list')
print(nested_list[1][2])
print()
print('modifying an inner list')
nested_list[0] = ['manoj','blessy']
print(nested_list)
print()
print('modifying an element in inner list')
nested_list[1][0] = 'benedict'
print(nested_list)
print()
print('adding an inner list')
nested_list.append(['melchi','melsha','juan','jayne'])
print(nested_list)
print()
print('adding an element in an inner list')
nested_list[0].append('prawin')
print(nested_list)
print()
print('Insert at a specific position')
nested_list[1].insert(2,'kavipriya')
print(nested_list)
print()
print('Extend an inner list with multiple values')
nested_list[2].extend(['mithilesh','ashok'])
print(nested_list)
print()
print('final list')
for list_ in nested_list:
    for element in list_:
        print(element)