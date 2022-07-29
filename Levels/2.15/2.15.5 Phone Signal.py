width = 10

for i in range(10,51,10):
    for j in range(2):
        forward(width)
        left(90)
        forward(i)
        left(90)
    penup()
    forward(25)
    pendown()