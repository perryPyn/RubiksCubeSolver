from Display import *
from Moves import moves

solveSequence = ''

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

def Sequence(sequence:str):
    sequence = FormatSequence(sequence)
    global cube
    for move in sequence:
        cube = moves[move](cube)

def SearchForCross(scramble):
    Sequence(scramble)
    global cube
    dictCubes = {cube:""} # cube state : "sequence to get to it"
    cubesToTest = [cube]
    while cubesToTest:
        for cubePre in cubesToTest:
            cubesToTest.remove(cubePre)
            for move in moves :
                cube = cubePre
                cube = moves[move](cube)
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
    ...


def ForwardOriginChanger():...


e=1
match e:
    case 1: scramble = "R2L2U2D2F2B2FR2UD2B'DRUD2F2UR2U'F2DL2B2D2L2"
    case 2: scramble = "RL2F2B2"
    case 3: scramble = "L'B'D2B2L2D2FD2F'U2L2B'U2R'F'DU'LRU"


print("Scramble :",scramble)
startTime =time()
sequenceCroix = SearchForCross(scramble)
print("Temps de recherche :",time()-startTime)
Sequence(scramble)
LireSequence(cube,sequenceCroix)
done()