#Determina a distância entre dois pontos
import math
x1=int(input("Introduza a abcissa do primeiro ponto:"))
y1=int(input("Introduza a ordenada do primeiro ponto:"))
x2=int(input("Introduza a abcissa do segundo ponto:"))
y2=int(input("Introduza a ordenada do segundo ponto:"))
d=math.sqrt((x2-x1)**2+(y2-y1)**2)
'''print("A distância dos pontos de coordenadas ({},{}) e ({},{}) é {}".format(x1,y1,x2,y2,d))'''
if d>=10:
    print("longe")
else:
    print("perto")

