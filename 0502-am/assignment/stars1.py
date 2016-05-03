def draw_stars(array):
    for value in array:
        stars = ""
        for i in range(value):
            stars += "*"
        print stars

x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)
