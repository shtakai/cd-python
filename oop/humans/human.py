import random

class Human(object):
    def __init__(self, clan=None):
        print 'New Human!!!'
        self.health = 100
        self.clan = clan
        self.strength = 3
        self.intelligence = 3
        self.stealth = 3


    def taunt(self):
        print "You want a piece of me?"


    def attack(self):
        self.taunt()
        luck = round(random.random() * 100)
        if(luck > 50):
            if (luck * self.strength > 150):
                print 'attacking!'
                return True
            else:
                print 'attack failed'
        else:
            self.health -= self.strength
            print 'attack failed'
            return False


class Point(object):
    def __init__(self, x = 0, y = 0):
        print "created a new point!"
        self.x = x
        self.y = y
    def distance(self):
        return (self.x**2 + self.y**2)**0.5


class Cat(object):
    def __init__(self, color, type, age):
        self.color = color
        self.type = type
        self.age = age


class Test(object):
    def __init__(self, phrase='Nothing was passed'):
        print "this string was passed in: " + phrase
        self.phrase = phrase

test1 = Test('Hello world')
test2 = Test()
print "test1 p" + test1.phrase
print "test2 p" + test2.phrase

michaed = Human('CodingDojo')
jimmy = Human('CodingNinjas')
