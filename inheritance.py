class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def barl(self):
        print('bark')


class Cat(Mammal):
    def be_annoying(self):
        print('annoying')


dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.be_annoying()