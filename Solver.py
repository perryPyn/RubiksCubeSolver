import os;os.system("cls" if os.name == "nt" else "clear")
from time import sleep
from turtle import *;hideturtle();screensize(500, 600, "black")

solveSequence = ''

index = [0,1,2,7,8,3,6,5,4]
colors = {"u":"#FFFFFF","d":"#FFFF00","r":"#0000FF","l":"#008000","f":"#FF0000","b":"#FF8C00"}

linkEdges = {"u":{1:("r",5),3:("f",1),5:('f',1),7:('l',1)},
             "l":{1:('u',1),3:('f',7),5:('d',7),7:("r",7)},
             "r":{1:('u',3),3:("r",3),5:('d',3),7:('f',3)},
             "b":{1:('d',5),3:("f",3),5:('u',1),7:('l',7)},
             "f":{1:('u',5),3:("f",7),5:('d',1),7:('l',3)},
             "d":{1:('f',5),3:("f",5),5:("r",1),7:('l',5)}}
linkFaces = {"u":{"r":(1,5),"f":(3,1),'f':(5,1),'l':(7,1)},
             "l":{'u':(1,1),'f':(3,7),'d':(5,7),"r":(7,7)},
             "r":{'u':(1,3),"r":(3,3),'d':(5,3),'f':(7,3)},
             "b":{'d':(1,5),"f":(3,3),'u':(5,1),'l':(7,7)},
             "f":{'u':(1,5),"f":(3,7),'d':(5,1),'l':(7,3)},
             "d":{'f':(1,5),"f":(3,5),"r":(5,1),'l':(7,5)}}
opposedColor = {"r":"l","l":"r","u":"d","d":"u","f":"b","b":"f"}

cube_o = "uuuuuuuuudddddddddrrrrrrrrrlllllllllfffffffffbbbbbbbbb" # len = 54
#       |+0      |+9      |+18     |+27     |+36     |+45     
cube = cube_o

def R():
    global cube
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[47:50] = cubeCopy[2:5]
    cube[2:5] = cubeCopy[38:41]
    cube[38:41] = cubeCopy[11:14]
    cube[11:14] = cubeCopy[47:50]

    for i in range(18,24): cube[i+2] = cubeCopy[i]
    cube[18:20] = cubeCopy[24:26]

    cube = ''.join(cube)
def Rp():
    global cube
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[2:5] = cubeCopy[47:50]
    cube[38:41] = cubeCopy[2:5]
    cube[11:14] = cubeCopy[38:41]
    cube[47:50] = cubeCopy[11:14]

    for i in range(18,24): cube[i] = cubeCopy[i+2]
    cube[24:26] = cubeCopy[18:20]

    cube = ''.join(cube)

def L():
    global cube
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[6:8] = cubeCopy[51:53]  ;cube[0] = cubeCopy[45]
    cube[51:53] = cubeCopy[15:17];cube[45] = cubeCopy[9]
    cube[15:17] = cubeCopy[42:44];cube[9] = cubeCopy[36]
    cube[42:44] = cubeCopy[6:8]  ;cube[36] = cubeCopy[0]

    for i in range(27,33): cube[i+2] = cubeCopy[i]
    cube[27:29] = cubeCopy[33:35]
    cube = ''.join(cube)
def Lp():
    global cube
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[51:53] = cubeCopy[6:8]  ;cube[45] = cubeCopy[0]
    cube[15:17] = cubeCopy[51:53];cube[9] = cubeCopy[45]
    cube[42:44] = cubeCopy[15:17];cube[36] = cubeCopy[9]
    cube[6:8] = cubeCopy[42:44]  ;cube[0] = cubeCopy[36]

    for i in range(27,33): cube[i] = cubeCopy[i+2]
    cube[33:35] = cubeCopy[27:29]

    cube = ''.join(cube)

def U():
    global cube
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[36:39] = cubeCopy[18:21]
    cube[18:21] = cubeCopy[49:52]
    cube[49:52] = cubeCopy[27:30]
    cube[27:30] = cubeCopy[36:39]

    for i in range(0,6): cube[i+2] = cubeCopy[i]
    cube[0:2] = cubeCopy[6:8]

    cube = ''.join(cube)
def Up():
    global cube
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[18:21] = cubeCopy[36:39]
    cube[49:52] = cubeCopy[18:21]
    cube[27:30] = cubeCopy[49:52]
    cube[36:39] = cubeCopy[27:30]

    for i in range(0,6): cube[i] = cubeCopy[i+2]
    cube[6:8] = cubeCopy[0:2]

    cube = ''.join(cube)

def D():
    global cube
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[22:25] = cubeCopy[40:43]
    cube[45:48] = cubeCopy[22:25]
    cube[31:34] = cubeCopy[45:48]
    cube[40:43] = cubeCopy[31:34]

    for i in range(9,15): cube[i+2] = cubeCopy[i]
    cube[9:11] = cubeCopy[15:17]

    cube = ''.join(cube)
def Dp():
    global cube
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[40:43] = cubeCopy[22:25]
    cube[22:25] = cubeCopy[45:48]
    cube[45:48] = cubeCopy[31:34]
    cube[31:34] = cubeCopy[40:43]

    for i in range(9,15): cube[i] = cubeCopy[i+2]
    cube[15:17] = cubeCopy[9:11]

    cube = ''.join(cube)

def F():
    global cube
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[4:7] = cubeCopy[29:32]
    cube[29:32] = cubeCopy[9:12]
    cube[9:12] = [cubeCopy[24],cubeCopy[25],cubeCopy[18]]
    cube[24],cube[25],cube[18] = cubeCopy[4],cubeCopy[5],cubeCopy[6]

    for i in range(36,42): cube[i+2] = cubeCopy[i]
    cube[36:38] = cubeCopy[42:44]

    cube = ''.join(cube)
def Fp():
    global cube
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[29:32] = cubeCopy[4:7]
    cube[9:12] = cubeCopy[29:32]
    cube[24],cube[25],cube[18] = cubeCopy[9],cubeCopy[10],cubeCopy[11]
    cube[4],cube[5],cube[6] = cubeCopy[24],cubeCopy[25],cubeCopy[18]

    for i in range(36,42): cube[i] = cubeCopy[i+2]
    cube[42:44] = cubeCopy[36:38]

    cube = ''.join(cube)

def B():
    global cube
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[0:3] = cubeCopy[20:23]
    cube[20:23] = cubeCopy[13:16]
    cube[13:16] = cubeCopy[33],cubeCopy[34],cubeCopy[27]
    cube[33],cube[34],cube[27] = cubeCopy[0:3]

    for i in range(45,51): cube[i+2] = cubeCopy[i]
    cube[45:47] = cubeCopy[51:53]

    cube = ''.join(cube)
def Bp():
    global cube
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[2:5] = cubeCopy[47:50]
    cube[38:41] = cubeCopy[2:5]
    cube[11:14] = cubeCopy[38:41]
    cube[47:50] = cubeCopy[11:14]

    for i in range(18,24): cube[i] = cubeCopy[i+2]
    cube[24:26] = cubeCopy[18:20]

    cube = ''.join(cube)

moves = {"R": R ,"L" :L ,"U" :U ,"D" :D ,"F" :F ,"B" :B ,
         "R'":Rp,"L'":Lp,"U'":Up,"D'":Dp,"F'":Fp,"B'":Bp}



def FormatterSequence(sequence):
    if sequence == "o" : return
    sequence = sequence.upper()#;print("sequence :",sequence)
    return (lambda res=[], i=0: (
        (lambda f: f(f, res, i))(
            lambda f, r, i: r if i >= len(sequence) else (
                r.extend([sequence[i], sequence[i]]) or f(f, r, i+2) if i+1 < len(sequence) and sequence[i+1] == '2' else
                r.extend([sequence[i]+'\'']) or f(f, r, i+2) if i+1 < len(sequence) and sequence[i+1] == "'" else
                r.append(sequence[i]) or f(f, r, i+1)
            )
        )
    ))()
def Sequence(sequence:str):
    sequence = FormatterSequence(sequence)
    global cube
    for move in sequence:
        moves[move]()

def RechercheCroix(scramble):
    Sequence(scramble)
    global cube
    c = 0
    dico_cubes = {cube:""} # cube state : "sequence to get to it"
    cube_a_traiter = [cube]
    while cube_a_traiter != []:
        for cube_precedent in cube_a_traiter:
            cube_a_traiter.remove(cube)
            for move in moves :
                cube = cube_precedent
                moves[move]()
                sequence = dico_cubes[cube_precedent] + move
                if [cube[i] for i in [1,3,5,7]] == ["u","u","u","u"]: # on peut généraliser pour tous les coté pour la version color neutral
                    print("Cross sequence found after",c,"attempts :",sequence)# in",len(sequence),"moves"
                    cube = cube_o
                    return sequence
                if dico_cubes.get(cube) == None:
                    dico_cubes[cube] = sequence
                    cube_a_traiter.append(cube)
                elif len(dico_cubes[cube]) > len(sequence) :
                    dico_cubes[cube] = sequence
                c+=1
                

                           




def Square(color :str):
    fillcolor(color[:7])
    begin_fill()
    down()
    for i in range(4):
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
def TracerCube():
    clear();tracer(0)

    goto(-75,+300);Face(cube[0:9])
    goto(-75,-0)  ;Face(cube[9:18])
    goto(+75,150) ;Face(cube[18:27])
    goto(-225,150);Face(cube[27:36])
    goto(-75,150) ;Face(cube[36:45])
    goto(-75,-150);Face(cube[45:54])
    
    update()
def LireSequence(sequence):
    sequence = FormatterSequence(sequence)
    global cube
    TracerCube()
    sleep(1.5)
    for move in sequence:
        moves[move]()
        TracerCube()
        sleep(.5)

scramble = "L'B'D2B2L2D2FD2F'U2L2B'U2R'F'DU'LRU"
"R2L2U2D2F2B2FR2UD2B'DRUD2F2UR2U'F2DL2B2D2L2"
"RL2F2B2"

print("Scramble :",scramble)
# sequenceCroix = RechercheCroix(scramble)
LireSequence(scramble)
# LireSequence(sequenceCroix)
LireSequence("BBBL'FRL")
done()