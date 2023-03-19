#Programa para determinar as raizes, complexas ou reais, de uma equação do 2º grau com coeficientes inteiros
import math
while True:
    try:
        a = int(input("Introduza o valor de a: "))
        break
    except ValueError:
        print("Por favor introduza um número inteiro.")
while True:
    try:
        b = int(input("Introduza o valor de b: "))
        break
    except ValueError:
        print("Por favor introduza um número inteiro.")

while True:
    try:
        c = int(input("Introduza o valor de c: "))
        break
    except ValueError:
        print("Por favor introduza um número inteiro.")

delta = b ** 2 - 4 * a * c

if delta < 0:
    delta=-delta
    p_real=float(-b/(2*a))
    p_img=float(math.sqrt(delta)/(2*a))
    x1=complex(float(-b/(2*a)), -float(math.sqrt(delta)/(2*a)))
    x2 = complex(float(-b/(2 * a)), float(math.sqrt(delta) / (2 * a)))
    print("Raizes complexas: ", end='')
    print(str(x1).replace("j", "i"), end='  ')
    print(str(x2).replace("j", "i"))
else:
    x1 = float((-b - math.sqrt(delta)) / (2 * a))
    x2 = float((-b + math.sqrt(delta)) / (2 * a))
    if delta == 0:
        print("A raiz dupla desta equação é: ", x1)
    else:
        if x1 < x2:
            print("Raízes reais: {} e {}".format(x1, x2))
        else:
            print("Raízes reais: {} e {}".format(x2, x1))