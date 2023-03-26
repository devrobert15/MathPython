#Determina o número de pares entre dois números
n_inicial=int(input("Introduza o número inicial: "))
n_final=int(input("Introduza o número final: "))
numeros=0
for contador in range(n_inicial,n_final+1):
    if contador%2==0:
        numeros+=1
print("Entre", n_inicial, "e", n_final, "há", numeros, "números pares.")

