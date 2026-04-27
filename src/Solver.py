import os;os.system("cls" if os.name == "nt" else "clear")
from Display import *

solveSequence = ''

index = [0,1,2,7,8,3,6,5,4]
colors = {"u":"#FFFFFF","d":"#FFFF00","r":"#0000FF","l":"#008000","f":"#FF0000","b":"#FF8C00"}


opposedColor = {"r":"l","l":"r","u":"d","d":"u","f":"b","b":"f"}
crossColor ={
                "u" : [( 1,"u"),( 3,"u"),( 5,"u"),( 7,"u"),(37,"f"),(19,"r"),(28,"l"),(50,"b")],
                "d" : [(10,"d"),(12,"d"),(14,"d"),(15,"d"),(41,"f"),(23,"r"),(32,"l"),(46,"b")],
                "r" : [(19,"r"),(21,"r"),(23,"r"),(25,"r"),(39,"f"),(3 ,"u"),(12,"d"),(48,"b")],
                "l" : [(28,"l"),(30,"l"),(32,"l"),(34,"l"),(43,"f"),(7 ,"u"),(16,"d"),(52,"b")],
                "f" : [(37,"f"),(39,"f"),(41,"f"),(43,"f"),(5 ,"u"),(25,"r"),(30,"l"),(10,"d")],
                "b" : [(46,"b"),(48,"b"),(50,"b"),(52,"b"),(1 ,"u"),(21,"r"),(34,"l"),(14,"d")]
            }


cube_o = "uuuuuuuuudddddddddrrrrrrrrrlllllllllfffffffffbbbbbbbbb" # len = 54
#         |+0      |+9      |+18     |+27     |+36     |+45     
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



def FormatSequence(sequence):
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
    sequence = FormatSequence(sequence)
    global cube
    for move in sequence:
        moves[move]()

def SearchForWCross(scramble):
    Sequence(scramble)
    global cube
    dictCubes = {cube:""} # cube state : "sequence to get to state"
    cubesToTest = [cube]
    while cubesToTest != []:
        for cubePre in cubesToTest:
            cubesToTest.remove(cube)
            for move in moves :
                cube = cubePre
                moves[move]()
                sequence = dictCubes[cubePre] + move
                if dictCubes.get(cube) == None:
                    if [cube[1],cube[3],cube[5],cube[7],cube[28],cube[37],cube[19],cube[50],] == ["u","u","u","u","l","f","r","b"] and [cube[19],cube[28],cube[37],cube[50]] == ["r","l","f","b"]:
                        print("White cross sequence found after",len(dictCubes),"attempts :",sequence)
                        cube = cube_o
                        return sequence
                    dictCubes[cube] = sequence
                    cubesToTest.append(cube)
                elif len(dictCubes[cube]) > len(sequence) : #Normalement n'arrive pas
                    dictCubes[cube] = sequence

def SearchForCross(scramble):
    Sequence(scramble)
    global cube
    dictCubes = {cube:""} # cube state : "sequence to get to it"
    cubesToTest = [cube]
    while cubesToTest != []:
        for cubePre in cubesToTest:
            cubesToTest.remove(cube)
            for move in moves :
                cube = cubePre
                moves[move]()
                sequence = dictCubes[cubePre] + move
                if dictCubes.get(cube) == None:
                    for face in crossColor: # Pour chaque face du cube
                        correctCross = True
                        for edge,faceColor in crossColor[face]: # On regarde l'arrête et la couleur de la face associée
                            if cube[edge] != faceColor :
                                correctCross = False
                                break
                        if correctCross == True:
                            print(face,"cross sequence found after",len(dictCubes)+1,"attempts :",sequence)
                            cube = cube_o
                            #print(dictCubes.values())
                            return sequence

                    dictCubes[cube] = sequence
                    cubesToTest.append(cube)

def SearchForXCross(scramble):
    Sequence(scramble)
    global cube
    attempts = 0
    dictCubes = {cube:""} # cube state : "sequence to get to it"
    cubesToTest = [cube]
    while cubesToTest != []:
        for cubePre in cubesToTest:
            cubesToTest.remove(cube)
            for move in moves :
                cube = cubePre
                moves[move]()
                sequence = dictCubes[cubePre] + move
                for face,offset in [("u",0),("d",9),("r",18),("l",27),("f",36),("b",45)]:
                    if [cube[i] for i in [1+offset,3+offset,5+offset,7+offset]] == [face,face,face,face]: # on peut généraliser pour tous les coté pour la version color neutral
                        if face in [cube[i] for i in [0+offset,2+offset,4+offset,6+offset]] :
                            print("X-Cross sequence found after",attempts,"attempts :",sequence)# in",len(sequence),"moves"
                            cube = cube_o
                            return sequence
                if dictCubes.get(cube) == None:
                    dictCubes[cube] = sequence
                    cubesToTest.append(cube)
                attempts+=1  


def ForwardOriginChanger():...
    



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
    sequence = FormatSequence(sequence)
    global cube
    TracerCube()
    sleep(1.5)
    for move in sequence:
        moves[move]()
        TracerCube()
        sleep(.5)


e=2
match e:
    case 1: scramble = "R2L2U2D2F2B2FR2UD2B'DRUD2F2UR2U'F2DL2B2D2L2"
    case 2: scramble = "RL2F2B2"
    case 3: scramble = "L'B'D2B2L2D2FD2F'U2L2B'U2R'F'DU'LRU"


print("Scramble :",scramble)
startTime =time()
sequenceCroix = SearchForCross(scramble)
print("Temps de recherche :",time()-startTime)
Sequence(scramble)
LireSequence(sequenceCroix)
done()