# faceradius = 100
# eyesradius = 10
# sizepen = 10

# answer = input("are you happy?  ")

    
# def face():
#     penup()
#     sety(0-faceradius)
#     pendown()
#     color("yellow")
#     begin_fill()
#     circle(faceradius)
#     end_fill()
    
#     penup()
#     setposition(-30,30)
#     pendown()
#     color("black")
#     begin_fill()
#     circle(eyesradius)
#     end_fill()
    
#     penup()
#     setposition(30,30)
#     pendown()
#     begin_fill()
#     circle(eyesradius)
#     end_fill()
    
#     penup()
#     setposition(-50,0)
#     pendown()
#     pensize(sizepen)
#     right(90)
#     circle(50,180,0)
    
# if answer == ("Yes"):
#     face()



speed()
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

happy = input("Are you happy?(Y/N): ")

happy = input("Are you happy?(Yes/No) ")

if happy == "Yes":
    draw_smiley()