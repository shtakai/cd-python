class Animal(object):
    def __init__(self, name):
        self.name   = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print "Animal", "Name:", self.name, "Health:", self.health


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self


class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print "this is a dragon!"
        super(Dragon, self).displayHealth()



animal = Animal('animal')
animal.walk().walk().walk().run().run().displayHealth()

dog = Dog('dogeatsdog')
dog.walk().walk().walk().run().run().pet().displayHealth()

dragon = Dragon('Ultima Dragon -Yoshi Asai')
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()

# does not work
# animal.walk.pet()

# does not work
# animal.fly()
