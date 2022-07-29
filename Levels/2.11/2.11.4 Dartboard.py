def return_center()
    penup()
    setposition(0,0)
    pendown()
    
def draw_a_circle(rad,radinc)
    right(90)
    penup()
    forward(rad)
    pendown()
    left(90)
    circle(rad)
    
radius = 25
RADIUS_INCREASE = 25
for i in range(4)
    return_center()
    draw_a_circle(radius,RADIUS_INCREASE)
    radius +=RADIUS_INCREASE