speed(0)
length = 40
color_value = "red"

def red_square():
    pendown()
    color("red")
    begin_fill()
    for i in range(4):
        forward(length)
        left(90)
    end_fill()
    penup()
    forward(length)
    color_value = "red"
    
def black_square():
    pendown()
    color("black")
    begin_fill()
    for j in range(4):
        forward(length)
        left(90)
    end_fill()
    penup()
    forward(length)
    color_value = "black"


penup()
setposition(-200,-200)
for l in range(10):
    for k in range(10):
        if (l+k)%2 == 0:
            red_square()
        elif (l+k)%2 != 0:
            black_square()
    
    penup()
    backward(400)
    left(90)
    forward(length)
    right(90)