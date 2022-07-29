speed(2)
penup()

def yellow_circle():
    setposition(0,-100)
    color("yellow")
    pendown()
    begin_fill()
    circle(100)
    end_fill()
    penup()
    
def smile():
    setposition(-75,10)
    right(90)
    pendown()
    color("black")
    pensize(10)
    circle(75,180)
    penup()

def eyes():
    setposition(-30,40)
    right(90)
    begin_fill()
    circle(10)
    end_fill()
    penup()
    forward(60)
    begin_fill()
    circle(10)
    end_fill()

def draw_smiley():
    yellow_circle()
    smile()
    eyes()
    
def draw_frowney():
    yellow_circle()
    smile()
    eyes()

happy = input("Are you happy?(Y/N): ")

happy = input("Are you happy?(Yes/No) ")

if happy == "Yes":
    draw_smiley()