radius = int(input("input the bottom radius - "))

def circular(radius):
    color("gray")
    pendown()
    begin_fill()
    circle(radius)
    end_fill()
    penup()
    left(90)
    forward(radius*2)
    right(90)
    
    
penup()
setposition(0,-200)
for i in range(3):
    
    circular(radius)
    radius /=2