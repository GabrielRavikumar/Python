class Animal:
    alive = True
    def eat(self):
        print('This animal is eating.')
    def sleep(self):
        print('This animal is sleeping.')
class Lion(Animal):
    def roar(self):
        print('The Lion is roaring')
class Falcon(Animal):
    def fly(self):
        print('The Falcon is flying')
class Whale(Animal):
    def swim(self):
        print('The Whale is swimming.')
lion = Lion()
falcon = Falcon()
whale = Whale()

print(lion.alive)
falcon.eat()
falcon.fly()
