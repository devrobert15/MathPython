#Raízes de uma equação do 2ºgrau
import math
a=int(input("Introduza o valor de a:"))
b=int(input("Introduza o valor de b:"))
c=int(input("Introduza o valor de c:"))
delta=b**2-4*a*c

if delta<0:
    print("Esta equação não possui raizes reais.")
else:
    x1 = float((-b - math.sqrt(delta)) / (2 * a))
    x2 = float((-b + math.sqrt(delta)) / (2 * a))
    if delta==0:
        print("A raiz dupla desta equação é: ", x1)
    else:
        if x1<x2:
            print("As raízes da equação são: {} e {}".format(x1,x2))
        else:
            print("As raízes da equação são: {} e {}".format(x2,x1))
