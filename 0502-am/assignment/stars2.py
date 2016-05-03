def draw_stars(array):
    for value in array:
        # print
        stars = ""

        value = str(value)
        if value.isdigit():
            # 1 2 3,, etc
            star_string = "*"
            length = int(value)
        else:
            star_string = value[:1]
            length = len(value)
        for s in range(length):
            stars += star_string

        # print star_string
        # print length
        print stars

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)
print "-----"
y = ["00w", "w00", 4, "10", 0, "d","s", "0"]
draw_stars(y)
