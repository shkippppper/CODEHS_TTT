def return_center():
    penup()
    setposition(0,0)
    pendown()
    
def draw_a_circle(rad,radinc,collor):
    right(90)
    penup()
    forward(rad)
    pendown()
    color(collor)
    begin_fill()
    left(90)
    circle(rad)
    end_fill()
    
    
radius = 100
RADIUS_INCREASE = 25
for i in range(4):
    return_center()
    color_choice = input("choose a color")
    draw_a_circle(radius,RADIUS_INCREASE,color_choice)
    radius -=RADIUS_INCREASE