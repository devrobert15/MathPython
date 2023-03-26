#Verifica se um número é primo
import math
b=True
numero=int(input("Introduza o número inteiro maior ou igual a 1 "))
if numero == 1 or (numero!=2 and numero%2==0):
    print("O número {} não é primo.".format(numero))
    exit()
else:
    for i in range(3,int(math.sqrt(numero))):
        if numero%i==0:
            print("O número {} não é primo.".format(numero))
            exit()
print("O número {} é primo.".format(numero))


