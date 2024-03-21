
from collections import OrderedDict
import math

def printf(smth, mess=""):
    print(str(mess) + str(smth) + "\n")
    
file = open('REPLY.txt').read()

file = file.split('\n')

printf(file)

W,H = file[0].split(' ')

printf(W)
printf(H)

N,M,R = file[1].split(' ')

bx = []
by = []
bl = []
bc = []
ar = []
ac = []

printf(N,"N: ")
for i in range(2,int(N) + 2):
    line = file[i].split(' ')
   
    bx.append(int(line[0]))
    by.append(int(line[1]))
    bl.append(int(line[2]))
    bc.append(int(line[3]))

for i in range(int(N)+2 , int(M) + int(N)+ 2):
    line = file[i].split(' ')
    printf(line, "Line: ")
   
    ar.append(int(line[0]))
    ac.append(int(line[1]))


printf(bx)
printf(by)
printf(bl)
printf(bc)


printf(ar)
printf(ac)

