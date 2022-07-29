length = 50

while length<=400:
    penup()
    sety(0-length/2)
    backward(length/2)
    pendown()
    for i in range(4):
        forward(length)
        left(90)
    penup()
    setposition(0,0)
    length += 50