weekend = { "Sun": "Sunday", "Mon": "Monday"}
print weekend
vals = dict(one = 1, two = 2)
print vals
capitals = {}
capitals["svk"] = "Bratislaba"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
print capitals
d = { i: object() for i in range(4) }
print d[0]
print d[1]

print weekend["Sun"]
print capitals["svk"]

print
for data in capitals:
    print data

print
for key in capitals.iterkeys():
    print key

print
for val in capitals.itervalues():
    print val

print
for key,data in capitals.items():
    print key," = ", data

print len(capitals)
print cmp(capitals, weekend)



dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]

contory_specialities = zip(countries, dishes)
print contory_specialities

contory_specialities_dict = dict(contory_specialities)
print contory_specialities_dict

countries = ["Italy", "Germany", "Spain", "USA", "Switzerland"]
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
country_specialities = zip(countries,dishes)
print country_specialities
