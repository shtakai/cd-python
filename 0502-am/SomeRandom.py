print ("hello world")

myVariable = ["phrase1", "phrase2", 37]

myVariable[0] = "new phrase"
#タプル　変更できない
myVariable2 = ("banana", "flower", 42)
#動かない
# myVariable2[0] = "sashimi"
for value in myVariable2:
    print value
