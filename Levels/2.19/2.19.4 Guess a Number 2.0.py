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

def up():
    penup()
    setposition(0,0)
    color("yellow")
    pensize(20)
    pendown()
    sety(-50)
    sety(50)
    right(45)
    forward(40)
    backward(40)
    left(90)
    backward(40)
    right(45)

def down():
    penup()
    setposition(0,0)
    color("yellow")
    pensize(20)
    pendown()
    sety(50)
    sety(-50)
    right(45)
    backward(40)
    forward(40)
    left(90)
    forward(40)
    right(45)
    

    
    
secret_number = 5
user_number = 1
while user_number != secret_number:
    user_number = int(input("guess number"))
    if user_number < secret_number:
        up()
    elif user_number > secret_number:
        down()
    else:
        clear()
        
    clear()
tick()