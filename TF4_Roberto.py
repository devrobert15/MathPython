#Programa que determina a dízima correspondente à fração dada
restos=[]
dizima=""
virgula=True
finita=False
print(restos)
numero=int(input("Introduza o numerador da fração: "))
den=int(input("Introduza o denominador da fração: "))
num=numero
while True:
    div_int=num//den
    dizima=dizima+str(div_int)
    if virgula:
        dizima=dizima+",("
    virgula=False
    if num%den==0:
        finita=True
        break
    if num%den in restos:
        break
    restos.append(num%den)
    num=num%den*10
if finita:
    dizima=str(numero/den)
else:
    dizima=dizima+")"
print (restos)
print (dizima)
