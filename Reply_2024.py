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
            line = file[i]
            gp = GoldenPoint()
            gp.x = line[0]
            gp.y = line[1]
            GPList.append(gp)

        printf(GPList, "GPList: ")

        file = file[Gn:]
        
        SPList = []
        for i in range(0,Sm):
            line = file[i]
            sp = SilverPoint()
            sp.x = line[0]
            sp.y = line[1]
            sp.sc = line[2]
            SPList.append(sp)

        for i in range(0,Tl): 
            line = file[i]
            tl = SilverPoint()
            tl.id = line[0]
            tl.y = line[1]
            sp.sc = line[2]
            SPList.append(sp)

        file = file[1:]
        

       



if __name__ == "__main__":
    input = Input()
    