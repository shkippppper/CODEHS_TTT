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

secret_number = 5
user_number = 1
while user_number != secret_number:
    user_number = int(input("guess number"))
tick()