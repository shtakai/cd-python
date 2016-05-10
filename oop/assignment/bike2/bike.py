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
        return self

    def reverse(self):
        reverseMile = 5
        print "Reversing"
        if (self.miles - reverseMile) >= 0:
            self.miles -= reverseMile
        return self


bike1 = Bike(200, "25mph")
bike2 = Bike(100, "30mph")
bike3 = Bike(10, "5mph")

bike1.ride().ride().ride().reverse().displayinfo()
print "*" * 3

bike2.ride().ride().reverse().reverse().displayinfo()
print "*" * 3

bike3.reverse().reverse().reverse().displayinfo()
print "*" * 3

