for i in range(25,101,25):
    penup()
    setposition(0,0)
    right(90)
    forward(i)
    left(90)
    pendown()
    circle(i)