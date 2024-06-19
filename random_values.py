import random

numbers = [10, 30, 40]

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))
    print(random.choices(numbers))


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())