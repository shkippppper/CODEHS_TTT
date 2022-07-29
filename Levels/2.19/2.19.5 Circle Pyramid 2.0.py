speed(0)
radius = 25



def victory():
    for i in range(8):
        left(90)


row_value = int(input("how many circles on the bottom - "))
penup()
setposition(0,-200)

while row_value !=0:
    backward((row_value-1)*radius)
    pendown()
    for i in range(row_value):
        circle(radius)
        penup()
        forward(radius*2)
        pendown()
    penup()
    backward((row_value+1)*radius)
    left(90)
    forward(radius*2)
    right(90)
    row_value -=1
victory()