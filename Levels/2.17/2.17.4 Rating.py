rating = int(input("score - "))

def cross():
    color("red")
    pensize(20)
    left(45)
    backward(50)
    forward(100)
    backward(50)
    right(90)
    backward(50)
    forward(100)
    backward(50)
    left(45)

def line():
    color("yellow")
    pensize(20)
    forward(50)
    backward(100)
    forward(50)

def tick():
    color("green")
    pensize(20)
    penup()
    setx(-50)
    pendown()
    right(45)
    forward(50)
    left(90)
    forward(100)
    

if rating <4:
    cross()
elif rating ==5 :
    line()
elif rating ==6 :
    line()
elif rating ==7 :
    line()
else:
    tick()