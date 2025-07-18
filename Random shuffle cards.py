import random
cards = ["2","3","4","5","6","7","8","9","10","K","Q","J","A"]
print(random.choice(cards))
random.shuffle(cards)
print(cards)