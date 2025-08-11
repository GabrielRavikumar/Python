nested_tuple = (('a','b','c'),('x','y','z'),('p','q','r','s'))
print(nested_tuple)
print('printing elements')
for tuple_ in nested_tuple:
    for element_ in tuple_:
        print(element_, end = ' ')
print()
print('accessing an inner tuple')
print(nested_tuple[0])
print('accessing an element in an inner list')
print(nested_tuple[2][2])
print('modifying tuple (avoiding immutability)')
print(nested_tuple[:1] + (('l','m','n','o'),) + nested_tuple[2:])

