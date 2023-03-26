#Escreve lista de pares
n_inicial=int(input("Introduza o número inicial: "))
n_final=int(input("Introduza o número final: "))
for contador in range(n_inicial,n_final+1):
    if contador%2==0:
        print(contador)


