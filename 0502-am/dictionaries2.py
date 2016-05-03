context = {
  'questions': [
   { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
   { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
   { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
   { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
  ]
 }

for key, data in context.items():
    #print data
    for value in data:
        pass
        # print "Q #", value["id"], ": ", value["content"]
        # print "----"

data = {"house":"Haus","cat":"Katze","red":"rot"}

print data.items()
print data.keys()
print data.values()
