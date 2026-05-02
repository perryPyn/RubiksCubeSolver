from Moves import *

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

def FormatSequence(sequence):
    if not sequence or sequence == "o":
        return []
    
    sequence = sequence.upper().replace(" ", "")
    res = []
    i = 0
    while i < len(sequence):
        move = sequence[i]
        # Vérifie si le caractère suivant est un modificateur
        if i + 1 < len(sequence):
            if sequence[i+1] == "2":
                res.append(move)
                res.append(move)
                i += 2
                continue
            elif sequence[i+1] == "'":
                res.append(move + "'")
                i += 2
                continue
        
        res.append(move)
        i += 1
    return res

def Sequence(cube, sequence:str):
    sequence = FormatSequence(sequence)
    for move in sequence:
        cube = moves[move](cube)
    return cube

def SearchForWCross(cube, scramble):
    Sequence(cube, scramble)
    dictCubes = {cube:""} # cube state : "sequence to get to state"
    cubesToTest = [cube]
    while cubesToTest != []:
        for cubePre in cubesToTest:
            cubesToTest.remove(cubePre)
            for move in moves :
                cube = cubePre
                cube = moves[move](cube)
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

def SearchForCross(cube, scramble):
    Sequence(cube, scramble)
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

def SearchForXCross(scramble):...
def ForwardOriginChanger():...