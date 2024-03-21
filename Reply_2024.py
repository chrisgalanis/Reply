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

    
    
if __name__ == "__main__":
    input = Input()
    