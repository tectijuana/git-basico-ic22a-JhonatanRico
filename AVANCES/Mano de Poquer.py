import random 
from random import choice

yh = []
ch = []
mh = []
sh = []

for i in range(5):
    a = choice(['A',2,3,4,5,6,7,8,9,10,'J','Q','K'])
    yh.append(a)
    b = choice(['A',2,3,4,5,6,7,8,9,10,'J','Q','K'])
    ch.append(b)

c = 0
x = 0
l = len(yh)
for x in range(l):
   y = 1
   for y in range(l):
      if (yh[y] == yh[x]):
         c += 1
         if (yh.count(yh[x]) >= 2):
            mh.append("*")
         else:
            c = 0
            continue 

print("Tu mano: ",list(yh))

c2 = 0
x2 = 0
l2 = len(ch)
for x2 in range(l2):
   y2 = 1
   for y2 in range(l2):
      if (ch[y2] == ch[x2]):
         c2 += 1
         if (ch.count(ch[x2]) >= 2):
            sh.append("*")
         else:
            c2 = 0
            continue

print("Mano del CPU: ",list(ch))

print()

lm = len(mh)/2
ls = len(sh)/2
if (lm > ls):
   print("El jugaador ha ganado la partida")
elif (ls > lm):
   print("La computadora ha ganado la partida")
elif ((lm == ls) and (lm >= 1) and (ls >= 1)):
   print("A por el par mas alto ( Gana el par mas alto )")
else:
   print("A por la carta mas alta de la mano")