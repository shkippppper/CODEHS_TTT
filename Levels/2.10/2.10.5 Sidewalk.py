SIDE = 400/8

speed(0)

def draw_square():
    for i in range(4):
        pendown()
        forward(SIDE)
        left(90)
        


penup()
setposition(-200,-200)
for i in range(4):
    for i in range(8):
        draw_square()
        forward(SIDE)
    penup()
    left(90)