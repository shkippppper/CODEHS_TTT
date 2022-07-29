square_length = int(input("input the square length - "))

def square(len):
    for i in range(4):
        forward(len)
        left(90)

penup()
setposition(-200,-200)
pendown()
square(square_length)
penup()
setposition(200-square_length,-200)
pendown()
square(square_length)
penup()
setposition(-200,200-square_length)
pendown()
square(square_length)
penup()
setposition(200-square_length,200-square_length)
pendown()
square(square_length)