# Phase 0: fix the typos/bugs 5 or so of them...!
# Phase 1: Comment this code!
# Phase 2: Build out the game further, make the armies attack one another!
# Phase 3: Set it up some that if a member of an army has less than 0 health remove it from the army
# Phase 4: Set up the battles so that different army types fight differently!
import random
class Human(object):
    def __init__(self, clan = None):
        super(Human, self).__init__()
        print 'New Human!!!', clan
        self.health = 100
        self.strength = 3
        self.intelligence = 3
        self.stealth = 3
        self.clan = clan


    def taunt(self):
        print "You want a piece of me?"
        return self


    def attack(self,target):
        print "*** attack", self, '->', target
        self.taunt()
        luck = round(random.random() * 100)
        attack = self.strength
        print 'luck', luck, 'attacker\'s strength', attack
        if (self.clan):
            # future arguments for determine what to do if your clan is...
            # maybe this should go in to the game class..
            # and there is something else wrong here... but since we aren't using this if statement...
			pass

        print 'luck', luck
        if(luck > 50):
            print 'attempting attack'
            if(luck * self.stealth > 150):
                print 'attacking!'
                target.health -= attack
                target.reporthealth()
                return True
            else:
                print 'attack failed'
                return False
        else:
            self.health -= self.strength
            print "attack failed"
        return False


    def reporthealth(self):
        if self.health > 0:
            print "I am not dead yet!"
        else:
            print "AAAaah you've killed me"


class Ninja(Human):
    def __init__(self, clan = 'Ninja'):
        super(Ninja, self).__init__(clan)
        self.health = 70
        self.steath = 30

class Warrior(Human):
    def __init__(self, clan = 'Warrior'):
        super(Warrior, self).__init__(clan)
        self.health = 130
        self.strength = 30

class Wizard(Human):
    def __init__(self, clan = 'Wizard'):
        super(Wizard, self).__init__(clan)
        self.health = 50
        self.intelligence = 3


class Game(object):
    """docstring for Game"""
    def __init__(self):
        super(Game, self).__init__()
        self.armies = []


    def buildArmy(self, clan = None):
        clanMap = {"Wizard": Wizard, "Ninja": Ninja, "Warrior": Warrior}
        army = []
        if clanMap[clan]:
            for human in range(random.randint(1,10)):
                army.append(clanMap[clan]())
        else:
            for human in range(random.randint(1,10)):
                army.append(Human())
        self.armies.append(army)


    def testRemove(self):
        testHuman = self.armies[0][0]
        print 'testHuman', testHuman
        print 'array    ', self.armies[0]
        self.armies[0].remove(testHuman)
        print 'removedar', self.armies[0]


    def battle(self):
        """ fight """
        print self.armies
        # pick 1 attacker from one clan
        # pick 1 defender from one clan
        # then attacker attacks defender
        for i in range(1,50):
            attackerClanIndex = random.randint(0, len(self.armies) - 1)
            attacker = self.armies[attackerClanIndex][random.randint(0, len(self.armies[attackerClanIndex]) - 1)]
            defenderClanIndex = random.randint(0, len(self.armies) - 1)
            defender = self.armies[defenderClanIndex][random.randint(0, len(self.armies[defenderClanIndex]) - 1)]
            print "-" * 50

            if attacker == defender or attacker.clan == defender.clan:
                continue

            attacker.attack(defender)
            print defender.health
            if attacker.health <= 0:
                print 'attacker', attacker, 'is dead HP:', attacker.health
                print 'before removing array', self.armies[attackerClanIndex]
                self.armies[attackerClanIndex].remove(attacker)
                print 'removed dead attacker from army ->', attacker
                print 'after removing array', self.armies[attackerClanIndex]
                print 'attacker remains', len(self.armies[attackerClanIndex])

            if defender.health <= 0:
                print 'defender', defender, 'is dead HP:', defender.health
                print 'before removing array', self.armies[defenderClanIndex]
                self.armies[defenderClanIndex].remove(defender)
                print 'removed dead defender from army ->', defender
                print 'after removing array', self.armies[defenderClanIndex]
                print 'defender remains', len(self.armies[defenderClanIndex])

            if len(self.armies[attackerClanIndex]) <= 0:
                print 'defender clan won'
                break;

            if len(self.armies[defenderClanIndex]) <= 0:
                print 'attacker clan won'
                break;


game = Game()
game.buildArmy('Ninja')
game.buildArmy('Warrior')
# print game.armies
game.battle()
# game.testRemove()
