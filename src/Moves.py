def R(cube):
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[47:50] = cubeCopy[2:5]
    cube[2:5] = cubeCopy[38:41]
    cube[38:41] = cubeCopy[11:14]
    cube[11:14] = cubeCopy[47:50]

    for i in range(18,24): cube[i+2] = cubeCopy[i]
    cube[18:20] = cubeCopy[24:26]

    cube = ''.join(cube)
    return cube

def Rp(cube):
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[2:5] = cubeCopy[47:50]
    cube[38:41] = cubeCopy[2:5]
    cube[11:14] = cubeCopy[38:41]
    cube[47:50] = cubeCopy[11:14]

    for i in range(18,24): cube[i] = cubeCopy[i+2]
    cube[24:26] = cubeCopy[18:20]

    cube = ''.join(cube)
    return cube

def L(cube):
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[6:8] = cubeCopy[51:53]  ;cube[0] = cubeCopy[45]
    cube[51:53] = cubeCopy[15:17];cube[45] = cubeCopy[9]
    cube[15:17] = cubeCopy[42:44];cube[9] = cubeCopy[36]
    cube[42:44] = cubeCopy[6:8]  ;cube[36] = cubeCopy[0]

    for i in range(27,33): cube[i+2] = cubeCopy[i]
    cube[27:29] = cubeCopy[33:35]
    cube = ''.join(cube)    
    return cube
def Lp(cube):
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[51:53] = cubeCopy[6:8]  ;cube[45] = cubeCopy[0]
    cube[15:17] = cubeCopy[51:53];cube[9] = cubeCopy[45]
    cube[42:44] = cubeCopy[15:17];cube[36] = cubeCopy[9]
    cube[6:8] = cubeCopy[42:44]  ;cube[0] = cubeCopy[36]

    for i in range(27,33): cube[i] = cubeCopy[i+2]
    cube[33:35] = cubeCopy[27:29]

    cube = ''.join(cube)    
    return cube

def U(cube):
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[36:39] = cubeCopy[18:21]
    cube[18:21] = cubeCopy[49:52]
    cube[49:52] = cubeCopy[27:30]
    cube[27:30] = cubeCopy[36:39]

    for i in range(0,6): cube[i+2] = cubeCopy[i]
    cube[0:2] = cubeCopy[6:8]

    cube = ''.join(cube)        
    return cube
def Up(cube):
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[18:21] = cubeCopy[36:39]
    cube[49:52] = cubeCopy[18:21]
    cube[27:30] = cubeCopy[49:52]
    cube[36:39] = cubeCopy[27:30]

    for i in range(0,6): cube[i] = cubeCopy[i+2]
    cube[6:8] = cubeCopy[0:2]

    cube = ''.join(cube)       
    return cube

def D(cube):
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[22:25] = cubeCopy[40:43]
    cube[45:48] = cubeCopy[22:25]
    cube[31:34] = cubeCopy[45:48]
    cube[40:43] = cubeCopy[31:34]

    for i in range(9,15): cube[i+2] = cubeCopy[i]
    cube[9:11] = cubeCopy[15:17]

    cube = ''.join(cube)        
    return cube
def Dp(cube):
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[40:43] = cubeCopy[22:25]
    cube[22:25] = cubeCopy[45:48]
    cube[45:48] = cubeCopy[31:34]
    cube[31:34] = cubeCopy[40:43]

    for i in range(9,15): cube[i] = cubeCopy[i+2]
    cube[15:17] = cubeCopy[9:11]

    cube = ''.join(cube)        
    return cube

def F(cube):
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[4:7] = cubeCopy[29:32]
    cube[29:32] = cubeCopy[9:12]
    cube[9:12] = [cubeCopy[24],cubeCopy[25],cubeCopy[18]]
    cube[24],cube[25],cube[18] = cubeCopy[4],cubeCopy[5],cubeCopy[6]

    for i in range(36,42): cube[i+2] = cubeCopy[i]
    cube[36:38] = cubeCopy[42:44]

    cube = ''.join(cube)        
    return cube
def Fp(cube):
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[29:32] = cubeCopy[4:7]
    cube[9:12] = cubeCopy[29:32]
    cube[24],cube[25],cube[18] = cubeCopy[9],cubeCopy[10],cubeCopy[11]
    cube[4],cube[5],cube[6] = cubeCopy[24],cubeCopy[25],cubeCopy[18]

    for i in range(36,42): cube[i] = cubeCopy[i+2]
    cube[42:44] = cubeCopy[36:38]

    cube = ''.join(cube)
    return cube

def B(cube):
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[0:3] = cubeCopy[20:23]
    cube[20:23] = cubeCopy[13:16]
    cube[13:16] = cubeCopy[33],cubeCopy[34],cubeCopy[27]
    cube[33],cube[34],cube[27] = cubeCopy[0:3]

    for i in range(45,51): cube[i+2] = cubeCopy[i]
    cube[45:47] = cubeCopy[51:53]

    cube = ''.join(cube)       
    return cube
def Bp(cube):
    cube = list(cube)
    cubeCopy = cube.copy()

    cube[2:5] = cubeCopy[47:50]
    cube[38:41] = cubeCopy[2:5]
    cube[11:14] = cubeCopy[38:41]
    cube[47:50] = cubeCopy[11:14]

    for i in range(18,24): cube[i] = cubeCopy[i+2]
    cube[24:26] = cubeCopy[18:20]

    cube = ''.join(cube)        
    return cube

moves = {"R": R ,"L" :L ,"U" :U ,"D" :D ,"F" :F ,"B" :B ,
         "R'":Rp,"L'":Lp,"U'":Up,"D'":Dp,"F'":Fp,"B'":Bp}