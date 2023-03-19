#Programa para determinar a medida de um dos lados de um triângulo retângulo
import math
while True:
    incognita = str(input("Qual é a medida desconhecida? cateto(c) hipotenusa(h) \n  Digita a letra correspondente: ")).upper().strip()
    if incognita != 'H' and incognita != 'C':
        continue
    break
if incognita=="H":
    cat1=float(input("Introduza a medida de um dos catetos: "))
    cat2=float(input("Introduza a medida do outro cateto: "))
    res=math.sqrt(cat1**2+cat2**2)
    txt="da hipotenusa"
elif incognita=="C":
    hip = float(input("Introduza a medida da hipotenusa: "))
    cat1 = float(input("Introduza a medida do outro cateto: "))
    while hip<cat1:
        print("A medida da hipotenusa tem que ser maior que a medida do cateto!")
        hip = float(input("Introduza a medida da hipotenusa: "))
        cat1 = float(input("Introduza a medida do outro cateto: "))
    res=math.sqrt(hip**2-cat1**2)
    txt="do outro cateto"
print("A medida",txt, "é ",res )