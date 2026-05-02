from Display import *
from Utils import *
from Moves import moves

solveSequence = ''


e=1
match e:
    case 1: scramble = "R2L2U2D2F2B2FR2UD2B'DRUD2F2UR2U'F2DL2B2D2L2"
    case 2: scramble = "RL2F2B2"
    case 3: scramble = "L'B'D2B2L2D2FD2F'U2L2B'U2R'F'DU'LRU"



cube = Sequence(cube_o, scramble)
startTime =time()
sequenceCroix = SearchForCross(cube, scramble)
print("Temps de recherche :",time()-startTime)


print("Scramble :",scramble)
LireSequence(cube_o,[scramble,sequenceCroix])
