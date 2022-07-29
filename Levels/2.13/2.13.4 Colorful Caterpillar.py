penup()
radius = int(input("input radius - "))
setx(radius*8*-1+radius)

def circular(radius):
    color_choice = input("input color - ")
    color(color_choice)
    pendown()
    begin_fill()
    circle(radius)
    end_fill()
    penup()
    forward(radius*2)

for i in range(8):    
    circular(radius)