side = 10
side_inc = 10


def draw_rectangle(sid):
    pendown()
    for i in range(4):
        forward(sid)
        left(90)
    penup()
    forward(sid*2)





penup()
setposition(-150,0)

for i in range(5):
    draw_rectangle(side)
    side += side_inc