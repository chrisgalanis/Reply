def printf(smth, mess=""):
    print(str(mess) + str(smth) + "\n")


class GoldenPoint:
    x = 0
    y = 0

class SilverPoint:
    x = 0
    y = 0
    sc = 0 #score

class Tiles:
    id = 0
    cost = 0
    number = 0




class Input:
    def __init__(self):
        file = open('REPLY.txt').read()

        file = file.split('\n')

        # self.printf(file)

        W,H, Gn, Sm, Tl = file[0].split(' ')
        W = int(W)
        H = int(H)
        Gn = int(Gn)
        Sm = int(Sm)
        Tl = int(Tl)

        printf(W,"W: ")
        printf(H, "H: ")

        file = file[1:]

        GPList = []
       
        for i in range(0,Gn):
            line = file[i].split(' ')
            gp = GoldenPoint()
            gp.x = int(line[0])
            gp.y = int(line[1])
            printf(gp.y,"Y: ")
            GPList.append(gp)

        # printf(GPList, "GPList: ")

        file = file[Gn:]
        
        SPList = []
        for i in range(0,Sm):
            line = file[i].split(' ')
            sp = SilverPoint()
            sp.x = int(line[0])
            sp.y = int(line[1])
            sp.sc = int(line[2])
            SPList.append(sp)
        
        file = file[Sm:]
        # printf(len(SPList), "SPList: ")
        AllTiles = {}
        for i in range(0,Tl): 
            line = file[i].split(' ')
            tl = Tiles()
            tl.id = line[0]
            tl.cost = int(line[1])
            tl.number = int(line[2])
            AllTiles[tl.id] = tl


        for key, value in AllTiles.items():
            print(key, "->", value.number)

        

       
def turnTiles():
    DR = ['9','D','B','F']
    DL = ['A','E', 'B', 'F']
    UR = ['5','D','7','F']
    UL = ['6', 'E', '7', 'F']
Moves = []
def calculate_path(startpos, endpos):
    
    #equate y
    j = 0 #index for updown array
    ydiff = startpos.y - finishpos.y
    for i in range (0,ydiff):
        ytile = Up_Down[j]
        if (AllTiles[ytile].number == 0):
            print("Not enough tiles of type: ", ytile)
        AllTiles[ytile].number -= 1
        if (j>3): 
                 print("Not enough tiles to go to 0 `", endpos)
                 break
        if (AllTiles[ytile].number==0):
            j+=1  
      
        Moves.append(Up_Down[j])
    #equate x
    k = 0 #index for lefrright array
    xdiff = startpos.x - finishpos.x
    for i in range (0,xdiff):
        xtile = Left_Right[k]
        if (AllTiles[xtile].number == 0):
            print("Not enough tiles of type: ", xtile)
        AllTiles[xtile].number -= 1
        if (k>3): 
                 print("Not enough tiles to go to 0 `", endpos)
                 break
        if (AllTiles[xtile].number==0):
            k+=1  
        Moves.append(Left_Right[k])
    return (endpos.x, endpos.y)
    
    
if __name__ == "__main__":
    input = Input()