radius = int(input("input radius - "))
colllor = input("input color - ")
collor = input("input color - ")

def square(radius,collor):
    penup()
    setposition(0,0)
    right(90)
    forward(radius)
    left(90)
    pendown()
    color(collor)
    begin_fill()
    circle(radius)
    end_fill()
    
def squuuare(radius,colllor):
    penup()
    setposition(0-radius,0-radius)
    pendown()
    color(colllor)
    begin_fill()
    for i in range(4):
        forward(radius*2)
        left(90)
    end_fill()
    
    

squuuare(radius,colllor)
square(radius,collor)