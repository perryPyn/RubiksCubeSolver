from turtle import *
hideturtle()
bgcolor('white')
speed(1000)
goto(-75,300)

cube = {'u':['#FFFFFF']*9,
        'd':['yellow']*9,
        'l':['green']*9,
        'r':['blue']*9,
        'b':['orange']*9,
        'f':['red']*9,
        't':[0,0,0,0,0,0,0,0,0]}

def Square(color :str):
    fillcolor(color)
    begin_fill()
    for i in range(4):
        forward(50)
        right(90)
    end_fill()
    forward(50)
    goto(pos()[0]-25,pos()[1]-35)
    write("9", align="center", font=("Courier", 16, "bold"))
    goto(pos()[0]+25,pos()[1]+35)

Square('white')
done()