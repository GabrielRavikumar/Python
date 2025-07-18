#*args in function
def num(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(num(1,2,3,4))