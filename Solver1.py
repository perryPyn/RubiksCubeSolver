import re
import os;os.system("cls" if os.name == "nt" else "clear")

solveSequence = ''

index = [0,1,2,7,8,3,6,5,4]
colors = {'w':"#FFFFFF",'y':"#FFFF00",'g':"#008000",'b':"#0000FF",'o':"#FF8C00",'r':"#FF0000"}

linkEdges = {"u":{1:('b',5),3:('r',1),5:('f',1),7:('l',1)},
             "l":{1:('u',1),3:('f',7),5:('d',7),7:('b',7)},
             "r":{1:('u',3),3:('b',3),5:('d',3),7:('f',3)},
             "b":{1:('d',5),3:('r',3),5:('u',1),7:('l',7)},
             "f":{1:('u',5),3:('r',7),5:('d',1),7:('l',3)},
             "d":{1:('f',5),3:('r',5),5:('b',1),7:('l',5)}}
linkFaces = {"u":{'b':(1,5),'r':(3,1),'f':(5,1),'l':(7,1)},
             "l":{'u':(1,1),'f':(3,7),'d':(5,7),'b':(7,7)},
             "r":{'u':(1,3),'b':(3,3),'d':(5,3),'f':(7,3)},
             "b":{'d':(1,5),'r':(3,3),'u':(5,1),'l':(7,7)},
             "f":{'u':(1,5),'r':(3,7),'d':(5,1),'l':(7,3)},
             "d":{'f':(1,5),'r':(3,5),'b':(5,1),'l':(7,5)}}
opposedColor = {'b':'g','g':'b','w':'y','y':'w','r':'o','o':'r'}
linkColorFace = {"w":'u',"g":'l',"b":'r',"o":'b',"r":'f',"y":'d'}

cube_init = {"u":['w']*9,
             "l":['g']*9,
             "r":['b']*9,
             "b":['o']*9,
             "f":['r']*9,
             "d":['y']*9}
cube = cube_init.copy()
#for k in cube.keys():
#    cube[k] = [str(cube_init[k][0])+str(i) for i in range(0,9)]

def R(direction :int):
    if direction == 1:
        t = cube["u"].copy()
        for i in [2,3,4]: # Rotation de la tranche
            cube["u"][i] = cube["f"][i]
            cube["f"][i] = cube["d"][i]
            cube["d"][i] = cube["b"][i]
            cube["b"][i] = t[i]
            
        t = cube["r"].copy()
        for i in range(0,8): # Rotation de la face
            cube["r"][i%8] = t[(i-2)%8]
    else :
        for _ in range(3): R(1)
def L(direction :int):
    if direction == 1:
        t = cube["f"].copy()
        for i in [0,7,6]:
            cube["f"][i] = cube["u"][i]
            cube["u"][i] = cube["b"][i]
            cube["b"][i] = cube["d"][i]
            cube["d"][i] = t[i]
            
        t = cube["l"].copy()
        for i in range(0,8):
            cube["l"][i%8] = t[(i-2)%8]
    else :
        for _ in range(3): L(1)
def U(direction :int):
    if direction == 1:
        t = cube["f"].copy()
        for i in [0,1,2]: # Rotation de la tranche
            cube["f"][i] = cube["r"][i]
            cube["r"][i] = cube["b"][i+4]
            cube["b"][i+4] = cube["l"][i]
            cube["l"][i] = t[i]
            
        t = cube["u"].copy()
        for i in range(0,8): # Rotation de la face
            cube["u"][i%8] = t[(i-2)%8]
    else :
        for _ in range(3): U(1)
def D(direction :int):
    if direction == 1:
        t = cube["f"].copy()
        for i in [6,5,4]:
            cube["f"][i] = cube["l"][i]
            cube["l"][i] = cube["b"][i-4]
            cube["b"][i-4] = cube["r"][i]
            cube["r"][i] = t[i]
            
        t = cube["d"].copy()
        for i in range(0,8):
            cube["d"][i%8] = t[(i-2)%8]
    else :
        for _ in range(3): D(1)
def F(direction :int):
    if direction == 1:
        t = cube["u"].copy()
        for i in [0,1,2]:
            cube["u"][i+4]     = cube["l"][i+2]
            cube["l"][i+2]     = cube["d"][i]
            cube["d"][i]       = cube["r"][(i-2)%8]
            cube["r"][(i+6)%8] = t[i+4]
            
        t = cube["f"].copy()
        for i in range(0,8):
            cube["f"][i%8] = t[(i-2)%8]
    else :
        for _ in range(3): F(1)
def B(direction :int):
    if direction == 1:
        t = cube["u"].copy()
        for i in [0,1,2]:
            cube["u"][i]       = cube["r"][i+2]
            cube["r"][i+2]     = cube["d"][i+4]
            cube["d"][i+4]     = cube["l"][(i-2)%8]
            cube["l"][(i+6)%8] = t[i]
            
        t = cube["b"].copy()
        for i in range(0,8):
            cube["b"][i%8] = t[(i-2)%8]
    else :
        for _ in range(3): B(1)

#primaryMovement = {"R": R(1),  "L": L(1),  "U": U(1),  "D": D(1),  "F": F(1),  "B": B(1),
#                   "R'": R(-1),"L'": L(-1),"U'": U(-1),"D'": D(-1),"F'": F(-1),"B'": B(-1)}
def Sequence(sequence :str):
    sequence = sequence.upper() # Toutes les lettres sont en majuscule
    #print(sequence)
    sequence = sum(([m[0]]*2 if m.endswith('2') else [m] for m in re.findall(r"[A-Z](?:2|')?", sequence)), [])
    for move in sequence:
        match move:
            case "R":R(1)
            case "L":L(1)
            case "U":U(1)
            case "D":D(1)
            case "F":F(1)
            case "B":B(1)
            case "R'":R(-1)
            case "L'":L(-1)
            case "U'":U(-1)
            case "D'":D(-1)
            case "F'":F(-1)
            case "B'":B(-1)

def RechercheCroix(cube=cube,solveSequence=solveSequence):
    colorLeft = ['b','r','o','g']; c=0
    while colorLeft != []:
        c +=1 # Securité
        for face in cube.keys():
            for facet in range(1,8,2):
                if cube[face][facet] == 'w':                            # On vient de trouver une vignette blanche
                    #print(face,facet)

                    faceLinked,facetLinked = linkEdges[face][facet]
                    colorLinked = cube[faceLinked][facetLinked]         # Couleur de l'arrête
                    #print(faceLinked,facetLinked,colorLinked)
                    if colorLinked not in colorLeft: break              # Déjà faite ?

                    faceColor = cube[face][8]                           # Face avec le côté blanc de l'arrête
                    faceLinkedColor = cube[faceLinked][8]               # Face avec la couleur de l'arrête
                    #print(faceLinkedColor,linkColorFace[faceLinkedColor])

                    if colorLinked == faceLinkedColor :
                        if 'y' == faceColor:
                            Sequence(faceLinked+"2")
                            solveSequence += faceLinked+"2"
                        else :
                            Sequence(faceLinked)
                            if cube['u'][linkFaces['u'][faceLinked][0]] == 'w':
                                solveSequence += faceLinked
                            else :
                                Sequence(faceLinked+"2")
                                solveSequence += faceLinked+"'"

                    if colorLinked == opposedColor[faceLinkedColor] :
                        Sequence(face+"2" +linkColorFace[colorLinked])
                        if cube['u'][linkFaces['u'][faceLinked][0]] != 'w':
                            Sequence(linkColorFace[colorLinked]+"2")
                            solveSequence += face+"2"+linkColorFace[colorLinked]+"'"+face+"2"
                        else :
                            Sequence(face+"2")
                            solveSequence += face+"2"+linkColorFace[colorLinked]+face+"2"
                    colorLeft.remove(colorLinked) # On part du pcpe que c'est fini donc attention
                    break
        if c > 50 :
            print('OVERFLOW'); break
    print(solveSequence)
                        
"RL2F2B2"
"R2L2U2D2F2B2FR2UD2B'DRUD2F2UR2U'F2DL2B2D2L2"
Sequence("RL2F2B2")
RechercheCroix()



from turtle import *;hideturtle();bgcolor("black");goto(-75,300)
def Square(color :str):
    fillcolor(color[:7])
    begin_fill()
    for i in range(4):
        forward(50)
        right(90)
    end_fill()
    forward(50)

    goto(pos()[0]-25,pos()[1]-35)
    write(color[7:], align="center", font=("Courier", 16, "bold"))
    goto(pos()[0]+25,pos()[1]+35)
def Face(face :list):
    i = 0
    for _ in range(3):
        for _ in range(3):
            Square(colors[cube[face][index[i]]])
            i+=1
        goto(pos()[0]-150,pos()[1]-50)
def TracerCube():
    clear();up();tracer(0);Face("u");Face("f");Face("d");Face("b");goto(-225,150);Face("l");goto(75,150);Face("r");update();done()

TracerCube()