from human import Human

class Wizard(Human):
    def __init__(self):
        super(Wizard, self).__init__()
        self.intelligence = 10
    def heal(self):
        self.health += 10

class Ninja(Human):
    def __init__(self):
        super(Ninja, self).__init__()
        self.stealth = 10
    def steal(self):
        self.stealth += 5

class Samurai(Human):
    def __init__(self):
        super(Samurai, self).__init__()
        self.strength = 10
    def sacrifice(self):
        self.health -= 5

print "-" * 10
harry = Wizard()
rain  = Ninja()
tom   = Samurai()

print "-" * 10
print harry.health
print rain.health
print tom.health

print "-" * 10
print harry.health
harry.heal()
print harry.health

print "-" * 10
print rain.stealth
rain.steal()
print rain.stealth

print "-" * 10
print tom.health
tom.sacrifice()
print tom.health

