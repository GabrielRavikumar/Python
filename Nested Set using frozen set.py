nested_set = {frozenset({'a','b','c'}),frozenset({'p','q','r','s'})}
print(nested_set)
for set_ in nested_set:
    print(set_)
    for element in set_:
        print(element)