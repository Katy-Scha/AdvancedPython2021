from random import choice

class Bird:
    def __init__(self, name=None, weight=0):
        self.name = name
        self.weight = weight
        self.sex = None
    def __repr__(self):
        return (f'I am {type(self).__name__}, with weight {self.weight} g \n') if (self.name is None) else (f'I am {type(self).__name__} {self.name}, with weight {self.weight} g \n')
    def eat(self, n=1):
        self.weight += float(n)
    def run(self, n=1):
        self.weight -= float(n)

class Cock(Bird):
    def __init__(self, name, weight):
        super().__init__(name = name, weight = weight)
        self.sex = 'M'
    def crow(self):
        print("Сock-a-doodle-doo!")

class Hen(Bird):
    def __init__(self, name, weight):
        super().__init__(name = name, weight = weight)
        self.sex = 'F'
    def lay(self):
        return Egg()

class Chicken(Bird):
    def __init__(self, name, weight, sex):
        super().__init__(name = name, weight = weight)
        self.sex = sex
        self.grown = 0
    def grow(self):
        if self.grown==1:
            raise AttributeError("Cock/Hen object has no attribute 'hatch'")
        self.grown = 1
        #print(self, 'Growing...')
        # я понимаю, что питон, ссылочная модель и проч. Но можно ли как-то реализовать, (как в С с указателями) чтобы менялась переменная, которую дали (объект класса на объект другого класса). Как-то так:
        # self = Hen(self.name, self.weight+80) if self.sex=='F' else Cock(self.name, self.weight+100)
        return Hen(self.name, self.weight+80) if (self.sex=='F') else Cock(self.name, self.weight+100)

class Egg(Bird):
    def __init__(self):
        super().__init__(name = None, weight = 50)
        self.hatched = 0
    def eat(self, n=1):
        pass
    def run(self, n=1):
        pass
    def hatch(self):
        if self.hatched == 1:
            raise AttributeError("Chicken object has no attribute 'hatch'")
        self.hatched = 1
        #print(self, 'Hitching...')
        return Chicken(self.name, self.weight, sex=choice(['F', 'M']))

if __name__=='__main__':
    chick = Chicken(name='Alex', weight=3, sex='F')
    hen = Hen(name='Anna', weight=10)
    egg = hen.lay()
    print(hen, chick, egg)
    egg.hatch()
    egg.hatch()