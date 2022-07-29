penup()
setx(-85)

def draw_full():
    pendown()
    begin_fill()
    for i in range(4):
        forward(20)
        left(90)
    end_fill()
    penup()
    forward(30)
    
        
    
def draw_empty():
    pendown()
    for i in range(4):
        forward(20)
        left(90)
    penup()
    forward(30)

for i in range(1,7,1):
    if i%2 ==0:
        draw_empty()
    else:
        draw_full() 