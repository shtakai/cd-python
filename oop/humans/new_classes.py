from human import Human

class Wizard(Human):
    def heal(self):
        self.health += 10

class Ninja(Human):
    def steal(self):
        self.stealth += 5

class Samurai(Human):
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
harry.heal()
print harry.health

print "-" * 10
rain.steal()
print rain.stealth

print "-" * 10
tom.sacrifice()
print tom.health
print tom.stealth

