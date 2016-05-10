class Car(object):
    def __init__(self, price, speed, fuel, mileage ):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0.15 if price > 10000 else 0.12

    def display_all(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax
        print


car1 = Car(100000, "11mph", "Full1", "15mph")
car2 = Car(2000, "22mph", "Full2", "25mph")
car3 = Car(30000, "33mph", "Full3", "35mph")
car4 = Car(4000, "44mph", "Full4", "45mph")
car5 = Car(50000, "55mph", "Full5", "55mph")

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
