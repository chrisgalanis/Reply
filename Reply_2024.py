def printf(smth, mess=""):
    print(str(mess) + str(smth) + "\n")


class Input:
    def __init__(self):
        file = open('REPLY.txt').read()

        file = file.split('\n')

        # self.printf(file)

        W,H = file[0].split(' ')
        W = int(W)
        H = int(H)
        printf(W,"W: ")
        printf(H, "H: ")
        file = file[1:]

        N,M,R = file[0].split(' ')
        N = int(N)
        M = int(M)
        R = int(R)
        printf(N,"N: ")
        printf(M,"M: ")
        printf(R,"R: ")
        file = file[1:]
        

        bx = []
        by = []
        bl = []
        bc = []
        ar = []
        ac = []



if __name__ == "__main__":
    input = Input()
    