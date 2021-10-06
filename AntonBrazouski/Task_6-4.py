class Bird:
    
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} bird can fly")

    def walk(self):
        print(f"{self.name} bird can walk")

    def __str__(self):
        print(f"{self.name} can walk and fly")


class FlyingBird(Bird):
    
    def __init__(self, name, ration='It eats mostly grains'):
        Bird.__init__(self, name)
        self.ration = ration

    def eat(self):
        print(self.ration)

    def __str__(self):
        print(f"{self.name} can walk and fly") 
        return str(self.name)


class NonFlyingBird(Bird):

    def __init__(self, name, ration):
        Bird.__init__(self, name)
        # self.name = name
        self.ration = ration

    def fly(self):
        raise AttributeError(f"{self.name} object has no attribute 'fly'")

    def swim(self):
        print(f"{self.name} bird can swim")

    def eat(self):
        print("It eats mostly fish")

    def __str__(self):
        print(f"{self.name} can walk and swim")

# inherit
class SuperBird(FlyingBird, NonFlyingBird):

    def __init__(self, name):
        Bird.__init__(self, name)
        # self.name = name
        self.ration = 'It eats fish'

    def __str__(self):
        print(f"{self.name} bird can walk, swim and fly")
        return ""

    def fly(self):
        # print(f"{self.name} bird can fly")
        # super().fly()
        Bird.fly(self)
    

b = Bird("Anny")
b.walk()

p = NonFlyingBird("Penguin", "fish")
p.swim()
# p.fly() #
p.eat()
    
c = FlyingBird("Canary")
str(c)
c.eat()

s = SuperBird("Gull")
str(s)
s.eat()
s.swim()
s.fly() 
print(SuperBird.mro())