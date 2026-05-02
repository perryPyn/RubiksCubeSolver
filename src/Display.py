from time import sleep
from turtle import fillcolor,begin_fill,down,forward,right,end_fill,up,goto,pos,clear,tracer,update,done,hideturtle,screensize;hideturtle();screensize(500, 600, "black")
from Moves import *
from Utils import FormatSequence

index = [0,1,2,7,8,3,6,5,4]
colors = {"u":"#FFFFFF","d":"#FFFF00","r":"#0000FF","l":"#008000","f":"#FF0000","b":"#FF8C00"}



def Square(color :str):
    fillcolor(color[:7])
    begin_fill()
    down()
    for _ in range(4):
        forward(50)
        right(90)
    end_fill()
    forward(50)
    up()
def Face(face :list):
    i = 0
    for _ in range(3):
        for _ in range(3):
            Square(colors[face[index[i]]])
            i+=1
        goto(pos()[0]-150,pos()[1]-50)
def TracerCube(cube):
    clear();tracer(0)

    goto(-75,+300);Face(cube[0:9])
    goto(-75,-0)  ;Face(cube[9:18])
    goto(+75,150) ;Face(cube[18:27])
    goto(-225,150);Face(cube[27:36])
    goto(-75,150) ;Face(cube[36:45])
    goto(-75,-150);Face(cube[45:54])
    
    update()
def LireSequence(cube, sequence):
    for sequence in sequence :
        sequence = FormatSequence(sequence)
        TracerCube(cube)
        sleep(1.5)
        for move in sequence:
            cube = moves[move](cube)
            TracerCube(cube)
            sleep(.2)
    done()