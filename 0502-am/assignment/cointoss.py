import random

def coin_toss():
    heads = 0
    tails = 0

    for value in range(0,5000):
        random_num = int(round(random.random()))
        if random_num == 0:
            result = "a head"
            heads += 1
        if random_num == 1:
            result = "a tail"
            tails += 1
        print "Attempt #" +  str(value + 1) +": Throwing a coin... It's " + result + "!... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
    print "Ending the program, thank you!"
coin_toss()
