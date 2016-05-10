class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print "PRICE:{} Maximum Speed:{} Total Miles:{}".format(self.price, self.max_speed, self.miles)

    def ride(self):
        print "Riding"
        self.miles += 10

    def reverse(self):
        reverseMile = 5
        print "Reversing"
        if (self.miles - reverseMile) >= 0:
            self.miles -= reverseMile


bike1 = Bike(200, "25mph")
bike2 = Bike(100, "30mph")
bike3 = Bike(10, "5mph")

bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayinfo()
print "*" * 3

bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayinfo()
print "*" * 3

bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayinfo()
print "*" * 3

